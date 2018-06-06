# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
import requests
import subprocess

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

logger = LoggerInstance


#比较两边数据是否一致
def cmp(expect_data, cmp_data):
	if isinstance(expect_data, dict):
		"""若为dict格式"""
		if not cmp_data or not isinstance(cmp_data, dict):
			return False
		for key in expect_data:
			cmp_key = key
			if cmp_key not in cmp_data:
				if cmp_key.capitalize() not in cmp_data:
					return False
				else:
					cmp_key = cmp_key.capitalize()
			if not cmp(expect_data[key], cmp_data[cmp_key]):
				return False
		return True
	elif isinstance(expect_data, list):
		"""若为list格式"""
		if not cmp_data or not isinstance(cmp_data, list):
			return False

		if len(expect_data) > len(cmp_data):
			return False
		for src_list, dst_list in zip(sorted(expect_data), sorted(cmp_data)):
			if not cmp(src_list, dst_list):
				return False
		return True
	else:
		if str(expect_data) != str(cmp_data):
			return False
		else:
			return True

def _check_md5(node_list, request):
	md5 = None
	if node_list:
		for index in node_list:
			ip = Config.SERVICES[index]
			response = utils.base.con_test_service(ip, request)
			if not response or "result" not in response:
				print("no md5: "+ ip)
				return False
			else:
				print(response["result"])
				if not md5:
					md5 = response["result"]
				elif md5 is not response["result"]:
					print("not same")
					return False
	else:
		return False
	return True

#检查节点服务器State数据库是否一致
def check_node_state(node_list):
	request = {
		"method": "get_states_md5",
		"jsonrpc": "2.0",
		"id": 0,
	}
	return _check_md5(node_list, request)


def check_node_ledgerevent(node_list):
	request = {
		"method": "get_ledgerevent_md5",
		"jsonrpc": "2.0",
		"id": 0,
	}
	return _check_md5(node_list, request)

def check_node_block(node_list):
	request = {
		"method": "get_block_md5",
		"jsonrpc": "2.0",
		"id": 0,
	}
	return _check_md5(node_list, request)

#检查节点服务器State数据库是否一致
def check_node_all(node_list):
	return (check_node_state(node_list) and check_node_ledgerevent(node_list) and check_node_block(node_list))

#部署合约
#返回值： 部署的合约地址
def deploy_contract(task):
	deploy_first = False
	deploy_code_path = ""
	deploy_contract_addr = None
	for key in task.data():
		if key.upper() == "DEPLOY":
			deploy_first = task.data()[key]
		elif key.upper() == "CODE_PATH":
			deploy_code_path = task.data()[key]
	
	if deploy_first:
		logger.print("[ DEPLOY ] ")
		cmd = Config.TOOLS_PATH + "/deploy_contract.sh " + deploy_code_path + " name" + " \"this is desc\"" + " > tmp"
		p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
		print(cmd)
		begintime = time.time()
		secondpass = 0
		timeout = 3
		while p.poll() is None:
			secondpass = time.time() - begintime
			if secondpass > timeout:
				p.terminate()
				print("Error: execute " + cmd + " time out!")
			time.sleep(0.1)

		tmpfile = open("tmp", "r+")  # 打开文件
		contents = tmpfile.readlines()
		tmpfile.close()
		for line in contents:
			#for log
			logger.print(line.strip('\n'))

		for line in contents:
			regroup = re.search(r'Contract Address:(([0-9]|[a-z]|[A-Z])*)', line)
			if regroup:
				deploy_contract_addr = regroup.group(1)
				if deploy_contract_addr:
					break
		return deploy_contract_addr
	else:
		return None

def sign_transction(task, judge = True, process_log = True):
	task.set_type("cli")
	(result, response) = run_single_task(task, judge, process_log)
	return (result, response)

def call_signed_contract(signed_tx, pre = True):
	sendrawtxtask = Task(Config.BASEAPI_PATH + "/rpc/sendrawtransaction.json")
	if pre:
		sendrawtxtask.request()["params"] = [signed_tx, 1]
	else:
		sendrawtxtask.request()["params"] = [signed_tx]

	(result, response) = run_single_task(sendrawtxtask, True, False)

	sendrawtxtask.data()["RESPONSE"] = response

	if not response is None and ("result" in response and "Result" in response["result"]):
		response["result"]["Result String"] = HexToByte(response["result"]["Result"]).decode('iso-8859-1')

	logger.print("[ CALL CONTRACT ] " + json.dumps(sendrawtxtask.data(), indent = 4))

	return (result, response)

#运行合约
#task: 需要执行的task
#judge：是否需要比较结果
#pre: 是否需要预执行
# 返回值: (result: True or False, response: 网络请求， 如果result为False, 返回的是字符串)
def call_contract(task, judge = True, pre = True):
	try:
		logger.print("[-------------------------------]")
		logger.print("[ RUN      ] "+ "contract" + "." + task.name())
		
		taskdata = task.data()

		deploy_contract_addr = deploy_contract(task)
			
		#step 1: signed tx
		expect_response = None
		if "RESPONSE" in taskdata:
			expect_response = taskdata["RESPONSE"]

		if deploy_contract_addr:
			taskdata["REQUEST"]["Params"]["address"] = deploy_contract_addr.strip()

		(result, response) = sign_transction(task, True, False)

		task.data()["RESPONSE"] = response
		logger.print("[ SIGNED TX ] " + json.dumps(taskdata, indent = 4))

		#step 2: call contract
		signed_tx = None
		if not response is None and "result" in response and not response["result"] is None and "signed_tx" in response["result"]:
			signed_tx = response["result"]["signed_tx"]

		if signed_tx == None or signed_tx == '':
			raise Error("no signed tx")

		(result, response) = call_signed_contract(signed_tx, pre)

		if response is None or "error" not in response or str(response["error"]) != '0':
			raise Error("call contract error")

		if judge and expect_response:
			result = cmp(expect_response, response)
			if not result:
				raise Error("not except result")

		return (result, response)

	except Error as err:
		return (False, err.msg)

#执行单个webapi
# task: 需要执行的task
# judge: 是否需要结果判断
# process_log： 是否需要记录运行log
# 返回值: (result: True or False, response: 网络请求)
def run_single_task(task, judge = True, process_log = True):
	connecttype = task.type()
	name = task.name()
	start_time = time.time()

	if process_log:
		logger.print("[-------------------------------]")
		logger.print("[ RUN      ] "+ connecttype + "." + name)
	cfg_content = task.data()
	cfg_request = cfg_content["REQUEST"]
	cfg_response = cfg_content["RESPONSE"]
	if process_log:
		logger.print("[ PARAMS   ]" + json.dumps(cfg_content, indent = 4))

	#(result, response) = self.multithread_run(logger, cfg_request, cfg_response)
	node_index = cfg_content["node_index"] if "node_index" in cfg_content else None
	node_ip = None
	if node_index:
		node_ip = Config.SERVICES[int(node_index)]

	response = utils.base.con(connecttype, node_ip, cfg_request)
	if process_log:
		logger.print("[ RESULT   ]" + json.dumps(response, indent = 4))

	end_time = time.time()
	time_consumed = (end_time - start_time) * 1000
	
	result = True
	if judge:
		result = cmp(cfg_response, response)
		if process_log:
			if result:
				logger.print("[ OK       ] " + connecttype + "."+ name +" (%d ms)" % (time_consumed))
			else:
				logger.print("[ Failed   ] " + connecttype + "."+ name +" (%d ms)"% (time_consumed))
			logger.print("[-------------------------------]")
			logger.print("")
	return (result, response)

#运行两个task
#假设 task1生成reponse1， task2得到reponse2， compare_src_key为 key1|key2, compare_dist_key为 key3|key4
#最终会比较reponse1["key1"]["key2"]和reponse2["key3"]["key4"]
#result: 比较结果 True or False
def run_pair_task(task1, task2, compare_src_key = None, compare_dist_key = None):
	result = True

	(result1, response1) = run_single_task(task1)
	if not result1:
		return result1

	(result2, response2) = run_single_task(task2)
	if not result2:
		return result2

	compare_src_data = response1
	if compare_src_key:
		compare_src_keys = compare_src_key.split('/')
		for key in compare_src_keys:
			if compare_src_data:
				compare_src_data = compare_src_data[key]
			else:
				break

		####split dist key
		compare_dist_data = response2
		if compare_dist_key:
			compare_dist_keys = compare_dist_key.split('/')
			for key in compare_dist_keys:
				if compare_dist_data:
					compare_dist_data = compare_dist_data[key]
				else:
					break
		result = cmp(compare_src_data, compare_dist_data)
	else:
		result = True

	return result

#暂停测试，需手动输入才能返回
# msg:暂停原因
# 返回值: 手动输入的值
def pause(msg):
	print(msg)
	command = ""
	try:
		command = sys.stdin.readline().strip('\n')
	except Exception as e:
		print(e)
	return command

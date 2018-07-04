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
		# 若为dict格式
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
		# 若为list格式
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
	isSame = True
	if node_list:
		for index in node_list:
			ip = Config.NODES[int(index)]["ip"]
			response = utils.base.con_test_service(ip, request)
			if not response or "result" not in response:
				print("no md5: "+ ip)
				isSame = False
			else:
				print(response["result"] + " [" + ip + "]")
				if not md5:
					md5 = response["result"]
				elif md5 != response["result"]:
					isSame = False
	else:
		isSame = False
	return isSame

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


def deploy_contract_full(neo_code_path, name = "name", desc = "this is desc", price = 0):
	if not neo_code_path or neo_code_path == "":
		return None

	deploy_contract_addr = None
	deploy_contract_txhash = None
	
	logger.print("[ DEPLOY ] ")
	cmd = Config.TOOLS_PATH + "/deploy_contract.sh " + neo_code_path + " \"" + name + "\" \"" + desc + "\" \"" + str(price) +  "\" > tmp"
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
	for line in contents:
		#for log
		logger.print(line.strip('\n'))

	for line in contents:
		regroup = re.search(r'Contract Address:(([0-9]|[a-z]|[A-Z])*)', line)
		if regroup:
			deploy_contract_addr = regroup.group(1)

		regroup = re.search(r'TxHash:(([0-9]|[a-z]|[A-Z])*)', line)
		if regroup:
			deploy_contract_txhash = regroup.group(1)

		if deploy_contract_addr and deploy_contract_txhash:
			break
	tmpfile.close()
	return (deploy_contract_addr, deploy_contract_txhash)
#部署合约
#返回值： 部署的合约地址
def deploy_contract(neo_code_path, name = "name", desc = "this is desc", price = 0):
	(deploy_contract_addr, deploy_contract_txhash) = deploy_contract_full(neo_code_path, name, desc, price)
	time.sleep(6)
	return deploy_contract_addr


def sign_transction(task, judge = True, process_log = True):
	if task.node_index() != None:
		print("sign transction with other node: " + str(task.node_index()))
		task.set_type("st")
		request = task.request()
		task.set_request({
							"method": "siginvoketx",
							"jsonrpc": "2.0",
							"id": 0,
						})
		task.request()["params"] = request

		(result, response) = run_single_task(task, False, process_log)
		if result:
			response = response["result"]
		return (result, response)
	else:
		task.set_type("cli")
		(result, response) = run_single_task(task, judge, process_log)
		return (result, response)

def call_signed_contract(signed_tx, pre = True, node_index = None):
	sendrawtxtask = Task(Config.BASEAPI_PATH + "/rpc/sendrawtransaction.json")
	if pre:
		sendrawtxtask.request()["params"] = [signed_tx, 1]
	else:
		sendrawtxtask.request()["params"] = [signed_tx]

	if node_index != None:
		sendrawtxtask.data()["NODE_INDEX"] = node_index
		
	(result, response) = run_single_task(sendrawtxtask, True, False)

	sendrawtxtask.data()["RESPONSE"] = response

	if not response is None and ("result" in response and "Result" in response["result"]):
		response["result"]["Result String"] = HexToByte(response["result"]["Result"]).decode('iso-8859-1')

	logger.print("[ CALL CONTRACT ] " + json.dumps(sendrawtxtask.data(), indent = 4))

	return (result, response)

#运行合约
#task: 需要执行的task
#judge: 是否需要比较结果
#pre: 是否需要预执行
# 返回值: (result: True or False, response: 网络请求， 如果result为False, 返回的是字符串)
def call_contract(task, judge = True, pre = True, twice = False):
	try:
		logger.print("\n\n[-------------------------------]")
		logger.print("[ RUN      ] "+ "contract" + "." + task.name())
		
		taskdata = task.data()
		node_index = None
		deploy_first = False;
		deploy_code_path = None;
		deploy_contract_addr = None
		for key in taskdata:
			if key.upper() == "DEPLOY":
				deploy_first = taskdata[key]
			if key.upper() == "CODE_PATH":
				deploy_code_path = taskdata[key]
			if key.upper() == "NODE_INDEX":
				node_index = int(taskdata[key])

		if deploy_first:
			deploy_contract_addr = deploy_contract(deploy_code_path)
		#step 1: signed tx
		expect_response = None
		expect_signresponse = None
		if "RESPONSE" in taskdata:
			expect_response = taskdata["RESPONSE"]

		if "SIGN_RESPONSE" in taskdata:
			expect_signresponse = taskdata["SIGN_RESPONSE"]

		if deploy_contract_addr:
			taskdata["REQUEST"]["Params"]["address"] = deploy_contract_addr.strip()

		(result, response) = sign_transction(task, True, False)

		task.data()["RESPONSE"] = response
		logger.print("[ SIGNED TX ] " + json.dumps(taskdata, indent = 4))

		#step 2: call contract
		if expect_signresponse != None:				
			result = cmp(expect_signresponse, response)
			if result and "error_code" in response and int(response["error_code"]) != 0:
				return (result, response) 

			if not result:
				raise Error("not except sign result")

		signed_tx = None
		if not response is None and "result" in response and not response["result"] is None and "signed_tx" in response["result"]:
			signed_tx = response["result"]["signed_tx"]

		if signed_tx == None or signed_tx == '':
			raise Error("no signed tx")

		if twice:
			(result, response) = call_signed_contract(signed_tx, True, node_index)
			(result1, response2) = call_signed_contract(signed_tx, False, node_index)
			response["txhash"] = response2["result"]
		else:
			(result, response) = call_signed_contract(signed_tx, pre, node_index)
	
		if response is None or "error" not in response:# or str(response["error"]) != '0':
			raise Error("call contract error")

		if judge and expect_response:
			result = cmp(expect_response, response)
			if not result:
				raise Error("not except result")

		response["signed_tx"] = signed_tx
		if deploy_contract_addr:
			response["address"] = taskdata["REQUEST"]["Params"]["address"]
		
		time.sleep(5)
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
	node_index = task.node_index()
	node_ip = None
	print(node_index)
	if node_index != None:
		node_ip = Config.NODES[int(node_index)]["ip"]
		print("run on other service: " + str(node_index) + "  " + node_ip)
		
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
	print("[ PAUSE     ] " + msg)
	command = ""
	try:
		command = sys.stdin.readline().strip('\n')
	except Exception as e:
		print(e)
	return command

#
def start_nodes(indexs, start_params = Config.DEFAULT_NODE_ARGS, clear_chain = False, clear_log = False, program = "ontology", config = "config.json"):
	for index in indexs:
		start_node(index, start_params, clear_chain, clear_log, program, config)

def start_node(index, start_params = Config.DEFAULT_NODE_ARGS, clear_chain = False, clear_log = False, program = "ontology", config = "config.json"):
	print("start node: " + str(index) + " start_params:" + start_params + " clear_chain:" + str(clear_chain) + " clear_log:" + str(clear_log))
	request = {
		"method": "start_node",
		"jsonrpc": "2.0",
		"id": 0,
		"params" : {
			"clear_chain" : clear_chain,
			"clear_log" : clear_log,
			"name" : program,
			"node_args" : start_params,
			"config" : config
		}
	}

	ip = Config.NODES[index]["ip"]
	response = utils.base.con_test_service(ip, request)

	return response

def stop_nodes(indexs):
	for index in indexs:
		stop_node(index)

def stop_node(index):
	print("stop node: " + str(index))
	request = {
		"method": "stop_node",
		"jsonrpc": "2.0",
		"id": 0
	}

	ip = Config.NODES[index]["ip"]
	response = utils.base.con_test_service(ip, request)

	return response

#
def replace_configs(indexs, config = None):
	for index in indexs:
		replace_config(index, config)
		
def replace_config(index, config = None):
	if not config:
		config = {
					"SeedList": ["139.219.140.190:20338",
					"139.219.138.144:20338",
					"139.219.128.181:20338",
					"139.219.133.116:20338"],
					"ConsensusType": "vbft",
					"VBFT": {
						"n": 7,
						"c": 2,
						"k": 7,
						"l": 112,
						"block_msg_delay": 10000,
						"hash_msg_delay": 10000,
						"peer_handshake_timeout": 10,
						"max_block_change_view": 200,
						"admin_ont_id": "did:ont:TA5dRCZE8pRcCMPLdF4uUYkT1zynkwCKGW",
						"min_init_stake": 10000,
						"vrf_value": "1c9810aa9822e511d5804a9c4db9dd08497c31087b0daafa34d768a3253441fa20515e2f30f81741102af0ca3cefc4818fef16adb825fbaa8cad78647f3afb590e",
						"vrf_proof": "c57741f934042cb8d8b087b44b161db56fc3ffd4ffb675d36cd09f83935be853d8729f3f5298d12d6fd28d45dde515a4b9d7f67682d182ba5118abf451ff1988",
						"peers": [{
							"index": 1,
							"peerPubkey": "12020258a22a27047610cd58cfc2d02aeda8381dd6f430dc5ddedb854b803271ab69f4",
							"address": "TA5dRCZE8pRcCMPLdF4uUYkT1zynkwCKGW",
							"initPos": 10000
						},
						{
							"index": 2,
							"peerPubkey": "120202d4b6ecc913b7f826055f3d7931657e494d5c45768e6c95ec139a912db03bac67",
							"address": "TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5",
							"initPos": 10000
						},
						{
							"index": 3,
							"peerPubkey": "12020390c9f71385bf0b21bf4c9feae5693c08b38bab078171c63398c06d174b19a413",
							"address": "TA5Uov3Pp9Ufej17NoV4NcXNZi8zFCAgEP",
							"initPos": 10000
						},
						{
							"index": 4,
							"peerPubkey": "120203483420b24240f9db477fb117d857bc6e537a1486eb803e2e702f7bb353eea481",
							"address": "TA82XAPQXtVzncQMczcY9SVytjb2VuTQy4",
							"initPos": 10000
						},
						{
							"index": 5,
							"peerPubkey": "1202032d9267a8542fcae0c5cca6d97f046a7c6a077e1237ee85aa607e83dbf1ef47ea",
							"address": "TA7TSQ5aJcA8sU5MpqJNyTG1r13AQYLYpR",
							"initPos": 10000
						},
						{
							"index": 6,
							"peerPubkey": "12020388e9f62a0d5c070d67b94bd7ec17957a950f953a401e2a2323f58d72431f3541",
							"address": "TA6HoPXWkxznDi3bSur1YaNaPy6Hr4XhM6",
							"initPos": 10000
						},
						{
							"index": 7,
							"peerPubkey": "120202657eab0d3060e47e7df105d5b2f360e826d2d4f406b99f9bd796f0ad6339bd86",
							"address": "TA8youx3VAU9yBSn5oxLR2V1dSGBkL2epq",
							"initPos": 10000
						}]
					}
				}

	request = {
		"method": "replace_node_config",
		"jsonrpc": "2.0",
		"id": 0,
		"params" : config
	}

	ip = Config.NODES[index]["ip"]
	response = utils.base.con_test_service(ip, request)

	return response

def transfer_ont(from_index, to_index, amount, price = 0):
	request = {
		"method": "transfer",
		"jsonrpc": "2.0",
		"id": 0,
		"params" : {
			"from" : Config.NODES[from_index]["address"],
			"to" : Config.NODES[to_index]["address"],
			"amount" : amount,
			"price" : price
		}
	}

	ip = Config.NODES[from_index]["ip"]
	response = utils.base.con_test_service(ip, request)
	time.sleep(5)
	return response

def transfer_ong(from_index, to_index, amount, price = 0):
	request = {
		"method": "transfer_ong",
		"jsonrpc": "2.0",
		"id": 0,
		"params" : {
			"from" : Config.NODES[from_index]["address"],
			"to" : Config.NODES[to_index]["address"],
			"amount" : amount,
			"price" : price
		}
	}

	ip = Config.NODES[from_index]["ip"]
	response = utils.base.con_test_service(ip, request)
	time.sleep(5)
	return response

def withdrawong(index):
	request = {
		"method": "withdrawong",
		"jsonrpc": "2.0",
		"id": 0
	}

	ip = Config.NODES[index]["ip"]
	response = utils.base.con_test_service(ip, request)

	return response

def script_hash_bl_reserver(input):
	if input == None:
		return ""
	rstrs = input[::-1]
	output = ""
	for i in range(0, len(input), 2):
		output = output + rstrs[i + 1]
		output = output + rstrs[i]
	return output

def base58_to_address(input):
	if input == None:
		return ""
	address = ""
	cmd = Config.TOOLS_PATH + "/base58ToAddress -base58 \"" + input + "\" > address.tmp"
	os.system(cmd)
	print(cmd)
	tmpfile = open("address.tmp", "r+")  # 打开文件
	contents = tmpfile.readlines()
	for line in contents:
		#for log
		logger.print(line.strip('\n'))

	for line in contents:
		regroup = re.search(r'address: (([0-9]|[a-z]|[A-Z])*)', line)
		if regroup:
			address = regroup.group(1)
	tmpfile.close()
	return address

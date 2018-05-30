# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

from utils.config import Config
from utils.baseapi import BaseApi
from utils.rpc import RPC
from utils.websocket import WS
from utils.cli import CLI
from utils.restful import Restful
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

logger = LoggerInstance
rpc = RPC()
cli = CLI()

def cmp(expect_data, cmp_data):
	if isinstance(expect_data, dict):
		"""若为dict格式"""
		if not cmp_data or not isinstance(cmp_data, dict):
			return False
		for key in expect_data:
			print(key)
			if key not in cmp_data:
				return False
			if not cmp(expect_data[key], cmp_data[key]):
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

def call_contract(task, judge = True):
	taskdata = task.data()
	if isinstance(taskdata, dict):
		taskdata = [taskdata]

	for task_item in taskdata:
		try:
			#step 1: signed tx
			expect_response = None
			if "RESPONSE" in task_item:
				expect_response = task_item["RESPONSE"]

			logger.print("[-------------------------------]")
			logger.print("[ RUN      ] "+ "contract" + "." + task.name())
			(result, response) = cli.run(task.name(), task_item)
			task.data()["RESPONSE"] = response
			logger.print("[ 1. SIGNED TX ] " + json.dumps(task_item, indent = 4))

			#step 2: call contract
			signed_tx = None
			if not response is None and "result" in response and not response["result"] is None and "signed_tx" in response["result"]:
				signed_tx = response["result"]["signed_tx"]

			if signed_tx == None or signed_tx == '':
				raise Error("no signed tx")

			sendrawtxtask = Task("tasks/webapi/rpc/sendrawtransaction")
			sendrawtxtask.data()["REQUEST"]["params"] = [signed_tx, 1]
			(result, response) = rpc.run(sendrawtxtask.name(), sendrawtxtask.data())

			sendrawtxtask.data()["RESPONSE"] = response
			sendrawtxtask.data()["EXPECT RESPONSE"] = expect_response

			if not response is None and ("result" in response and "Result" in response["result"]):
				response["result"]["Result String"] = HexToByte(response["result"]["Result"]).decode('iso-8859-1')
			
			logger.print("[ 2. CALL CONTRACT ] " + json.dumps(sendrawtxtask.data(), indent = 4))

			if response is None or "error" not in response or str(response["error"]) != '0':
				raise Error("call contract error")

			if judge and expect_response:
				result = cmp(expect_response, response)
				if not result:
					raise Error("not except result")

			return (result, response)

		except Error as err:
			return (False, err.msg)
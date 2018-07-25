# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')



from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.api.websocketapi import WebSocketApi
from utils.api.commonapi import *
from utils.base import WebSocket

time.sleep(2)
print("stop all")
stop_all_nodes()
print("start all")
start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
time.sleep(60)
print("waiting for 60s......")

from ws_api_conf import Conf

logger = LoggerInstance

wsapi = WebSocketApi()


class TestWebAPI(ParametrizedTestCase):
		

	def start(self, log_path):
		logger.open(log_path)

	def normal_finish(self, task_name, log_path, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()

	def abnormal_finish(self, task_name, log_path, result, msg):
		if not result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()
	
	def test_001_heartbeat(self):
		logger.open("test_001_heartbeat.log","test_001_heartbeat")
		(result, response) = wsapi.heartbeat()
		logger.close(result)

	def test_002_heartbeat(self):
		logger.open("test_002_heartbeat.log","test_002_heartbeat")
		stop_node(0)
		(result, response) = wsapi.heartbeat()
		start_node(0, Config.DEFAULT_NODE_ARGS)
		time.sleep(5)
		self.abnormal_finish(task_name, log_path, result, "")
	
	def test_003_heartbeat(self):
		logger.open("test_003_heartbeat.log","test_003_heartbeat")
		try:
			ws = WebSocket()
			ws.exec(heartbeat_gap=400)
			# (result, response) = wsapi.heartbeat()
		except:
			pass
		self.normal_finish(task_name, log_path, True, "")

	def test_004_subscribe(self):
		logger.open("test_004_subscribe.log","test_004_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT])
		logger.close(result)

	def test_005_subscribe(self):
		logger.open("test_005_subscribe.log","test_005_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_INCORRECT_2])
		logger.close(result)
	
	def test_006_subscribe(self):
		logger.open("test_006_subscribe.log","test_006_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_INCORRECT_3])
		logger.close(result)

	def test_007_subscribe(self):
		logger.open("test_007_subscribe.log","test_007_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sevent=True)
		logger.close(result)

	def test_008_subscribe(self):
		logger.open("test_008_subscribe.log","test_008_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sevent=False)
		logger.close(result)

	def test_009_subscribe(self):
		logger.open("test_009_subscribe.log","test_009_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sevent=None)
		logger.close(result)

	def test_010_subscribe(self):
		logger.open("test_010_subscribe.log","test_010_subscribe")
		(result, response) = wsapi.subscribe(None, sevent=True)
		logger.close(result)

	def test_011_subscribe(self):
		logger.open("test_011_subscribe.log","test_011_subscribe")
		(result, response) = wsapi.subscribe(None, sevent=0)
		logger.close(result)

	def test_012_subscribe(self):
		logger.open("test_012_subscribe.log","test_012_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sjsonblock=True)
		logger.close(result)

	def test_013_subscribe(self):
		logger.open("test_013_subscribe.log","test_013_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sjsonblock=False)
		logger.close(result)

	def test_014_subscribe(self):
		logger.open("test_014_subscribe.log","test_014_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sjsonblock=None)
		logger.close(result)

	def test_015_subscribe(self):
		logger.open("test_015_subscribe.log","test_015_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sjsonblock=0)
		logger.close(result)

	def test_016_subscribe(self):
		logger.open("test_016_subscribe.log","test_016_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], srawblock=True)
		logger.close(result)

	def test_017_subscribe(self):
		logger.open("test_017_subscribe.log","test_017_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], srawblock=False)
		logger.close(result)

	def test_018_subscribe(self):
		logger.open("test_018_subscribe.log","test_018_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], srawblock=None)
		logger.close(result)

	def test_019_subscribe(self):
		logger.open("test_019_subscribe.log","test_019_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], srawblock=0)
		logger.close(result)

	def test_020_subscribe(self):
		logger.open("test_020_subscribe.log","test_020_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=True)
		logger.close(result)

	def test_021_subscribe(self):
		logger.open("test_021_subscribe.log","test_021_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=False)
		logger.close(result)

	def test_022_subscribe(self):
		logger.open("test_022_subscribe.log","test_022_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=None)
		logger.close(result)

	def test_023_subscribe(self):
		logger.open("test_023_subscribe.log","test_023_subscribe")
		time.sleep(5)
		(result, response) = wsapi.subscribe([Conf.CONTRACT_ADDRESS_CORRECT], sblocktxhashs=0)
		logger.close(result)

	def test_024_getgenerateblocktime(self):
		logger.open("test_024_getgenerateblocktime.log","test_024_getgenerateblocktime")
		(result, response) = wsapi.getgenerateblocktime()
		logger.close(result)

	def test_025_getgenerateblocktime(self):
		logger.open("test_025_getgenerateblocktime.log","test_025_getgenerateblocktime")
		(result, response) = wsapi.getgenerateblocktime({"height":"1"})
		logger.close(result)

	def test_026_getconnectioncount(self):
		logger.open("test_026_getconnectioncount.log","test_026_getconnectioncount")
		(result, response) = wsapi.getconnectioncount()
		logger.close(result)

	def test_027_getconnectioncount(self):
		logger.open("test_027_getconnectioncount.log","test_027_getconnectioncount")
		stop_node(0)
		(result, response) = wsapi.getconnectioncount()
		start_node(0, Config.DEFAULT_NODE_ARGS)
		time.sleep(5)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_028_getconnectioncount(self):
		logger.open("test_028_getconnectioncount.log","test_028_getconnectioncount")
		(result, response) = wsapi.getconnectioncount({"height":"1"})
		logger.close(result)

	def test_029_getblocktxsbyheight(self):
		logger.open("test_029_getblocktxsbyheight.log","test_029_getblocktxsbyheight")
		(result, response) = wsapi.getblocktxsbyheight(Conf.HEIGHT_CORRECT)
		logger.close(result)

	def test_031_getblocktxsbyheight(self):
		logger.open("test_031_getblocktxsbyheight.log","test_031_getblocktxsbyheight")
		(result, response) = wsapi.getblocktxsbyheight(Conf.HEIGHT_BORDER)
		logger.close(result)

	def test_032_getblocktxsbyheight(self):
		logger.open("test_032_getblocktxsbyheight.log","test_032_getblocktxsbyheight")
		(result, response) = wsapi.getblocktxsbyheight(Conf.HEIGHT_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_033_getblocktxsbyheight(self):
		logger.open("test_033_getblocktxsbyheight.log","test_033_getblocktxsbyheight")
		(result, response) = wsapi.getblocktxsbyheight(Conf.HEIGHT_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_034_getblocktxsbyheight(self):
		logger.open("test_034_getblocktxsbyheight.log","test_034_getblocktxsbyheight")
		(result, response) = wsapi.getblocktxsbyheight(Conf.HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_035_getblockbyheight(self):
		logger.open("test_035_getblockbyheight.log","test_035_getblockbyheight")
		(result, response) = wsapi.getblockbyheight(Conf.HEIGHT_CORRECT)
		logger.close(result)

	def test_037_getblockbyheight(self):
		logger.open("test_037_getblockbyheight.log","test_037_getblockbyheight")
		(result, response) = wsapi.getblockbyheight(Conf.HEIGHT_BORDER)
		logger.close(result)

	def test_038_getblockbyheight(self):
		logger.open("test_038_getblockbyheight.log","test_038_getblockbyheight")
		(result, response) = wsapi.getblockbyheight(Conf.HEIGHT_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_039_getblockbyheight(self):
		logger.open("test_039_getblockbyheight.log","test_039_getblockbyheight")
		(result, response) = wsapi.getblockbyheight(Conf.HEIGHT_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_040_getblockbyheight(self):
		logger.open("test_040_getblockbyheight.log","test_040_getblockbyheight")
		(result, response) = wsapi.getblockbyheight(Conf.HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_041_getblockbyhash(self):
		logger.open("test_041_getblockbyhash.log","test_041_getblockbyhash")
		(result, response) = wsapi.getblockbyhash(Conf.BLOCK_HASH_CORRECT)
		logger.close(result)
	
	def test_043_getblockbyhash(self):
		logger.open("test_043_getblockbyhash.log","test_043_getblockbyhash")
		(result, response) = wsapi.getblockbyhash(Conf.BLOCK_HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_044_getblockbyhash(self):
		logger.open("test_044_getblockbyhash.log","test_044_getblockbyhash")
		(result, response) = wsapi.getblockbyhash(Conf.BLOCK_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_045_getblockbyhash(self):
		logger.open("test_045_getblockbyhash.log","test_045_getblockbyhash")
		(result, response) = wsapi.getblockbyhash(Conf.BLOCK_HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_046_getblockbyhash(self):
		logger.open("test_046_getblockbyhash.log","test_046_getblockbyhash")
		(result, response) = wsapi.getblockbyhash(Conf.BLOCK_HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_047_getblockheight(self):
		logger.open("test_047_getblockheight.log","test_047_getblockheight")
		(result, response) = wsapi.getblockheight()
		logger.close(result)
	
	def test_048_getblockheight(self):
		logger.open("test_048_getblockheight.log","test_048_getblockheight")
		stop_nodes([0, 1, 2, 3, 4, 5, 6])
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS)
		time.sleep(10)
		(result, response) = wsapi.getblockheight()
		logger.close(result)
	
	def test_049_getblockhashbyheight(self):
		logger.open("test_049_getblockhashbyheight.log","test_049_getblockhashbyheight")
		(result, response) = wsapi.getblockhashbyheight(Conf.HEIGHT_CORRECT)
		logger.close(result)

	def test_051_getblockhashbyheight(self):
		logger.open("test_051_getblockhashbyheight.log","test_051_getblockhashbyheight")
		(result, response) = wsapi.getblockhashbyheight(Conf.HEIGHT_BORDER)
		logger.close(result)

	def test_052_getblockhashbyheight(self):
		logger.open("test_052_getblockhashbyheight.log","test_052_getblockhashbyheight")
		(result, response) = wsapi.getblockhashbyheight(Conf.HEIGHT_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_053_getblockhashbyheight(self):
		logger.open("test_053_getblockhashbyheight.log","test_053_getblockhashbyheight")
		(result, response) = wsapi.getblockhashbyheight(Conf.HEIGHT_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_054_getblockhashbyheight(self):
		logger.open("test_054_getblockhashbyheight.log","test_054_getblockhashbyheight")
		(result, response) = wsapi.getblockhashbyheight(Conf.HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_055_gettransaction(self):
		logger.open("test_055_gettransaction.log","test_055_gettransaction")
		time.sleep(10)
		(result, response) = wsapi.gettransaction(Conf.TX_HASH_CORRECT)
		logger.close(result)

	def test_056_gettransaction(self):
		logger.open("test_056_gettransaction.log","test_056_gettransaction")
		(result, response) = wsapi.gettransaction(Conf.TX_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_057_gettransaction(self):
		logger.open("test_057_gettransaction.log","test_057_gettransaction")
		(result, response) = wsapi.gettransaction(Conf.TX_HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_058_gettransaction(self):
		logger.open("test_058_gettransaction.log","test_058_gettransaction")
		(result, response) = wsapi.gettransaction(Conf.TX_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_059_gettransaction(self):
		logger.open("test_059_gettransaction.log","test_059_gettransaction")
		(result, response) = wsapi.gettransaction(Conf.TX_HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_060_gettransaction(self):
		logger.open("test_060_gettransaction.log","test_060_gettransaction")
		(result, response) = wsapi.gettransaction(Conf.TX_HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_061_sendrawtransaction(self):
		logger.open("test_061_sendrawtransaction.log","test_061_sendrawtransaction")
		(result, response) = wsapi.sendrawtransaction(Conf.RAW_TRANSACTION_DATA_CORRECT)
		logger.close(result)

	def test_063_sendrawtransaction(self):
		logger.open("test_063_sendrawtransaction.log","test_063_sendrawtransaction")
		(result, response) = wsapi.sendrawtransaction(Conf.RAW_TRANSACTION_DATA_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_064_sendrawtransaction(self):
		logger.open("test_064_sendrawtransaction.log","test_064_sendrawtransaction")
		(result, response) = wsapi.sendrawtransaction(Conf.RAW_TRANSACTION_DATA_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_065_sendrawtransaction(self):
		logger.open("test_065_sendrawtransaction.log","test_065_sendrawtransaction")
		(result, response) = wsapi.sendrawtransaction(Conf.RAW_TRANSACTION_DATA_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_066_get_version(self):
		logger.open("test_066_get_version.log","test_066_get_version")
		task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
		task.set_type("ws")
		param = None
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)
		(result, response) = run_single_task(task)
		logger.close(result)

	def test_068_get_version(self):
		logger.open("test_068_get_version.log","test_068_get_version")
		task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
		task.set_type("ws")
		param = {"height":""}
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)
		(result, response) = run_single_task(task)
		logger.close(result)

	def test_069_get_version(self):
		logger.open("test_069_get_version.log","test_069_get_version")
		task = Task(Config.BASEAPI_PATH + "/ws/getversion.json")
		task.set_type("ws")
		param = {"height":"abc"}
		if param and isinstance(param, dict):
			taskrequest = task.request()
			for key in param:
				taskrequest[key] = param[key]
			task.set_request(taskrequest)
		(result, response) = run_single_task(task)
		logger.close(result)

	def test_070_getbalancebyaddr(self):
		logger.open("test_070_getbalancebyaddr.log","test_070_getbalancebyaddr")
		(result, response) = wsapi.getbalancebyaddr(Conf.ACCOUNT_ADDRESS_CORRECT)
		logger.close(result)

	def test_071_getbalancebyaddr(self):
		logger.open("test_071_getbalancebyaddr.log","test_071_getbalancebyaddr")
		(result, response) = wsapi.getbalancebyaddr(Conf.ACCOUNT_ADDRESS_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_072_getbalancebyaddr(self):
		logger.open("test_072_getbalancebyaddr.log","test_072_getbalancebyaddr")
		(result, response) = wsapi.getbalancebyaddr(Conf.ACCOUNT_ADDRESS_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_073_getbalancebyaddr(self):
		logger.open("test_073_getbalancebyaddr.log","test_073_getbalancebyaddr")
		(result, response) = wsapi.getbalancebyaddr(Conf.ACCOUNT_ADDRESS_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_074_getcontract(self):
		logger.open("test_074_getcontract.log","test_074_getcontract")
		(result, response) = wsapi.getcontract(Conf.ACCOUNT_ADDRESS_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_075_getcontract(self):
		logger.open("test_075_getcontract.log","test_075_getcontract")
		time.sleep(10)
		(result, response) = wsapi.getcontract(Conf.CONTRACT_ADDRESS_CORRECT)
		logger.close(result)

	def test_077_getcontract(self):
		logger.open("test_077_getcontract.log","test_077_getcontract")
		time.sleep(5)
		(result, response) = wsapi.getcontract(Conf.CONTRACT_ADDRESS_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_078_getcontract(self):
		logger.open("test_078_getcontract.log","test_078_getcontract")
		time.sleep(5)
		(result, response) = wsapi.getcontract(Conf.CONTRACT_ADDRESS_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_079_getcontract(self):
		logger.open("test_079_getcontract.log","test_079_getcontract")
		time.sleep(5)
		(result, response) = wsapi.getcontract(Conf.CONTRACT_ADDRESS_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_080_getcontract(self):
		logger.open("test_080_getcontract.log","test_080_getcontract")
		time.sleep(5)
		(result, response) = wsapi.getcontract(Conf.CONTRACT_ADDRESS_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_081_getsmartcodeeventbyheight(self):
		logger.open("test_081_getsmartcodeeventbyheight.log","test_081_getsmartcodeeventbyheight")
		(result, response) = wsapi.getsmartcodeeventbyheight(Conf.HEIGHT_CORRECT)
		logger.close(result)

	def test_082_getsmartcodeeventbyheight(self):
		logger.open("test_082_getsmartcodeeventbyheight.log","test_082_getsmartcodeeventbyheight")
		(result, response) = wsapi.getsmartcodeeventbyheight(Conf.HEIGHT_CORRECT)
		logger.close(result)

	def test_083_getsmartcodeeventbyheight(self):
		logger.open("test_083_getsmartcodeeventbyheight.log","test_083_getsmartcodeeventbyheight")
		(result, response) = wsapi.getsmartcodeeventbyheight(Conf.HEIGHT_BORDER)
		logger.close(result)

	def test_084_getsmartcodeeventbyheight(self):
		logger.open("test_084_getsmartcodeeventbyheight.log","test_084_getsmartcodeeventbyheight")
		(result, response) = wsapi.getsmartcodeeventbyheight(Conf.HEIGHT_INCORRECT_1)
		logger.close(result)

	def test_085_getsmartcodeeventbyheight(self):
		logger.open("test_085_getsmartcodeeventbyheight.log","test_085_getsmartcodeeventbyheight")
		(result, response) = wsapi.getsmartcodeeventbyheight(Conf.HEIGHT_INCORRECT_2)
		logger.close(result)

	def test_086_getsmartcodeeventbyheight(self):
		logger.open("test_086_getsmartcodeeventbyheight.log","test_086_getsmartcodeeventbyheight")
		(result, response) = wsapi.getsmartcodeeventbyheight(Conf.HEIGHT_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_087_getsmartcodeeventbyhash(self):
		logger.open("test_087_getsmartcodeeventbyhash.log","test_087_getsmartcodeeventbyhash")
		time.sleep(10)
		(result, response) = wsapi.getsmartcodeeventbyhash(Conf.TX_HASH_CORRECT)
		logger.close(result)

	def test_088_getsmartcodeeventbyhash(self):
		logger.open("test_088_getsmartcodeeventbyhash.log","test_088_getsmartcodeeventbyhash")
		time.sleep(10)
		(result, response) = wsapi.getsmartcodeeventbyhash(Conf.TX_HASH_INCORRECT_5)
		logger.close(result)

	def test_089_getsmartcodeeventbyhash(self):
		logger.open("test_089_getsmartcodeeventbyhash.log","test_089_getsmartcodeeventbyhash")
		time.sleep(10)
		(result, response) = wsapi.getsmartcodeeventbyhash(Conf.TX_HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_090_getsmartcodeeventbyhash(self):
		logger.open("test_090_getsmartcodeeventbyhash.log","test_090_getsmartcodeeventbyhash")
		time.sleep(10)
		(result, response) = wsapi.getsmartcodeeventbyhash(Conf.TX_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_091_getsmartcodeeventbyhash(self):
		logger.open("test_091_getsmartcodeeventbyhash.log","test_091_getsmartcodeeventbyhash")
		time.sleep(10)
		(result, response) = wsapi.getsmartcodeeventbyhash(Conf.TX_HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_092_getsmartcodeeventbyhash(self):
		logger.open("test_092_getsmartcodeeventbyhash.log","test_092_getsmartcodeeventbyhash")
		time.sleep(10)
		(result, response) = wsapi.getsmartcodeeventbyhash(Conf.TX_HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_093_getblockheightbytxhash(self):
		logger.open("test_093_getblockheightbytxhash.log","test_093_getblockheightbytxhash")
		time.sleep(10)
		(result, response) = wsapi.getblockheightbytxhash(Conf.TX_HASH_CORRECT)
		logger.close(result)

	def test_094_getblockheightbytxhash(self):
		logger.open("test_094_getblockheightbytxhash.log","test_094_getblockheightbytxhash")
		time.sleep(10)
		(result, response) = wsapi.getblockheightbytxhash(Conf.TX_HASH_INCORRECT_5)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_095_getblockheightbytxhash(self):
		logger.open("test_095_getblockheightbytxhash.log","test_095_getblockheightbytxhash")
		time.sleep(10)
		(result, response) = wsapi.getblockheightbytxhash(Conf.TX_HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_096_getblockheightbytxhash(self):
		logger.open("test_096_getblockheightbytxhash.log","test_096_getblockheightbytxhash")
		time.sleep(10)
		(result, response) = wsapi.getblockheightbytxhash(Conf.TX_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")					

	def test_097_getblockheightbytxhash(self):
		logger.open("test_097_getblockheightbytxhash.log","test_097_getblockheightbytxhash")
		time.sleep(10)
		(result, response) = wsapi.getblockheightbytxhash(Conf.TX_HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")		

	def test_098_getblockheightbytxhash(self):
		logger.open("test_098_getblockheightbytxhash.log","test_098_getblockheightbytxhash")
		time.sleep(10)
		(result, response) = wsapi.getblockheightbytxhash(Conf.TX_HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_099_getmerkleproof(self):
		logger.open("test_099_getmerkleproof.log","test_099_getmerkleproof")
		time.sleep(10)
		(result, response) = wsapi.getmerkleproof(Conf.TX_HASH_CORRECT)
		logger.close(result)
	
	def test_100_getmerkleproof(self):
		logger.open("test_100_getmerkleproof.log","test_100_getmerkleproof")
		time.sleep(10)
		(result, response) = wsapi.getmerkleproof(Conf.TX_HASH_INCORRECT_5)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_101_getmerkleproof(self):
		logger.open("test_101_getmerkleproof.log","test_101_getmerkleproof")
		time.sleep(10)
		(result, response) = wsapi.getmerkleproof(Conf.TX_HASH_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_102_getmerkleproof(self):
		logger.open("test_102_getmerkleproof.log","test_102_getmerkleproof")
		time.sleep(10)
		(result, response) = wsapi.getmerkleproof(Conf.TX_HASH_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_103_getmerkleproof(self):
		logger.open("test_103_getmerkleproof.log","test_103_getmerkleproof")
		time.sleep(10)
		(result, response) = wsapi.getmerkleproof(Conf.TX_HASH_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_104_getmerkleproof(self):
		logger.open("test_104_getmerkleproof.log","test_104_getmerkleproof")
		time.sleep(10)
		(result, response) = wsapi.getmerkleproof(Conf.TX_HASH_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_105_getsessioncount(self):
		logger.open("test_105_getsessioncount.log","test_105_getsessioncount")
		(result, response) = wsapi.getsessioncount()
		logger.close(result)

	def test_106_getsessioncount(self):
		logger.open("test_106_getsessioncount.log","test_106_getsessioncount")
		stop_node(0)
		(result, response) = wsapi.getsessioncount()
		start_node(0, Config.DEFAULT_NODE_ARGS)
		time.sleep(5)
		self.abnormal_finish(task_name, log_path, result, "")
	
	'''
	def test_107_getstorage(self):
		log_path = "107_getstorage.log"
		task_name = "107_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_108_getstorage(self):
		log_path = "108_getstorage.log"
		task_name = "108_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_2, KEY_CORRECT)
		logger.close(result)

	def test_109_getstorage(self):
		log_path = "109_getstorage.log"
		task_name = "109_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_3, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_110_getstorage(self):
		log_path = "110_getstorage.log"
		task_name = "110_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_4, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_111_getstorage(self):
		log_path = "111_getstorage.log"
		task_name = "111_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_INCORRECT_1, KEY_CORRECT)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_112_getstorage(self):
		log_path = "112_getstorage.log"
		task_name = "112_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_CORRECT)
		logger.close(result)

	def test_113_getstorage(self):
		log_path = "113_getstorage.log"
		task_name = "113_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_2)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_114_getstorage(self):
		log_path = "114_getstorage.log"
		task_name = "114_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_3)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_115_getstorage(self):
		log_path = "115_getstorage.log"
		task_name = "115_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_4)
		self.abnormal_finish(task_name, log_path, result, "")

	def test_116_getstorage(self):
		log_path = "116_getstorage.log"
		task_name = "116_getstorage"
		logger.open(".log","")
		(result, response) = wsapi.getstorage(CONTRACT_ADDRESS_CORRECT, KEY_INCORRECT_1)
		self.abnormal_finish(task_name, log_path, result, "")
	'''
####################################################
if __name__ == '__main__':
	suite = unittest.main()
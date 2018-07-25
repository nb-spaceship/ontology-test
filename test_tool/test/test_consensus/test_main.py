# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time

sys.path.append('..')
sys.path.append('../..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API

from test_api import test_api
from test_config import test_config

############################################################
############################################################
#正常节点和vbft共识
class test_consensus_1(ParametrizedTestCase):
	def test_init(self):
		API.node().stop_all_nodes()
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(8)
		for index in range(7):
			API.native().regid_with_publickey(index)
		
		API.native().init_ont_ong()
		time.sleep(10)
		
		(test_config.m_contract_addr, test_config.m_contract_txhash) = API.contract().deploy_contract_full(test_config.deploy_neo_1, test_config.name1, test_config.desc, test_config.price)
		(test_config.m_contract_addr2, test_config.m_contract_txhash2) = API.contract().deploy_contract_full(test_config.deploy_neo_2, test_config.name2, test_config.desc2, test_config.price)
		
		#A节点是Admin节点
		(process, response) = API.contract().init_admin(test_config.m_contract_addr, Config.ontID_A)
		(process, response) = API.native().bind_role_function(test_config.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])


	def setUp(self):
		logger.open("test_consensus/" + self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_001_consensus(self):
		process = False
		try:
			(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
			self.ASSERT(process, "transfer error...")
	
			(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
			self.ASSERT(process, "not a valid block...")
		except Exception as e:
			print(e)
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_normal_002_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 02')
			storage_value = ByteToHex(b'Test Value 02')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
		
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...")
			self.ASSERT(response["result"]["Result"] != storage_value, "invoke_function get error...")
		except Exception as e:
			print(e)

	def test_normal_003_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 03')
			storage_value = ByteToHex(b'Test Value 03')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			self.ASSERT(process, "invoke_function put error...")
		
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")
		
		except Exception as e:
			print(e)
		
	def test_normal_004_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 04')
			storage_value = ByteToHex(b'Test Value 04')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
		
			process = API.node().check_node_state([0,1,2,3,4,5,6])
			self.ASSERT(process, "")

		except Exception as e:
			print(e)
	
	def test_normal_005_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 05')
			storage_value = ByteToHex(b'Test Value 05')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
		
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...[1]")
			self.ASSERT(response["result"]["Result"] != storage_value, "invoke_function get error...[2]")
		except Exception as e:
			print(e)
	
	def test_base_006_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			storage_key = ByteToHex(b'Test Key 06')
			storage_value = ByteToHex(b'Test Value 06')
			
			API.node().stop_nodes(stopnodes)
			
			process = False
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...[1]")
			self.ASSERT(response["result"]["Result"] != storage_value, "invoke_function get error...[2]")

			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except Exception as e:
			print(e)
		
	def test_normal_007_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			API.node().stop_nodes(stopnodes)
		
			process = False
			storage_key = ByteToHex(b'Test Key 07')
			storage_value = ByteToHex(b'Test Value 07')

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			self.ASSERT(process, "invoke_function put error...")

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")
			
			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except Exception as e:
			print(e)
		
	def test_normal_008_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			API.node().stop_nodes(stopnodes)
			process = False
			(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
			self.ASSERT(process, "transfer error...")

			(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
			self.ASSERT(process, "not a valid block...")

			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except Exception as e:
			print(e)

	def test_normal_009_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			API.node().stop_nodes(stopnodes)
			process = False
			for i in range(10):
				storage_key = ByteToHex(bytes("Test Key 09-" + str(i), encoding = "utf8"))
				storage_value = ByteToHex(bytes("Test Value 09-" + str(i), encoding = "utf8"))

				logger.print("times: " + str(i))
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function put error...")

				time.sleep(30)
				(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
				self.ASSERT(process, "not a valid block...in " + str(i) + " times")
				time.sleep(10)
				
			API.node().start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except Exception as e:
			print(e)

##TODO
'''
	def test_base_019_consensus(self):
		# log_path = "19_consensus.log"
		# task_name = "19_consensus"
		try:
		# self.start(log_path)
			(process, response) = test_api.transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)
		
		
	def test_normal_020_consensus(self):
		# log_path = "20_consensus.log"
		# task_name = "20_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.transfer_20(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_normal_021_consensus(self):
		# log_path = "21_consensus.log"
		# task_name = "21_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.transfer_21(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_normal_022_consensus(self):
		# log_path = "22_consensus.log"
		# task_name = "22_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.transfer_22(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_C, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_abnormal_023_consensus(self):
		# log_path = "23_consensus.log"
		# task_name = "23_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.transfer_23(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_C, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_normal_024_consensus(self):
		# log_path = "24_consensus.log"
		# task_name = "24_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.transfer_24(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY, test_config.PUBLIC_KEY_2, test_config.PUBLIC_KEY_3, test_config.PUBLIC_KEY_4)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_abnormal_025_consensus(self):
		# log_path = "25_consensus.log"
		# task_name = "25_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.transfer_25(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY_5, test_config.PUBLIC_KEY_2, test_config.PUBLIC_KEY_3, test_config.PUBLIC_KEY_4)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_base_030_consensus(self):
		# log_path = "30_consensus.log"
		# task_name = "30_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = test_api.transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_C, "1000")
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_abnormal_031_consensus(self):
		# log_path = "31_consensus.log"
		# task_name = "31_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.approve_31(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = test_api.approve_31(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = test_api.allowance(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = test_api.allowance(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)

	def test_abnormal_032_consensus(self):
		# log_path = "32_consensus.log"
		# task_name = "32_consensus"
		# self.start(log_path)
		try:
			(process, response) = test_api.approve_32(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_C, test_config.ADDRESS_B, "1000")
			(process, response) = test_api.transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = test_api.transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_C, "1000")
			(process, response) = test_api.allowance_32(test_config.ADDRESS_A, test_config.ADDRESS_A)
			self.ASSERT(process, "")	
		except Exception as e:
			print(e)
'''
		
############################################################
############################################################
#拜占庭节点, 5, 6节点是拜占庭节点
class test_consensus_2(ParametrizedTestCase):
	def test_init(self):
		pass
	
	def setUp(self):
		logger.open( "test_consensus/" + self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())
		
	def init_bft_node(self, bft_index):
		API.node().stop_all_nodes()
		API.node().start_nodes([0,1,2,3,4], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology")
		print("start bft node: " + "ontology-bft_" + str(bft_index))
		API.node().start_nodes([5,6], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology-bft_" + str(bft_index))
		time.sleep(8)
		
		for node_index in range(7):			
			API.native().regid_with_publickey(node_index)
		API.native().init_ont_ong()
		time.sleep(15)
		
		(test_config.m_contract_addr, test_config.m_contract_txhash) = API.contract().deploy_contract_full(test_config.deploy_neo_1, test_config.name1, test_config.desc, test_config.price)
		(test_config.m_contract_addr2, test_config.m_contract_txhash2) = API.contract().deploy_contract_full(test_config.deploy_neo_2, test_config.name1, test_config.desc, test_config.price)
		
		
	def test_normal_010_consensus(self):
		try:
			process = False
			storage_key = ByteToHex(b'Test Key 10')
			storage_value = ByteToHex(b'Test Value 10')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function error...")

				(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
				self.ASSERT(process, "not a valid block...")
				
		except Exception as e:
			print(e)
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_normal_011_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 11')
			storage_value = ByteToHex(b'Test Value 11')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function put error...")
				
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
				self.ASSERT(process, "invoke_function error...[1]")
				self.ASSERT(response["result"]["Result"] == storage_value, "invoke_function error...[2]")

		except Exception as e:
			print(e)

	def test_abnormal_012_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 12')
			storage_value = ByteToHex(b'Test Value 12')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				
				#A节点是Admin节点
				(process, response) = API.contract().init_admin(test_config.m_contract_addr, Config.ontID_A)
				self.ASSERT(process, "init_admin error...")
					
				(process, response) = API.native().bind_role_function(test_config.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
				self.ASSERT(process, "bind_role_function error...")
				
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
				self.ASSERT(process, "invoke_function put error...")
				
				(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
				self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")

		except Exception as e:
			print(e)
		
	def test_normal_013_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 13')
			storage_value = ByteToHex(b'Test Value 13')
			for i in range(1, 4):
				self.init_bft_node(i)
				time.sleep(30)
				for j in range(10):
					(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
					self.ASSERT(process, "invoke_function put error...")
					time.sleep(10)
						
		except Exception as e:
			print(e)
		
		
############################################################
############################################################
#dbft共识
class test_consensus_3(ParametrizedTestCase):
	def test_init(self):
		for node_index in range(len(Config.NODES)):
			stop_nodes([node_index])
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True, config="config-dbft-1.json")
		#start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(8)
		for node_index in range(7):
			API.native().regid_with_publickey(node_index)
		
		API.native().init_ont_ong()
		time.sleep(15)
		
		(test_config.m_contract_addr, test_config.m_contract_txhash) = API.contract().deploy_contract_full(test_config.deploy_neo_1, test_config.name1, test_config.desc, test_config.price)
		(test_config.m_contract_addr2, test_config.m_contract_txhash2) = API.contract().deploy_contract_full(test_config.deploy_neo_2, test_config.name1, test_config.desc, test_config.price)
		
		#A节点是Admin节点
		(process, response) = API.contract().init_admin(test_config.m_contract_addr, Config.ontID_A)
		time.sleep(6)
		(process, response) = API.native().bind_role_function(test_config.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
	
	def setUp(self):
		logger.open( "test_consensus/" +  self._testMethodName+".log",self._testMethodName)
		test_config.AMOUNT = "1001"
	
	def tearDown(self):
		logger.close(self.result())
	
	def test_normal_014_consensus(self):
		process = False
		try:
			(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
			self.ASSERT(process, "transfer error...")
			
			(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
			self.ASSERT(process, "not a valid block...")

		except Exception as e:
			print(e.msg)
		
	
	def test_normal_015_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 15')
			storage_value = ByteToHex(b'Test Value 15')

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")
			
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...")

		except Exception as e:
			print(e.msg)
		
	def test_abnormal_016_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 16')
			storage_value = ByteToHex(b'Test Value 16')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			self.ASSERT(process, "invoke_function put error...")
			
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			self.ASSERT(response["result"]["Result"] == '', "invoke_function get error...")

		except Exception as e:
			print(e)
		
	def test_normal_017_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 17')
			storage_value = ByteToHex(b'Test Value 17')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")

			process = API.node().check_node_state([0,1,2,3,4,5,6])
			self.ASSERT(process, "check_node_state")

		except Exception as e:
			print(e)
		
	def test_normal_018_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 18')
			storage_value = ByteToHex(b'Test Value 18')
			(process, response) = API.contract().invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function put error...")

			(process, response) = API.contract().invoke_function(test_config.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
			self.ASSERT(process, "invoke_function get error...[1]")
			self.ASSERT(response["result"]["Result"] != storage_value, "invoke_function get error...[2]")		
		except Exception as e:
			print(e)


def add_candidate_node(new_node, init_ont = 5000000, init_ong = 1000, init_pos = 10000, from_node = 0):
	#新加入节点, 并申请候选节点
	start_nodes([new_node], clear_chain = True, clear_log = True)
	time.sleep(5)
	API.native().regid_with_publickey(new_node)
	(process, response) = API.native().bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
	if not process:
		return (process, response)
		
	(process, response) = API.native().bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8"))])
	if not process:
		return (process, response)
		
	API.native().transfer_ont(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ont), 0)
	API.native().transfer_ong(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ong), 0)
	
	time.sleep(10)
	
	(process, response) = API.native().register_candidate(Config.NODES[new_node]["pubkey"], Config.NODES[new_node]["address"], str(init_pos), ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8")), "1", new_node)
	if not process:
		return (process, response)	
		
	(process, response) = API.native().approve_candidate(Config.NODES[new_node]["pubkey"])		
	return (process, response)


class test_consensus_4(ParametrizedTestCase):
	
	def setUp(self):
		logger.open( "test_consensus/" +  self._testMethodName+".log",self._testMethodName)
		self.m_checknode = 4
		time.sleep(2)
		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		for i in range(0, 7):
			API.native().regid_with_publickey(i)
		API.native().init_ont_ong()
		
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_033_consensus(self):
		process = False
		try:
			add_candidate_node(7, init_pos = 2000, from_node = 0)
			test_api.getStorageConf("vbftConfig")
			# step 2 wallet A unvote in the second round
			(process, response) = commit_dpos()
			time.sleep(5)
			test_api.getStorageConf("vbftConfig")
			self.ASSERT(process, "")
		except Exception as e:
			print(e)

	def test_normal_034_consensus(self):
		process = False
		try:
			vote_node = 13 #投票节点
			peer_node1 = 7 #被投票节点1
			peer_node2 = 8 #被投票节点2
			peer_node3 = 9 #被投票节点3
				
			API.node().start_nodes([vote_node], Config.DEFAULT_NODE_ARGS, True, True)
			API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "5000000", 0)
			API.native().transfer_ong(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "1000", 0)

			for i in range(7, 14):
				add_candidate_node(i, init_pos = 10000, from_node = 0)

			(process, response) = vote_for_peer(Config.NODES[vote_node]["address"], [Config.NODES[peer_node1]["pubkey"], Config.NODES[peer_node2]["pubkey"], Config.NODES[peer_node3]["pubkey"]], ["15000", "15000", "15000"])
			self.ASSERT(process, "vote error")
			
			getStorageConf("vbftConfig")
			# step 2 wallet A unvote in the second round
			(process, response) = commit_dpos()
			time.sleep(5)
			#if not process:
			#	raise Error("unvote error")

			getStorageConf("vbftConfig")
		except Exception as e:
			print(e)


if __name__ == '__main__':
    unittest.main()

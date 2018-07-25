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
	def test_init(cls):
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
		logger.open( self._testMethodName+".log",self._testMethodName)
		(contract_addr, contract_tx_hash) = API.contract().deploy_contract_full("./tasks/neo.neo")
		
	def tearDown(self):
		logger.close(self.m_result)
		pass
	
	def test_base_001_consensus(self):
		process = False
		try:
			try:
				(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
				if not process:
					raise Error("transfer error...")
			
				(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
				if not process:
					raise Error("not a valid block...")
			
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_normal_002_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 02')
			storage_value = ByteToHex(b'Test Value 02')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				if not process:
					raise Error("invoke_function put error...")
			
				(process, response) = invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
				if not process or response["result"]["Result"] == storage_value:
					raise Error("invoke_function get error...")
			
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass

	def test_normal_003_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 03')
			storage_value = ByteToHex(b'Test Value 03')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
				if not process:
					raise Error("invoke_function put error...")
			
				(process, response) = invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
				if response["result"]["Result"] != '':
					process = False
					raise Error("invoke_function get error...")
			
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
		
	def test_normal_004_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 04')
			storage_value = ByteToHex(b'Test Value 04')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				if not process:
					raise Error("invoke_function put error...")
			
				process = check_node_state([0,1,2,3,4,5,6])
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
	
	def test_normal_005_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 05')
			storage_value = ByteToHex(b'Test Value 05')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				if not process:
					raise Error("invoke_function put error...")
			
				(process, response) = invoke_function(test_config.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
				if not process or response["result"]["Result"] == storage_value:
					raise Error("invoke_function get error...")
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
	
	def test_base_006_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			storage_key = ByteToHex(b'Test Key 06')
			storage_value = ByteToHex(b'Test Value 06')
			
			stop_nodes(stopnodes)
			process = False
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				if not process:
					raise Error("invoke_function put error...")
			
				(process, response) = invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
				if not process or response["result"]["Result"] == storage_value:
					raise Error("invoke_function get error...")
			
			except Exception as e:
				print(e.msg)
				process = False
			
			ASSERT(process, "")
			start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except:
			pass
		
	
	def test_normal_007_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			stop_nodes(stopnodes)
		
			process = False
			storage_key = ByteToHex(b'Test Key 07')
			storage_value = ByteToHex(b'Test Value 07')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
				if not process:
					raise Error("invoke_function put error...")
			
				(process, response) = invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
				if response["result"]["Result"] != '':
					process = False
					raise Error("invoke_function get error...")
			
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
			start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except:
			pass
		
		
	
	def test_normal_008_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			stop_nodes(stopnodes)
			process = False
			try:
				(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
				if not process:
					raise Error("transfer error...")
				
				(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
				if not process:
					raise Error("not a valid block...")
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")	
			start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except:
			pass
		
		
	
	def test_normal_009_consensus(self):
		try:
			stopnodes = test_config.m_stop_2_nodes
			stop_nodes(stopnodes)
			process = False
			try:
				for i in range(10):
					storage_key = ByteToHex(bytes("Test Key 09-" + str(i), encoding = "utf8"))
					storage_value = ByteToHex(bytes("Test Value 09-" + str(i), encoding = "utf8"))

					logger.print("times: " + str(i))
					(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
					if not process:
						raise Error("invoke_function put error...")
					
					time.sleep(30)
					(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
					if not process:
						raise Error("not a valid block...in " + str(i) + " times")
					time.sleep(10)
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")		
			start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
			time.sleep(3)
		except:
			pass
		
		

	
	def test_base_019_consensus(self):
		# log_path = "19_consensus.log"
		# task_name = "19_consensus"
		try:
		# self.start(log_path)
			(process, response) = transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT)
			ASSERT(process, "")	
		except:
			pass
		
		
	def test_normal_020_consensus(self):
		# log_path = "20_consensus.log"
		# task_name = "20_consensus"
		# self.start(log_path)
		try:
			(process, response) = transfer_20(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			ASSERT(process, "")	
		except:
			pass

	def test_normal_021_consensus(self):
		# log_path = "21_consensus.log"
		# task_name = "21_consensus"
		# self.start(log_path)
		try:
			(process, response) = transfer_21(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			ASSERT(process, "")	
		except:
			pass

	def test_normal_022_consensus(self):
		# log_path = "22_consensus.log"
		# task_name = "22_consensus"
		# self.start(log_path)
		try:
			(process, response) = transfer_22(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_C, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			ASSERT(process, "")	
		except:
			pass

	def test_abnormal_023_consensus(self):
		# log_path = "23_consensus.log"
		# task_name = "23_consensus"
		# self.start(log_path)
		try:
			(process, response) = transfer_23(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_C, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY)
			ASSERT(process, "")	
		except:
			pass

	def test_normal_024_consensus(self):
		# log_path = "24_consensus.log"
		# task_name = "24_consensus"
		# self.start(log_path)
		try:
			(process, response) = transfer_24(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY, test_config.PUBLIC_KEY_2, test_config.PUBLIC_KEY_3, test_config.PUBLIC_KEY_4)
			ASSERT(process, "")	
		except:
			pass

	def test_abnormal_025_consensus(self):
		# log_path = "25_consensus.log"
		# task_name = "25_consensus"
		# self.start(log_path)
		try:
			(process, response) = transfer_25(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, test_config.AMOUNT, test_config.PUBLIC_KEY_5, test_config.PUBLIC_KEY_2, test_config.PUBLIC_KEY_3, test_config.PUBLIC_KEY_4)
			ASSERT(process, "")	
		except:
			pass

	def test_base_030_consensus(self):
		# log_path = "30_consensus.log"
		# task_name = "30_consensus"
		# self.start(log_path)
		try:
			(process, response) = transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_C, "1000")
			ASSERT(process, "")	
		except:
			pass

	def test_abnormal_031_consensus(self):
		# log_path = "31_consensus.log"
		# task_name = "31_consensus"
		# self.start(log_path)
		try:
			(process, response) = approve_31(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = approve_31(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = allowance(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = allowance(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			ASSERT(process, "")	
		except:
			pass

	def test_abnormal_032_consensus(self):
		# log_path = "32_consensus.log"
		# task_name = "32_consensus"
		# self.start(log_path)
		try:
			(process, response) = approve_32(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_C, test_config.ADDRESS_B, "1000")
			(process, response) = transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_B, "1000")
			(process, response) = transfer_19(test_config.CONTRACT_ADDRESS, test_config.ADDRESS_A, test_config.ADDRESS_C, "1000")
			(process, response) = allowance_32(test_config.ADDRESS_A, test_config.ADDRESS_A)
			ASSERT(process, "")	
		except:
			pass
		
############################################################
############################################################
#拜占庭节点, 5, 6节点是拜占庭节点
class test_consensus_2(ParametrizedTestCase):
	def test_init(self):
		pass
	
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.m_result)
		pass
		
	def init_bft_node(self, bft_index):
		stop_all_nodes()
		start_nodes([0,1,2,3,4], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology")
		print("start bft node: " + "ontology-bft_" + str(bft_index))
		start_nodes([5,6], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology-bft_" + str(bft_index))
		time.sleep(8)
		
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		init_ont_ong()
		time.sleep(15)
		
		(test_config.m_contract_addr, test_config.m_contract_txhash) = deploy_contract_full(test_config.deploy_neo_1, test_config.name1, test_config.desc, test_config.price)
		(test_config.m_contract_addr2, test_config.m_contract_txhash2) = deploy_contract_full(test_config.deploy_neo_2, test_config.name1, test_config.desc, test_config.price)
		
		
	def test_normal_010_consensus(self):
		try:
			process = False
			storage_key = ByteToHex(b'Test Key 10')
			storage_value = ByteToHex(b'Test Value 10')
			try:
				for i in range(1, 4):
					self.init_bft_node(i)
					time.sleep(30)
					(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
					if not process:
						raise Error("invoke_function error...")
					
					(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
					if not process:
						raise Error("not a valid block...")
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_normal_011_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 11')
			storage_value = ByteToHex(b'Test Value 11')
			try:
				for i in range(1, 4):
					self.init_bft_node(i)
					time.sleep(30)
					(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
					if not process:
						raise Error("invoke_function put error...")
					
					(process, response) = invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
					if not process or response["result"]["Result"] != storage_value:
						raise Error("invoke_function get error...")
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_012_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 12')
			storage_value = ByteToHex(b'Test Value 12')
			try:
				for i in range(1, 4):
					self.init_bft_node(i)
					time.sleep(30)
					
					#A节点是Admin节点
					(process, response) = init_admin(test_config..m_contract_addr, Config.ontID_A)
					if not process:
						raise Error("init_admin error...")
						
					(process, response) = bind_role_function(test_config.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
					if not process:
						raise Error("bind_role_function error...")
					
					(process, response) = invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
					if not process:
						raise Error("invoke_function put error...")
					
					(process, response) = invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
					if response["result"]["Result"] != '':
						process = False
						raise Error("invoke_function get error...")
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
		
	def test_normal_013_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 13')
			storage_value = ByteToHex(b'Test Value 13')
			try:
				for i in range(1, 4):
					self.init_bft_node(i)
					time.sleep(30)
					for j in range(10):
						(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
						if not process:
							raise Error("invoke_function put error...")
						time.sleep(10)
						
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
		
		
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
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		
		init_ont_ong()
		time.sleep(15)
		
		(test_config.m_contract_addr, test_config.m_contract_txhash) = deploy_contract_full(test_config.deploy_neo_1, test_config.name1, test_config.desc, test_config.price)
		(test_config.m_contract_addr2, test_config.m_contract_txhash2) = deploy_contract_full(test_config.deploy_neo_2, test_config.name1, test_config.desc, test_config.price)
		
		#A节点是Admin节点
		(process, response) = init_admin(test_config.m_contract_addr, Config.ontID_A)
		time.sleep(6)
		(process, response) = bind_role_function(test_config.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
	
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		test_config.AMOUNT = "1001"
	
	def tearDown(self):
		logger.close(self.m_result)
		pass
	
	def test_normal_014_consensus(self):
		process = False
		try:
			try:
				(process, response) = test_api.transfer(test_config.m_contract_addr, Config.NODES[test_config.m_current_node]["address"], Config.NODES[1]["address"], test_config.AMOUNT, test_config.m_current_node)
				if not process:
					raise Error("transfer error...")
				
				(process, response) = API.rpc().getblockheightbytxhash(response["txhash"])
				if not process:
					raise Error("not a valid block...")
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
	
	def test_normal_015_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 15')
			storage_value = ByteToHex(b'Test Value 15')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				if not process:
					raise Error("invoke_function put error...")
				
				(process, response) = invoke_function(test_config.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
				if not process or response["result"]["Result"] != storage_value:
					raise Error("invoke_function get error...")
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
		
	def test_abnormal_016_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 16')
			storage_value = ByteToHex(b'Test Value 16')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
				if not process:
					raise Error("invoke_function put error...")
				
				(process, response) = invoke_function(test_config.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
				if response["result"]["Result"] != '':
					process = False
					raise Error("invoke_function get error...")
				
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
		
	def test_normal_017_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 17')
			storage_value = ByteToHex(b'Test Value 17')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				if not process:
					raise Error("invoke_function put error...")
				
				process = check_node_state([0,1,2,3,4,5,6])
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass
		
	def test_normal_018_consensus(self):
		process = False
		try:
			storage_key = ByteToHex(b'Test Key 18')
			storage_value = ByteToHex(b'Test Value 18')
			try:
				(process, response) = invoke_function(test_config.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = test_config.m_current_node)
				if not process:
					raise Error("invoke_function put error...")
				
				(process, response) = invoke_function(test_config.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = test_config.m_current_node)
				if not process or response["result"]["Result"] == storage_value:
					raise Error("invoke_function get error...")
					
			except Exception as e:
				print(e.msg)
				process = False
			ASSERT(process, "")
		except:
			pass


def add_candidate_node(new_node, init_ont = 5000000, init_ong = 1000, init_pos = 10000, from_node = 0):
	#新加入节点, 并申请候选节点
	start_nodes([new_node], clear_chain = True, clear_log = True)
	time.sleep(5)
	regIDWithPublicKey(new_node)
	(process, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
	if not process:
		return (process, response)
		
	(process, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8"))])
	if not process:
		return (process, response)
		
	native_transfer_ont(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ont), 0)
	native_transfer_ong(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ong), 0)
	
	time.sleep(10)
	
	(process, response) = invoke_function_register(Config.NODES[new_node]["pubkey"], Config.NODES[new_node]["address"], str(init_pos), ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8")), "1", new_node)
	if not process:
		return (process, response)	
		
	(process, response) = invoke_function_approve(Config.NODES[new_node]["pubkey"])		
	return (process, response)


class test_consensus_4(ParametrizedTestCase):
	
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		self.m_checknode = 4
		time.sleep(2)
		print("stop all")
		for node_index in range(len(Config.NODES)):
			stop_nodes([node_index])
		print("start all")
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		for i in range(0, 7):
			regIDWithPublicKey(i)
		init_ont_ong()
		
	def tearDown(self):
		logger.close(self.m_result)
	
	def test_base_033_consensus(self):
		process = False
		try:
			try:
				add_candidate_node(7, init_pos = 2000, from_node = 0)
				getStorageConf("vbftConfig")
				# step 2 wallet A unvote in the second round
				(process, response) = invoke_function_consensus(Config.NODES[0]["pubkey"])
				time.sleep(5)
				#if not process:
				#	raise Error("unvote error")

				getStorageConf("vbftConfig")

			except Exception as e:
				print(e.msg)
			ASSERT(process, "")
		except:
			pass

	def test_normal_034_consensus(self):
		process = False
		try:
			vote_node = 13 #投票节点
			peer_node1 = 7 #被投票节点1
			peer_node2 = 8 #被投票节点2
			peer_node3 = 9 #被投票节点3
			try:
				
				start_nodes([vote_node], Config.DEFAULT_NODE_ARGS, True, True)
				native_transfer_ont(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "5000000", 0)
				native_transfer_ong(Config.NODES[0]["address"], Config.NODES[vote_node]["address"], "1000", 0)

				for i in range(7, 14):
					add_candidate_node(i, init_pos = 10000, from_node = 0)

				(process, response) = invoke_function_vote(Config.NODES[vote_node]["address"], [Config.NODES[peer_node1]["pubkey"], Config.NODES[peer_node2]["pubkey"], Config.NODES[peer_node3]["pubkey"]], ["15000", "15000", "15000"])
				if not process:
					raise Error("vote error")
				
				getStorageConf("vbftConfig")
				# step 2 wallet A unvote in the second round
				(process, response) = invoke_function_consensus(Config.NODES[0]["pubkey"])
				time.sleep(5)
				#if not process:
				#	raise Error("unvote error")

				getStorageConf("vbftConfig")

			except Exception as e:
				print(e.msg)
			ASSERT(process, "")
		except:
			pass


if __name__ == '__main__':
    unittest.main()

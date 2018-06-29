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

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.contractapi import *
from test_api import *
from utils.rpcapi import *
from utils.init_ong_ont import *


##19-32 start
CONTRACT_ADDRESS = "92ed1b65d9549ce4a083af0dc83862fcba03d5c3"
ADDRESS_A = "da14e05b077d6147e487a4774455a57873fd07d0"  #"AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN"
ADDRESS_B = "24b453d1388732a9d78228b572e05f7a082b90a9" #"AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X"
ADDRESS_C = "e3462e4422c6317a93604fef74255117ed2b5328"
AMOUNT = "1000"
PUBLIC_KEY = "02b59d88bc4b2f5814b691d32e736bcd7ad018794f041235092f6954e23198cbcf"
PUBLIC_KEY_2 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc"
PUBLIC_KEY_3 = "02f59dbaf056dedfbdc2fedd2cf700a585df1acdd777561d65ba484b5f519287ef"
PUBLIC_KEY_4 = "0354fe669e9df891698ef8c4cbc9e3fbfa503ee93e237e1b38d3e3e4c7869886ee"

#test cases


		
############################################################
############################################################
#正常节点和vbft共识
class TestConsensus_1_9__19_32(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		stop_nodes([0,1,2,3,4,5,6])
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(8)
		init_ont_ong()
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		(cls.m_contract_addr, cls.m_contract_txhash) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		(cls.m_contract_addr2, cls.m_contract_txhash2) = deploy_contract_full("tasks/B.neo", "nameB", "descB", 0)
		
		#A节点是Admin节点
		(result, response) = init_admin(cls.m_contract_addr, Config.ontID_A)
		(result, response) = bind_role_function(cls.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
		cls.m_current_node = 0
		cls.m_storage_key = ByteToHex(b'Test Key')
		cls.m_storage_value = ByteToHex(b'Test Value')
		cls.m_stop_2_nodes = [5,6]
	
	def test_01_consensus(self):
		result = False
		logger.open("01_consensus.log", "01_consensus")
		try:
			(result, response) = transfer(self.m_contract_addr, Config.NODES[0]["address"], Config.NODES[1]["address"], AMOUNT, self.m_current_node)
			if not result:
				raise Error("transfer error...")
			
			(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
			if not result:
				raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_02_consensus(self):
		result = False
		logger.open("02_consensus.log", "02_consensus")
		storage_key = ByteToHex(b'Test Key 02')
		storage_value = ByteToHex(b'Test Value 02')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)

	def test_03_consensus(self):
		result = False
		logger.open("03_consensus.log", "03_consensus")
		storage_key = ByteToHex(b'Test Key 03')
		storage_value = ByteToHex(b'Test Value 03')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			if response["result"] != '':
				result = False
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
	def test_04_consensus(self):
		result = False
		logger.open("04_consensus.log", "04_consensus")
		storage_key = ByteToHex(b'Test Key 04')
		storage_value = ByteToHex(b'Test Value 04')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			result = check_node_state([0,1,2,3,4,5,6])
		except Exception as e:
			print(e.msg)
		logger.close(result)
	
	def test_05_consensus(self):
		result = False
		logger.open("05_consensus.log", "05_consensus")
		storage_key = ByteToHex(b'Test Key 05')
		storage_value = ByteToHex(b'Test Value 05')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
		except Exception as e:
			print(e.msg)
		logger.close(result)
	
	def test_06_consensus(self):
		stopnodes = self.m_stop_2_nodes
		storage_key = ByteToHex(b'Test Key 06')
		storage_value = ByteToHex(b'Test Value 06')
		
		stop_nodes(stopnodes)
		result = False
		logger.open("06_consensus.log", "06_consensus")
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_07_consensus(self):
		stopnodes = self.m_stop_2_nodes
		stop_nodes(stopnodes)
	
		result = False
		logger.open("07_consensus.log", "07_consensus")
		storage_key = ByteToHex(b'Test Key 07')
		storage_value = ByteToHex(b'Test Value 07')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			if response["result"] != '':
				result = False
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_08_consensus(self):
		stopnodes = self.m_stop_2_nodes
		stop_nodes(stopnodes)
		result = False
		logger.open("08_consensus.log", "08_consensus")
		try:
			(result, response) = transfer(self.m_contract_addr, Config.NODES[0]["address"], Config.NODES[1]["address"], AMOUNT, self.m_current_node)
			if not result:
				raise Error("transfer error...")
			
			(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
			if not result:
				raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_09_consensus(self):
		stopnodes = self.m_stop_2_nodes
		
		logger.open("09_consensus.log", "09_consensus")
		stop_nodes(stopnodes)
		result = False
		logger.open("09_consensus.log", "09_consensus")
		try:
			for i in range(10):
				storage_key = ByteToHex(bytes("Test Key 09-" + str(i), encoding = "utf8"))
				storage_value = ByteToHex(bytes("Test Value 09-" + str(i), encoding = "utf8"))

				logger.print("times: " + str(i))
				(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
				if not result:
					raise Error("invoke_function put error...")
				
				(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
				if not result:
					raise Error("not a valid block...in " + str(i) + " times")
				time.sleep(10)
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
		start_nodes(stopnodes, Config.DEFAULT_NODE_ARGS)
		time.sleep(3)
	
	def test_19_consensus(self):
		log_path = "19_consensus.log"
		task_name = "19_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT)
		logger.close(result)

	def test_20_consensus(self):
		log_path = "20_consensus.log"
		task_name = "20_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_20(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY)
		logger.close(result)

	def test_21_consensus(self):
		log_path = "21_consensus.log"
		task_name = "21_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_21(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY)
		logger.close(result)

	def test_22_consensus(self):
		log_path = "22_consensus.log"
		task_name = "22_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_22(CONTRACT_ADDRESS, ADDRESS_C, ADDRESS_B, AMOUNT, PUBLIC_KEY)
		logger.close(result)

	def test_23_consensus(self):
		log_path = "23_consensus.log"
		task_name = "23_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_23(CONTRACT_ADDRESS, ADDRESS_C, ADDRESS_B, AMOUNT, PUBLIC_KEY)
		logger.close(result)

	def test_24_consensus(self):
		log_path = "24_consensus.log"
		task_name = "24_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_24(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY, PUBLIC_KEY_2, PUBLIC_KEY_3, PUBLIC_KEY_4)
		logger.close(result)

	def test_25_consensus(self):
		log_path = "25_consensus.log"
		task_name = "25_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_25(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY, PUBLIC_KEY_2, PUBLIC_KEY_3, PUBLIC_KEY_4)
		logger.close(result)

	def test_30_consensus(self):
		log_path = "30_consensus.log"
		task_name = "30_consensus"
		logger.open(log_path, task_name)
		(result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT)
		(result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_C, AMOUNT)
		logger.close(result)

	def test_31_consensus(self):
		log_path = "31_consensus.log"
		task_name = "31_consensus"
		logger.open(log_path, task_name)
		(result, response) = approve_31(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", AMOUNT)
		(result, response) = approve_31(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AcVb7HZB4nMDscQHXXoqKvnNFwrpL3V1u3", AMOUNT)
		(result, response) = allowance(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", AMOUNT)
		(result, response) = allowance(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AcVb7HZB4nMDscQHXXoqKvnNFwrpL3V1u3", AMOUNT)
		logger.close(result)

	def test_32_consensus(self):
		log_path = "32_consensus.log"
		task_name = "32_consensus"
		logger.open(log_path, task_name)
		(result, response) = approve_32(CONTRACT_ADDRESS, "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", AMOUNT)
		(result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT)
		(result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_C, AMOUNT)
		(result, response) = allowance_32("AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN")
		logger.close(result)

		
############################################################
############################################################
#拜占庭节点, 5, 6节点是拜占庭节点
class TestConsensus_10_13(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		pass
		
	def init_bft_node(self, bft_index):
		stop_nodes([0,1,2,3,4,5,6])
		start_nodes([0,1,2,3,4], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology")
		start_nodes([5,6], Config.DEFAULT_NODE_ARGS, True, True, program = "ontology-bft_" + str(bft_index))
		time.sleep(8)
		init_ont_ong()
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		#regIDWithPublicKey(5)
		#regIDWithPublicKey(6)
		
		(self.m_contract_addr, self.m_contract_txhash) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		(self.m_contract_addr2, self.m_contract_txhash2) = deploy_contract_full("tasks/B.neo", "name", "desc", 0)
		
		#A节点是Admin节点
		(result, response) = init_admin(self.m_contract_addr, Config.ontID_A)
		(result, response) = bind_role_function(self.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
		self.m_current_node = 0
		self.m_storage_key = ByteToHex(b'Test Key')
		self.m_storage_value = ByteToHex(b'Test Value')
		self.m_stop_2_nodes = [5,6]
		
	def test_10_consensus(self):
		result = False
		logger.open("10_consensus.log", "10_consensus")
		try:
			for i in range(3):
				self.init_bft_node(i)
				(result, response) = transfer(self.m_contract_addr, Config.NODES[0]["address"], Config.NODES[1]["address"], AMOUNT, self.m_current_node)
				if not result:
					raise Error("transfer error...")
				
				(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
				if not result:
					raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
	
	#contract_address, function_str, callerOntID, public_key="1", argvs = [{"type": "string","value": ""}], node_index = None
	def test_11_consensus(self):
		result = False
		logger.open("11_consensus.log", "11_consensus")
		storage_key = ByteToHex(b'Test Key 11')
		storage_value = ByteToHex(b'Test Value 11')
		try:
			for i in range(3):
				self.init_bft_node(i)
				(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
				if not result:
					raise Error("invoke_function put error...")
				
				(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
				if not result or response["result"]["Result"] == storage_value:
					raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)

	def test_12_consensus(self):
		result = False
		logger.open("12_consensus.log", "12_consensus")
		storage_key = ByteToHex(b'Test Key 12')
		storage_value = ByteToHex(b'Test Value 12')
		try:
			for i in range(3):
				self.init_bft_node(i)
				(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
				if not result:
					raise Error("invoke_function put error...")
				
				(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
				if response["result"] != '':
					result = False
					raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
	def test_13_consensus(self):
		result = False
		logger.open("13_consensus.log", "13_consensus")
		storage_key = ByteToHex(b'Test Key 13')
		storage_value = ByteToHex(b'Test Value 13')
		try:
			for i in range(3):
				self.init_bft_node(i)
				(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
				if not result:
					raise Error("invoke_function put error...")
			
			result = check_node_state([0,1,2,3,4,5,6])
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
		
############################################################
############################################################
#dbft共识
class TestConsensus_14_18(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		stop_nodes([0,1,2,3,4,5,6])
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True, config="config-dbft.json")
		time.sleep(8)
		init_ont_ong()
		regIDWithPublicKey(0)
		regIDWithPublicKey(1)
		regIDWithPublicKey(2)
		regIDWithPublicKey(3)
		regIDWithPublicKey(4)
		regIDWithPublicKey(5)
		regIDWithPublicKey(6)
		
		(cls.m_contract_addr, cls.m_contract_txhash) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		(cls.m_contract_addr2, cls.m_contract_txhash2) = deploy_contract_full("tasks/B.neo", "name", "desc", 0)
		
		#A节点是Admin节点
		(result, response) = init_admin(cls.m_contract_addr, Config.ontID_A)
		(result, response) = bind_role_function(cls.m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
		cls.m_current_node = 0
		cls.m_storage_key = ByteToHex(b'Test Key')
		cls.m_storage_value = ByteToHex(b'Test Value')
		cls.m_stop_2_nodes = [5,6]
		
	def test_14_consensus(self):
		result = False
		logger.open("14_consensus.log", "14_consensus")
		try:
			(result, response) = transfer(self.m_contract_addr, Config.NODES[0]["address"], Config.NODES[1]["address"], AMOUNT, self.m_current_node)
			if not result:
				raise Error("transfer error...")
			
			(result, response) = RPCApi().getblockheightbytxhash(response["txhash"])
			if not result:
				raise Error("not a valid block...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
	
	def test_15_consensus(self):
		result = False
		logger.open("15_consensus.log", "15_consensus")
		storage_key = ByteToHex(b'Test Key 15')
		storage_value = ByteToHex(b'Test Value 15')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
	def test_16_consensus(self):
		result = False
		logger.open("16_consensus.log", "16_consensus")
		storage_key = ByteToHex(b'Test Key 16')
		storage_value = ByteToHex(b'Test Value 16')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "auth_put", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}])
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr, "get", Config.ontID_B, "1", argvs = [{"type": "bytearray","value": storage_key}])
			if response["result"] != '':
				result = False
				raise Error("invoke_function get error...")
			
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
	def test_17_consensus(self):
		result = False
		logger.open("17_consensus.log", "17_consensus")
		storage_key = ByteToHex(b'Test Key 17')
		storage_value = ByteToHex(b'Test Value 17')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			result = check_node_state([0,1,2,3,4,5,6])
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
	def test_18_consensus(self):
		result = False
		logger.open("18_consensus.log", "18_consensus")
		storage_key = ByteToHex(b'Test Key 18')
		storage_value = ByteToHex(b'Test Value 18')
		try:
			(result, response) = invoke_function(self.m_contract_addr, "put", "", "1", argvs = [{"type": "bytearray","value": storage_key},{"type": "bytearray","value": storage_value}], node_index = self.m_current_node)
			if not result:
				raise Error("invoke_function put error...")
			
			(result, response) = invoke_function(self.m_contract_addr2, "get", "", "1", argvs = [{"type": "bytearray","value": storage_key}], node_index = self.m_current_node)
			if not result or response["result"]["Result"] == storage_value:
				raise Error("invoke_function get error...")
		except Exception as e:
			print(e.msg)
		logger.close(result)  


if __name__ == '__main__':
    unittest.main()

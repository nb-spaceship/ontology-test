# -*- coding:utf-8 -*-

import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time
import requests
import subprocess

sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API

####################################################
logger = LoggerInstance
rpcApi = API.rpc()
####################################################


######################################################
# test cases
class test_rpc_1(ParametrizedTestCase):
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		API.node().stop_all_nodes()
		API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(5)
		
	def tearDown(self):
		logger.close(self.m_result)
		pass
		
	# can not test
	def test_normal_021_getbestblockhash(self):
		try:
			(process, response) = rpcApi.getbestblockhash()
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
		
	# can not test
	def test_normal_023_getblockcount(self):
		try:
			(process, response) = rpcApi.getblockcount()
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
class test_rpc_2(ParametrizedTestCase):
	def test_init(self):
		API.node().stop_all_nodes()
		API.node().start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(30)
		
		(self.m_contractaddr_right, self.m_txhash_right) = API.contract().deploy_contract_full("/home/ubuntu/ontology/git/test/test_tool/test/test_web_api/tasks/A.neo", "name", "desc", 0)
		self.m_txhash_wrong = "is a wrong tx hash"
		
		(result, reponse) = rpcApi.getblockhash(height = 1)
		self.m_block_hash_right = reponse["result"]
		
		self.m_block_hash_error = "this is a wrong block hash"
		print("=============", self.m_block_hash_error)
		
		self.m_block_height_right = 1
		
		self.m_block_height_wrong = 9999
		
		self.m_block_height_overflow = 99999999
		
		(result, reponse) = API.contract().sign_transction(Task("/home/ubuntu/ontology/git/test/test_tool/test/test_web_api/tasks/cli/siginvoketx.json"), False)
		self.m_signed_txhash_right = reponse["result"]["signed_tx"]
		self.m_signed_txhash_wrong = self.m_signed_txhash_right + "0f0f0f0f"
		
		
		self.m_getstorage_contract_addr = self.m_contractaddr_right
		self.m_getstorage_contract_addr_wrong = self.m_contractaddr_right + "0f0f0f0f"
		self.m_getstorage_contract_key = ByteToHex(b'key1')
		self.m_getstorage_contract_value = ByteToHex(b'value1')
		API.contract().invoke_function(self.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": self.m_getstorage_contract_key},{"type": "bytearray","value": self.m_getstorage_contract_value}], node_index = 0)
		
		self.getsmartcodeevent_height = 5

		self.getbalance_address_true = Config.NODES[0]["address"]
		self.getbalance_address_false = "ccccccccccccccc"
		
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		time.sleep(1)
		
	def tearDown(self):
		logger.close(self.m_result)
		pass
			
	def test_base_001_getblock(self):
		print("-=-=-=-=-=-=-=", self.m_block_hash_right)
		try:
			(process, response) = rpcApi.getblock(height = None, blockhash = self.m_block_hash_right, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_002_getblock(self):
		print("-=-=-=-=-=-=-=", self.m_block_hash_error)
		try:
			(process, response) = rpcApi.getblock(height = None, blockhash = self.m_block_hash_error, verbose = None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_003_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_004_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = 0, blockhash = None, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
		
	def test_abnormal_005_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_wrong, blockhash = None, verbose = None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_006_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_overflow, blockhash = None, verbose = None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_normal_007_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_008_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_009_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = -1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_010_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_011_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_012_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = None)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_013_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = self.m_block_height_right)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_014_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = 0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_015_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = self.m_block_height_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_016_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = self.m_block_height_overflow)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_017_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_018_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = -1)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_019_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_base_020_getbestblockhash(self):
		try:
			(process, response) = rpcApi.getbestblockhash()
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_022_getblockcount(self):
		try:
			(process, response) = rpcApi.getblockcount()
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_024_getconnectioncount(self):
		try:
			(process, response) = rpcApi.getconnectioncount()
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	# can not test
	def test_normal_025_getconnectioncount(self):
		try:
			stop_nodes([1, 2, 3, 4, 5, 6])
		
			(process, response) = rpcApi.getconnectioncount()
		
			start_nodes([1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, False, False)
			time.sleep(10)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
			
	def test_abnormal_026_getgenerateblocktime(self):
		try:
			(process, response) = rpcApi.getgenerateblocktime()
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	
	def test_base_027_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_028_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_029_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_030_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(1)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_031_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_032_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_right, 1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_033_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_right, 0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_034_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_right, -1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_035_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_right, 2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_036_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_right, "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_normal_037_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(self.m_txhash_right, None)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_038_sendrawtransaction(self):
		try:
			(process, response) = rpcApi.sendrawtransaction(self.m_signed_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_039_sendrawtransaction(self):
		try:
			(process, response) = rpcApi.sendrawtransaction("")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_040_sendrawtransaction(self):
		try:
			(process, response) = rpcApi.sendrawtransaction(None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_041_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, self.m_getstorage_contract_key)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_042_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(self.m_getstorage_contract_addr_wrong, self.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_043_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage("abc", self.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_044_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(1, self.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_045_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(None, self.m_getstorage_contract_key)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_normal_046_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, self.m_getstorage_contract_key)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_047_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, "getstorage_key_error")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_048_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_049_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, 123)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_050_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	

	def test_base_051_getversion(self):
		try:
			(process, response) = rpcApi.getversion()
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_058_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_contractaddr_right)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_059_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_060_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_061_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(123)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_062_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(None, 1)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_normal_063_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_064_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_contractaddr_right, -1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_065_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_066_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_contractaddr_right, "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_normal_067_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_068_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(self.m_contractaddr_right, None)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_069_getmempooltxstate(self):
		try:
			(process, response) = invoke_function(self.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": self.m_getstorage_contract_key},{"type": "bytearray","value": self.m_getstorage_contract_value}], node_index = 0, sleep = 0)

			(process, response) = rpcApi.getmempooltxstate(response["txhash"])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_070_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate(self.m_txhash_right)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_071_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_072_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate(123)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_073_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate(None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_074_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height = self.getsmartcodeevent_height)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_075_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height = 99999999)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_076_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height="abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_077_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height =None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_078_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(tx_hash = self.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_079_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(tx_hash = self.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_080_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = self.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_081_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = self.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_082_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = "abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_083_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = 123)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_084_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_base_085_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance(self.getbalance_address_true)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_086_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance(self.getbalance_address_false)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_087_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_088_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance(None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_089_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof(self.m_txhash_right)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_090_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof(self.m_txhash_wrong)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_091_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof("abc")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_092_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof("123")
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_093_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof(None)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

	def test_normal_094_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/94_getmerkleproof.json")
			task.request()["params"] = [self.m_txhash_right]
			(process, response) =  run_single_task(task)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_095_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/95_getmerkleproof.json")
			task.request()["params"] = [self.m_txhash_right]
			(process, response) =  run_single_task(task)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	# can not test
	def test_abnormal_096_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/96_getmerkleproof.json")
			(process, response) =  run_single_task(task)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_097_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/97_getmerkleproof.1.json")
			(process, response) =  run_single_task(task)
			self.ASSERT(not process, "")
		except Exception as e:
			print(e.args)

if __name__ == '__main__':
    unittest.main()
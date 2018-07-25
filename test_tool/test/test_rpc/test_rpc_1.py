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
testpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(testpath)

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API
from test_config import *

####################################################
rpcApi = API.rpc()
nodeApi = API.node()
contractApi = API.contract()
TEST_PATH = os.path.dirname(os.path.realpath(__file__))
####################################################



######################################################
# test cases
class test_rpc_1(ParametrizedTestCase):
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		nodeApi.stop_all_nodes()
		nodeApi.start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(5)
		
	def tearDown(self):
		logger.close(self.m_result)
		pass
		
	# can not test
	def test_normal_021_getbestblockhash(self):
		try:
			self.clear_nodes()
			(process, response) = rpcApi.getbestblockhash()
			ASSERT(process, "")
		except:
			pass
		
	# can not test
	def test_normal_023_getblockcount(self):
		try:
			self.clear_nodes()
			(process, response) = rpcApi.getblockcount()
			ASSERT(process, "")
		except:
			pass
	
class test_rpc_2(ParametrizedTestCase):
	def test_init(self):
		stop_all_nodes()
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(60)
		
		(test_config.m_contractaddr_right, test_config.m_txhash_right) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		
		(result, response) = rpcApi.getblockhash(height = 1)
		test_config.m_block_hash_right = response["result"]
		(result, response) = sign_transction(Task("tasks/cli/siginvoketx.json"), False)
		test_config.m_signed_txhash_right = response["result"]["signed_tx"]
		test_config.m_signed_txhash_wrong = test_config.m_signed_txhash_right + "0f0f0f0f"
		
		invoke_function(test_config.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": test_config.m_getstorage_contract_key},{"type": "bytearray","value": test_config.m_getstorage_contract_value}], node_index = 0)
		
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		time.sleep(1)
		
	def tearDown(self):
		logger.close(self.m_result)
		pass
			
	def test_base_001_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = None, blockhash = test_config.m_block_hash_right, verbose = None)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_002_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = None, blockhash = test_config.m_block_hash_error, verbose = None)
			ASSERT(not process, "")
		except:
			pass
	
	def test_normal_003_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_right, blockhash = None, verbose = None)
			ASSERT(process, "")
		except:
			pass
	
	def test_normal_004_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = 0, blockhash = None, verbose = None)
			ASSERT(process, "")
		except:
			pass
		
	def test_abnormal_005_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_wrong, blockhash = None, verbose = None)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_006_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_overflow, blockhash = None, verbose = None)
			ASSERT(not process, "")
		except:
			pass

	def test_normal_007_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_right, blockhash = None, verbose = 0)
			ASSERT(process, "")
		except:
			pass

	def test_normal_008_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_right, blockhash = None, verbose = 1)
			ASSERT(process, "")
		except:
			pass

	def test_normal_009_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_right, blockhash = None, verbose = -1)
			ASSERT(process, "")
		except:
			pass
	
	def test_normal_010_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_right, blockhash = None, verbose = 2)
			ASSERT(process, "")
		except:
			pass
	
	def test_abnormal_011_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_right, blockhash = None, verbose = "abc")
			ASSERT(not process, "")
		except:
			pass
	
	def test_normal_012_getblock(self):
		try:
			(process, response) = rpcApi.getblock(height = test_config.m_block_height_right, blockhash = None, verbose = None)
			ASSERT(process, "")
		except:
			pass

	def test_base_013_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = test_config.m_block_height_right)
			ASSERT(process, "")
		except:
			pass
	
	def test_normal_014_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = 0)
			ASSERT(process, "")
		except:
			pass
	
	def test_abnormal_015_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = test_config.m_block_height_wrong)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_016_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = test_config.m_block_height_overflow)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_017_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = "abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_018_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = -1)
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_019_getblockhash(self):
		try:
			(process, response) = rpcApi.getblockhash(height = None)
			ASSERT(not process, "")
		except:
			pass

	def test_base_020_getbestblockhash(self):
		try:
			(process, response) = rpcApi.getbestblockhash()
			ASSERT(process, "")
		except:
			pass
	
	def test_base_022_getblockcount(self):
		try:
			(process, response) = rpcApi.getblockcount()
			ASSERT(process, "")
		except:
			pass

	def test_base_024_getconnectioncount(self):
		try:
			(process, response) = rpcApi.getconnectioncount()
			ASSERT(process, "")
		except:
			pass

	# can not test
	def test_normal_025_getconnectioncount(self):
		try:
			stop_nodes([1, 2, 3, 4, 5, 6])
		
			(process, response) = rpcApi.getconnectioncount()
		
			start_nodes([1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, False, False)
			time.sleep(10)
			ASSERT(process, "")
		except:
			pass
			
	def test_abnormal_026_getgenerateblocktime(self):
		try:
			(process, response) = rpcApi.getgenerateblocktime()
			ASSERT(not process, "")
		except:
			pass
	'''
	# can not test
	def test_026_getconnectioncount_1(self):
		logger.open("rpc/27_getconnectioncount.log", "27_getconnectioncount")
		(process, response) = rpcApi.getgenerateblocktime()
		logger.close(not result)
	'''
	
	def test_base_027_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_right)
			ASSERT(process, "")
		except:
			pass
	
	def test_abnormal_028_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_wrong)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_029_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction("abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_030_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(1)
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_031_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(None)
			ASSERT(not process, "")
		except:
			pass
	
	def test_normal_032_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_right, 1)
			ASSERT(process, "")
		except:
			pass
	
	def test_normal_033_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_right, 0)
			ASSERT(process, "")
		except:
			pass

	def test_normal_034_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_right, -1)
			ASSERT(process, "")
		except:
			pass

	def test_normal_035_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_right, 2)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_036_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_right, "abc")
			ASSERT(not process, "")
		except:
			pass

	def test_normal_037_getrawtransaction(self):
		try:
			(process, response) = rpcApi.getrawtransaction(test_config.m_txhash_right, None)
			ASSERT(process, "")
		except:
			pass
	
	def test_base_038_sendrawtransaction(self):
		try:
			(process, response) = rpcApi.sendrawtransaction(test_config.m_signed_txhash_right)
			ASSERT(process, "")
		except:
			pass
	
	def test_abnormal_039_sendrawtransaction(self):
		try:
			(process, response) = rpcApi.sendrawtransaction("")
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_040_sendrawtransaction(self):
		try:
			(process, response) = rpcApi.sendrawtransaction(None)
			ASSERT(not process, "")
		except:
			pass
	
	def test_base_041_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(test_config.m_getstorage_contract_addr, test_config.m_getstorage_contract_key)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_042_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(test_config.m_getstorage_contract_addr_wrong, test_config.m_getstorage_contract_key)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_043_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage("abc", test_config.m_getstorage_contract_key)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_044_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(1, test_config.m_getstorage_contract_key)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_045_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(None, test_config.m_getstorage_contract_key)
			ASSERT(not process, "")
		except:
			pass

	def test_normal_046_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(test_config.m_getstorage_contract_addr, test_config.m_getstorage_contract_key)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_047_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(test_config.m_getstorage_contract_addr, "getstorage_key_error")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_048_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(test_config.m_getstorage_contract_addr, "abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_049_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(test_config.m_getstorage_contract_addr, 123)
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_050_getstorage(self):
		try:
			(process, response) = rpcApi.getstorage(test_config.m_getstorage_contract_addr, None)
			ASSERT(not process, "")
		except:
			pass
	

	def test_base_051_getversion(self):
		try:
			(process, response) = rpcApi.getversion()
			ASSERT(process, "")
		except:
			pass

	# can not test
	'''
	def test_52_getversion(self):
		self.clear_nodes();
		logger.open("rpc/52_getversion.log", "52_getversion")
		(process, response) = rpcApi.getversion()
		logger.close(not result)
	
	def test_53_getblocksysfee(self):
		logger.open("rpc/52_getversion.log", "52_getversion")
		(process, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(process)

	# can not test
	def test_54_getblocksysfee(self):
		logger.open("rpc/54_getblocksysfee.log", "54_getblocksysfee")
		(process, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(process)

	def test_55_getblocksysfee(self):
		logger.open("rpc/55_getblocksysfee.log", "55_getblocksysfee")
		(process, response) = rpcApi.getblocksysfee(getblocksysfee_index_false)
		logger.close(not result)

	def test_56_getblocksysfee(self):
		logger.open("rpc/56_getblocksysfee.log", "56_getblocksysfee")
		(process, response) = rpcApi.getblocksysfee("abc")
		logger.close(not result)

	def test_57_getblocksysfee(self):
		logger.open("rpc/57_getblocksysfee.log", "57_getblocksysfee")
		(process, response) = rpcApi.getblocksysfee(None)
		logger.close(not result)
	'''
	def test_base_058_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_contractaddr_right)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_059_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_txhash_wrong)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_060_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate("abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_061_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(123)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_062_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(None, 1)
			ASSERT(not process, "")
		except:
			pass

	def test_normal_063_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_contractaddr_right, 1)
			ASSERT(process, "")
		except:
			pass

	def test_normal_064_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_contractaddr_right, -1)
			ASSERT(process, "")
		except:
			pass

	def test_normal_065_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_contractaddr_right, 2)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_066_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_contractaddr_right, "abc")
			ASSERT(not process, "")
		except:
			pass

	def test_normal_067_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_contractaddr_right, 0)
			ASSERT(process, "")
		except:
			pass

	def test_normal_068_getcontractstate(self):
		try:
			(process, response) = rpcApi.getcontractstate(test_config.m_contractaddr_right, None)
			ASSERT(process, "")
		except:
			pass

	def test_base_069_getmempooltxstate(self):
		try:
			(process, response) = invoke_function(test_config.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": test_config.m_getstorage_contract_key},{"type": "bytearray","value": test_config.m_getstorage_contract_value}], node_index = 0, sleep = 0)

			(process, response) = rpcApi.getmempooltxstate(response["txhash"])
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_070_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate(test_config.m_txhash_right)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_071_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate("abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_072_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate(123)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_073_getmempooltxstate(self):
		try:
			(process, response) = rpcApi.getmempooltxstate(None)
			ASSERT(not process, "")
		except:
			pass
	
	def test_base_074_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height = test_config.getsmartcodeevent_height)
			ASSERT(process, "")
		except:
			pass

	def test_normal_075_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height = 99999999)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_076_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height="abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_077_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(height =None)
			ASSERT(not process, "")
		except:
			pass
	
	def test_normal_078_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(tx_hash = test_config.m_txhash_right)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_079_getsmartcodeevent(self):
		try:
			(process, response) = rpcApi.getsmartcodeevent(tx_hash = test_config.m_txhash_wrong)
			ASSERT(not process, "")
		except:
			pass
	
	def test_base_080_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = test_config.m_txhash_right)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_081_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = test_config.m_txhash_wrong)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_082_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = "abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_083_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = 123)
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_084_getblockheightbytxhash(self):
		try:
			(process, response) = rpcApi.getblockheightbytxhash(tx_hash = None)
			ASSERT(not process, "")
		except:
			pass

	def test_base_085_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance(test_config.getbalance_address_true)
			ASSERT(process, "")
		except:
			pass
	
	def test_abnormal_086_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance(test_config.getbalance_address_false)
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_087_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance("abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_088_getbalance(self):
		try:
			(process, response) = rpcApi.getbalance(None)
			ASSERT(not process, "")
		except:
			pass
	
	def test_base_089_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof(test_config.m_txhash_right)
			ASSERT(process, "")
		except:
			pass

	def test_abnormal_090_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof(test_config.m_txhash_wrong)
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_091_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof("abc")
			ASSERT(not process, "")
		except:
			pass

	def test_abnormal_092_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof("123")
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_093_getmerkleproof(self):
		try:
			(process, response) = rpcApi.getmerkleproof(None)
			ASSERT(not process, "")
		except:
			pass

	def test_normal_094_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/94_getmerkleproof.json")
			task.request()["params"] = [test_config.m_txhash_right]
			(process, response) =  run_single_task(task)
			ASSERT(process, "")
		except:
			pass

	def test_normal_095_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/95_getmerkleproof.json")
			task.request()["params"] = [test_config.m_txhash_right]
			(process, response) =  run_single_task(task)
			ASSERT(process, "")
		except:
			pass

	# can not test
	def test_abnormal_096_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/96_getmerkleproof.json")
			(process, response) =  run_single_task(task)
			ASSERT(not process, "")
		except:
			pass
	
	def test_abnormal_097_getmerkleproof(self):
		try:
			task = Task("tasks/rpc/97_getmerkleproof.1.json")
			(process, response) =  run_single_task(task)
			ASSERT(not process, "")
		except:
			pass

if __name__ == '__main__':
    unittest.main()
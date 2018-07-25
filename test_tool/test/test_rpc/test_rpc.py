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

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.api.rpcapi import RPCApi
from utils.api.commonapi import *
from utils.api.contractapi import invoke_function

####################################################
logger = LoggerInstance
rpcApi = RPCApi()
####################################################



######################################################
# test cases
class Test_no_block(ParametrizedTestCase):
	def setUp(self):
		stop_all_nodes()
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(5)
		
	# can not test
	def test_021_getbestblockhash(self):
		self.clear_nodes()
		logger.open("rpc/test_021_getbestblockhash.log", "test_021_getbestblockhash")
		(result, response) = rpcApi.getbestblockhash()
		logger.close(result)
		
	# can not test
	def test_023_getblockcount(self):
		self.clear_nodes()
		logger.open("rpc/test_023_getblockcount.log", "test_023_getblockcount")
		(result, response) = rpcApi.getblockcount()
		logger.close(result and int(response["result"]) == 1)
	
class TestRpc(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		stop_all_nodes()
		start_nodes([0, 1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(60)
		
		(cls.m_contractaddr_right, cls.m_txhash_right) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		cls.m_txhash_wrong = "is a wrong tx hash"
		
		(result, reponse) = rpcApi.getblockhash(height = 1)
		cls.m_block_hash_right = reponse["result"]
		
		cls.m_block_hash_error = "this is a wrong block hash"
		
		cls.m_block_height_right = 1
		
		cls.m_block_height_wrong = 9999
		
		cls.m_block_height_overflow = 99999999
		
		(result, reponse) = sign_transction(Task("tasks/cli/siginvoketx.json"), False)
		cls.m_signed_txhash_right = reponse["result"]["signed_tx"]
		cls.m_signed_txhash_wrong = cls.m_signed_txhash_right + "0f0f0f0f"
		
		
		cls.m_getstorage_contract_addr = cls.m_contractaddr_right
		cls.m_getstorage_contract_addr_wrong = cls.m_contractaddr_right + "0f0f0f0f"
		cls.m_getstorage_contract_key = ByteToHex(b'key1')
		cls.m_getstorage_contract_value = ByteToHex(b'value1')
		invoke_function(cls.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": cls.m_getstorage_contract_key},{"type": "bytearray","value": cls.m_getstorage_contract_value}], node_index = 0)
		
		cls.getsmartcodeevent_height = 5

		cls.getbalance_address_true = Config.NODES[0]["address"]
		cls.getbalance_address_false = "ccccccccccccccc"
		
	def setUp(self):
		time.sleep(1)
			
	def test_001_getblock(self):
		logger.open("rpc/test_001_getblock.log", "test_001_getblock")
		(result, response) = rpcApi.getblock(height = None, blockhash = self.m_block_hash_right, verbose = None)
		logger.close(result)

	def test_002_getblock(self):
		logger.open("rpc/test_002_getblock.log", "test_002_getblock")
		(result, response) = rpcApi.getblock(height = None, blockhash = self.m_block_hash_error, verbose = None)
		logger.close(not result)
	
	def test_003_getblock(self):
		logger.open("rpc/test_003_getblock.log", "test_003_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = None)
		logger.close(result)
	
	def test_004_getblock(self):
		logger.open("rpc/test_004_getblock.log", "test_004_getblock")
		(result, response) = rpcApi.getblock(height = 0, blockhash = None, verbose = None)
		logger.close(result)
		
	def test_005_getblock(self):
		logger.open("rpc/test_005_getblock.log", "test_005_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_wrong, blockhash = None, verbose = None)
		logger.close(not result)

	def test_006_getblock(self):
		logger.open("rpc/test_006_getblock.log", "test_006_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_overflow, blockhash = None, verbose = None)
		logger.close(not result)

	def test_007_getblock(self):
		logger.open("rpc/test_007_getblock.log", "test_007_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 0)
		logger.close(result)

	def test_008_getblock(self):
		logger.open("rpc/test_008_getblock.log", "test_008_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 1)
		logger.close(result)

	def test_009_getblock(self):
		logger.open("rpc/test_009_getblock.log", "test_009_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = -1)
		logger.close(result)
	
	def test_010_getblock(self):
		logger.open("rpc/test_010_getblock.log", "test_010_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = 2)
		logger.close(result)
	
	def test_011_getblock(self):
		logger.open("rpc/test_011_getblock.log", "test_011_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = "abc")
		logger.close(not result)
	
	def test_012_getblock(self):
		logger.open("rpc/test_012_getblock.log", "test_012_getblock")
		(result, response) = rpcApi.getblock(height = self.m_block_height_right, blockhash = None, verbose = None)
		logger.close(result)

	def test_013_getblockhash(self):
		logger.open("rpc/test_013_getblockhash.log", "test_013_getblockhash")
		(result, response) = rpcApi.getblockhash(height = self.m_block_height_right)
		logger.close(result)
	
	def test_014_getblockhash(self):
		logger.open("rpc/test_014_getblockhash.log", "test_014_getblockhash")
		(result, response) = rpcApi.getblockhash(height = 0)
		logger.close(result)
	
	def test_015_getblockhash(self):
		logger.open("rpc/test_015_getblockhash.log", "test_015_getblockhash")
		(result, response) = rpcApi.getblockhash(height = self.m_block_height_wrong)
		logger.close(not result)

	def test_016_getblockhash(self):
		logger.open("rpc/test_016_getblockhash.log", "test_016_getblockhash")
		(result, response) = rpcApi.getblockhash(height = self.m_block_height_overflow)
		logger.close(not result)

	def test_017_getblockhash(self):
		logger.open("rpc/test_017_getblockhash.log", "test_017_getblockhash")
		(result, response) = rpcApi.getblockhash(height = "abc")
		logger.close(not result)

	def test_018_getblockhash(self):
		logger.open("rpc/test_018_getblockhash.log", "test_018_getblockhash")
		(result, response) = rpcApi.getblockhash(height = -1)
		logger.close(not result)
	
	def test_019_getblockhash(self):
		logger.open("rpc/test_019_getblockhash.log", "test_019_getblockhash")
		(result, response) = rpcApi.getblockhash(height = None)
		logger.close(not result)

	def test_020_getbestblockhash(self):
		logger.open("rpc/test_020_getbestblockhash.log", "test_020_getbestblockhash")
		(result, response) = rpcApi.getbestblockhash()
		logger.close(result)
	
	def test_022_getblockcount(self):
		logger.open("rpc/test_022_getblockcount.log", "test_022_getblockcount")
		(result, response) = rpcApi.getblockcount()
		logger.close(result)

	def test_024_getconnectioncount(self):
		logger.open("rpc/test_024_getconnectioncount.log", "test_024_getconnectioncount")
		(result, response) = rpcApi.getconnectioncount()
		logger.close(result and int(response["result"]) == 6)

	# can not test
	def test_025_getconnectioncount(self):
		stop_nodes([1, 2, 3, 4, 5, 6])
		
		logger.open("rpc/test_025_getconnectioncount.log", "test_025_getconnectioncount")
		(result, response) = rpcApi.getconnectioncount()
		logger.close(result and int(response["result"]) == 0)
		
		start_nodes([1, 2, 3, 4, 5, 6], Config.DEFAULT_NODE_ARGS, False, False)
		time.sleep(10)
	
	def test_026_getgenerateblocktime(self):
		logger.open("rpc/test_026_getgenerateblocktime.log", "test_026_getgenerateblocktime")
		(result, response) = rpcApi.getgenerateblocktime()
		logger.close(result)
	'''
	# can not test
	def test_026_getconnectioncount_1(self):
		logger.open("rpc/27_getconnectioncount.log", "27_getconnectioncount")
		(result, response) = rpcApi.getgenerateblocktime()
		logger.close(not result)
	'''
	
	def test_027_getrawtransaction(self):
		logger.open("rpc/test_027_getrawtransaction.log", "test_027_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right)
		logger.close(result)
	
	def test_028_getrawtransaction(self):
		logger.open("rpc/test_028_getrawtransaction.log", "test_028_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_wrong)
		logger.close(not result)

	def test_029_getrawtransaction(self):
		logger.open("rpc/test_029_getrawtransaction.log", "test_029_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction("abc")
		logger.close(not result)

	def test_030_getrawtransaction(self):
		logger.open("rpc/test_030_getrawtransaction.log", "test_030_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(1)
		logger.close(not result)
	
	def test_031_getrawtransaction(self):
		logger.open("rpc/test_031_getrawtransaction.log", "test_031_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(None)
		logger.close(not result)
	
	def test_032_getrawtransaction(self):
		logger.open("rpc/test_032_getrawtransaction.log", "test_032_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, 1)
		logger.close(result)
	
	def test_033_getrawtransaction(self):
		logger.open("rpc/test_033_getrawtransaction.log", "test_033_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, 0)
		logger.close(result)

	def test_034_getrawtransaction(self):
		logger.open("rpc/test_034_getrawtransaction.log", "test_034_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, -1)
		logger.close(result)

	def test_035_getrawtransaction(self):
		logger.open("rpc/test_035_getrawtransaction.log", "test_035_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, 2)
		logger.close(result)

	def test_036_getrawtransaction(self):
		logger.open("rpc/test_036_getrawtransaction.log", "test_036_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, "abc")
		logger.close(not result)

	def test_037_getrawtransaction(self):
		logger.open("rpc/test_037_getrawtransaction.log", "test_037_getrawtransaction")
		(result, response) = rpcApi.getrawtransaction(self.m_txhash_right, None)
		logger.close(result)
	
	def test_038_sendrawtransaction(self):
		logger.open("rpc/test_038_sendrawtransaction.log", "test_038_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction(self.m_signed_txhash_right)
		logger.close(result)
	
	def test_039_sendrawtransaction(self):
		logger.open("rpc/test_039_sendrawtransaction.log", "test_039_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction("")
		logger.close(not result)
	
	def test_040_sendrawtransaction(self):
		logger.open("rpc/test_040_sendrawtransaction.log", "test_040_sendrawtransaction")
		(result, response) = rpcApi.sendrawtransaction(None)
		logger.close(not result)
	
	def test_041_getstorage(self):
		logger.open("rpc/test_041_getstorage.log", "test_041_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, self.m_getstorage_contract_key)
		logger.close(result and response["result"] == self.m_getstorage_contract_value)

	def test_042_getstorage(self):
		logger.open("rpc/test_042_getstorage.log", "test_042_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr_wrong, self.m_getstorage_contract_key)
		logger.close(not result)

	def test_043_getstorage(self):
		logger.open("rpc/test_043_getstorage.log", "test_043_getstorage")
		(result, response) = rpcApi.getstorage("abc", self.m_getstorage_contract_key)
		logger.close(not result)

	def test_044_getstorage(self):
		logger.open("rpc/test_044_getstorage.log", "test_044_getstorage")
		(result, response) = rpcApi.getstorage(1, self.m_getstorage_contract_key)
		logger.close(not result)

	def test_045_getstorage(self):
		logger.open("rpc/test_045_getstorage.log", "test_045_getstorage")
		(result, response) = rpcApi.getstorage(None, self.m_getstorage_contract_key)
		logger.close(not result)

	def test_046_getstorage(self):
		logger.open("rpc/test_046_getstorage.log", "test_046_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, self.m_getstorage_contract_key)
		logger.close(result)

	def test_047_getstorage(self):
		logger.open("rpc/test_047_getstorage.log", "test_047_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, "getstorage_key_error")
		logger.close(not result)

	def test_048_getstorage(self):
		logger.open("rpc/test_048_getstorage.log", "test_048_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, "abc")
		logger.close(not result)

	def test_049_getstorage(self):
		logger.open("rpc/test_049_getstorage.log", "test_049_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, 123)
		logger.close(not result)
	
	def test_050_getstorage(self):
		logger.open("rpc/test_050_getstorage.log", "test_050_getstorage")
		(result, response) = rpcApi.getstorage(self.m_getstorage_contract_addr, None)
		logger.close(not result)
	

	def test_051_getversion(self):
		logger.open("rpc/test_051_getversion.log", "test_051_getversion")
		(result, response) = rpcApi.getversion()
		logger.close(result)

	# can not test
	'''
	def test_52_getversion(self):
		self.clear_nodes();
		logger.open("rpc/52_getversion.log", "52_getversion")
		(result, response) = rpcApi.getversion()
		logger.close(not result)
	
	def test_53_getblocksysfee(self):
		logger.open("rpc/52_getversion.log", "52_getversion")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(result)

	# can not test
	def test_54_getblocksysfee(self):
		logger.open("rpc/54_getblocksysfee.log", "54_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_true)
		logger.close(result)

	def test_55_getblocksysfee(self):
		logger.open("rpc/55_getblocksysfee.log", "55_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(getblocksysfee_index_false)
		logger.close(not result)

	def test_56_getblocksysfee(self):
		logger.open("rpc/56_getblocksysfee.log", "56_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee("abc")
		logger.close(not result)

	def test_57_getblocksysfee(self):
		logger.open("rpc/57_getblocksysfee.log", "57_getblocksysfee")
		(result, response) = rpcApi.getblocksysfee(None)
		logger.close(not result)
	'''
	def test_058_getcontractstate(self):
		logger.open("rpc/test_058_getcontractstate.log", "test_058_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right)
		logger.close(result)

	def test_059_getcontractstate(self):
		logger.open("rpc/test_059_getcontractstate.log", "test_059_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_txhash_wrong)
		logger.close(not result)

	def test_060_getcontractstate(self):
		logger.open("rpc/test_060_getcontractstate.log", "test_060_getcontractstate")
		(result, response) = rpcApi.getcontractstate("abc")
		logger.close(not result)

	def test_061_getcontractstate(self):
		logger.open("rpc/test_061_getcontractstate", "test_061_getcontractstate")
		(result, response) = rpcApi.getcontractstate(123)
		logger.close(not result)

	def test_062_getcontractstate(self):
		logger.open("rpc/test_062_getcontractstate.log", "test_062_getcontractstate")
		(result, response) = rpcApi.getcontractstate(None, 1)
		logger.close(not result)

	def test_063_getcontractstate(self):
		logger.open("rpc/test_063_getcontractstate.log", "test_063_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 1)
		logger.close(result)

	def test_064_getcontractstate(self):
		logger.open("rpc/test_064_getcontractstate.log", "test_064_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, -1)
		logger.close(result)

	def test_065_getcontractstate(self):
		logger.open("rpc/test_065_getcontractstate.log", "test_065_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 2)
		logger.close(result)

	def test_066_getcontractstate(self):
		logger.open("rpc/test_066_getcontractstate.log", "test_066_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, "abc")
		logger.close(not result)

	def test_067_getcontractstate(self):
		logger.open("rpc/test_067_getcontractstate.log", "test_067_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, 0)
		logger.close(result)

	def test_068_getcontractstate(self):
		logger.open("rpc/test_068_getcontractstate.log", "test_068_getcontractstate")
		(result, response) = rpcApi.getcontractstate(self.m_contractaddr_right, None)
		logger.close(result)

	def test_069_getmempooltxstate(self):
		logger.open("rpc/test_069_getmempooltxstate.log", "test_069_getmempooltxstate")
		(result, response) = invoke_function(self.m_contractaddr_right, "put", "", "1", argvs = [{"type": "bytearray","value": self.m_getstorage_contract_key},{"type": "bytearray","value": self.m_getstorage_contract_value}], node_index = 0, sleep = 0)

		(result, response) = rpcApi.getmempooltxstate(response["txhash"])
		logger.close(result)

	def test_070_getmempooltxstate(self):
		logger.open("rpc/test_070_getmempooltxstate.log", "test_070_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(self.m_txhash_right)
		logger.close(not result)

	def test_071_getmempooltxstate(self):
		logger.open("rpc/test_071_getmempooltxstate.log", "test_071_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate("abc")
		logger.close(not result)

	def test_072_getmempooltxstate(self):
		logger.open("rpc/test_072_getmempooltxstate.log", "test_072_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(123)
		logger.close(not result)

	def test_073_getmempooltxstate(self):
		logger.open("rpc/test_073_getmempooltxstate.log", "test_073_getmempooltxstate")
		(result, response) = rpcApi.getmempooltxstate(None)
		logger.close(not result)
	
	def test_074_getsmartcodeevent(self):
		logger.open("rpc/test_074_getsmartcodeevent.log", "test_074_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height = self.getsmartcodeevent_height)
		logger.close(result)

	def test_075_getsmartcodeevent(self):
		logger.open("rpc/test_075_getsmartcodeevent.log", "test_075_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height = 99999999)
		logger.close(not result)

	def test_076_getsmartcodeevent(self):
		logger.open("rpc/test_076_getsmartcodeevent.log", "test_076_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height="abc")
		logger.close(not result)

	def test_077_getsmartcodeevent(self):
		logger.open("rpc/test_077_getsmartcodeevent.log", "test_077_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(height =None)
		logger.close(not result)
	
	def test_078_getsmartcodeevent(self):
		logger.open("rpc/test_078_getsmartcodeevent.log", "test_078_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(tx_hash = self.m_txhash_right)
		logger.close(result)

	def test_079_getsmartcodeevent(self):
		logger.open("rpc/test_079_getsmartcodeevent.log", "test_079_getsmartcodeevent")
		(result, response) = rpcApi.getsmartcodeevent(tx_hash = self.m_txhash_wrong)
		logger.close(not result)
	
	def test_080_getblockheightbytxhash(self):
		logger.open("rpc/test_080_getblockheightbytxhash.log", "test_080_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = self.m_txhash_right)
		logger.close(result)

	def test_081_getblockheightbytxhash(self):
		logger.open("rpc/test_081_getblockheightbytxhash.log", "test_081_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = self.m_txhash_wrong)
		logger.close(not result)

	def test_082_getblockheightbytxhash(self):
		logger.open("rpc/test_082_getblockheightbytxhash.log", "test_082_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = "abc")
		logger.close(not result)

	def test_083_getblockheightbytxhash(self):
		logger.open("rpc/test_083_getblockheightbytxhash.log", "test_083_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = 123)
		logger.close(not result)
	
	def test_084_getblockheightbytxhash(self):
		logger.open("rpc/test_084_getblockheightbytxhash.log", "test_084_getblockheightbytxhash")
		(result, response) = rpcApi.getblockheightbytxhash(tx_hash = None)
		logger.close(not result)

	def test_085_getbalance(self):
		logger.open("rpc/test_085_getbalance.log", "test_085_getbalance")
		(result, response) = rpcApi.getbalance(self.getbalance_address_true)
		logger.close(result)
	
	def test_086_getbalance(self):
		logger.open("rpc/test_086_getbalance.log", "test_086_getbalance")
		(result, response) = rpcApi.getbalance(self.getbalance_address_false)
		logger.close(not result)
	
	def test_087_getbalance(self):
		logger.open("rpc/test_087_getbalance.log", "test_087_getbalance")
		(result, response) = rpcApi.getbalance("abc")
		logger.close(not result)

	def test_088_getbalance(self):
		logger.open("rpc/test_088_getbalance.log", "test_088_getbalance")
		(result, response) = rpcApi.getbalance(None)
		logger.close(not result)
	
	def test_089_getmerkleproof(self):
		logger.open("rpc/test_089_getmerkleproof.log", "test_089_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(self.m_txhash_right)
		logger.close(result)

	def test_090_getmerkleproof(self):
		logger.open("rpc/test_090_getmerkleproof.log", "test_090_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(self.m_txhash_wrong)
		logger.close(not result)

	def test_091_getmerkleproof(self):
		logger.open("rpc/test_091_getmerkleproof.log", "test_091_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof("abc")
		logger.close(not result)

	def test_092_getmerkleproof(self):
		logger.open("rpc/test_092_getmerkleproof.log", "test_092_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof("123")
		logger.close(not result)
	
	def test_093_getmerkleproof(self):
		logger.open("rpc/test_093_getmerkleproof.log", "test_093_getmerkleproof")
		(result, response) = rpcApi.getmerkleproof(None)
		logger.close(not result)

	def test_094_getmerkleproof(self):
		logger.open("rpc/test_094_getmerkleproof.log", "test_094_getmerkleproof")
		task = Task("tasks/rpc/94_getmerkleproof.json")
		task.request()["params"] = [self.m_txhash_right]
		(result, response) =  run_single_task(task)
		logger.close(result)

	def test_095_getmerkleproof(self):
		logger.open("rpc/test_095_getmerkleproof.log", "test_095_getmerkleproof")
		task = Task("tasks/rpc/95_getmerkleproof.json")
		task.request()["params"] = [self.m_txhash_right]
		(result, response) =  run_single_task(task)
		logger.close(result)

	# can not test
	def test_096_getmerkleproof(self):
		logger.open("rpc/test_096_getmerkleproof.log", "test_096_getmerkleproof")
		task = Task("tasks/rpc/96_getmerkleproof.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)
	
	def test_097_getmerkleproof(self):
		logger.open("rpc/test_097_getmerkleproof.log", "test_097_getmerkleproof")
		task = Task("tasks/rpc/97_getmerkleproof.1.json")
		(result, response) =  run_single_task(task)
		logger.close(not result)	

if __name__ == '__main__':
    unittest.main()
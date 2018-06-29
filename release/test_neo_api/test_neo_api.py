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
from utils.websocketapi import WebSocketApi
from utils.commonapi import *
from utils.base import WebSocket
from test_api import *
from neo_api_conf import Conf

from utils.commonapi import call_contract

logger = LoggerInstance

####################################################
#test cases
class TestNeoAPI(ParametrizedTestCase):
	def start(self, log_path):
		logger.open(log_path)

	def finish(self, task_name, log_path, result, msg):
		if result:
			logger.print("[ OK       ] ")
			logger.append_record(task_name, "pass", log_path)
		else:
			logger.print("[ Failed   ] " + msg)
			logger.append_record(task_name, "fail", log_path)
		logger.close()

	def test_01_blockchain_get_height(self):
		log_path = "01_blockchain_get_height.log"
		task_name = "01_blockchain_get_height"
		self.start(log_path)
		(result, response) = invoke_func_with_0_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEIGHT_FUNC_NAME)
		self.normal_finish(task_name, log_path, result, "")

	def test_03_blockchain_get_header(self):
		log_path = "03_blockchain_get_header.log"
		task_name = "03_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")
	
	def test_04_blockchain_get_header(self):
		log_path = "04_blockchain_get_header.log"
		task_name = "04_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_INCORRECT_2)
		self.normal_finish(task_name, log_path, result, "")

	def test_05_blockchain_get_header(self):
		log_path = "05_blockchain_get_header.log"
		task_name = "05_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_BORDER_BOTTON)
		self.normal_finish(task_name, log_path, result, "")

	def test_06_blockchain_get_header(self):
		log_path = "06_blockchain_get_header.log"
		task_name = "06_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_BORDER_TOP)
		self.normal_finish(task_name, log_path, result, "")

	def test_07_blockchain_get_header(self):
		log_path = "07_blockchain_get_header.log"
		task_name = "07_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_INCORRECT_1)
		self.normal_finish(task_name, log_path, result, "")

	def test_08_blockchain_get_header(self):
		log_path = "08_blockchain_get_header.log"
		task_name = "08_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_INCORRECT_3)
		self.normal_finish(task_name, log_path, result, "")

	def test_09_blockchain_get_header(self):
		log_path = "09_blockchain_get_header.log"
		task_name = "09_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_INCORRECT_4)
		self.normal_finish(task_name, log_path, result, "")

	def test_10_blockchain_get_block(self):
		log_path = "10_blockchain_get_block.log"
		task_name = "10_blockchain_get_block"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.BLOCK_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_11_blockchain_get_header(self):
		log_path = "11_blockchain_get_header.log"
		task_name = "11_blockchain_get_header"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.BLOCK_HASH_INCORRECT_4)
		self.normal_finish(task_name, log_path, result, "")

	def test_12_blockchain_get_transaction(self):
		log_path = "12_blockchain_get_transaction.log"
		task_name = "12_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_TRANSACTION_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.TX_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_13_blockchain_get_transaction(self):
		log_path = "13_blockchain_get_transaction.log"
		task_name = "13_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_TRANSACTION_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.TX_HASH_INCORRECT_4)
		self.normal_finish(task_name, log_path, result, "")

	def test_15_blockchain_get_transaction(self):
		log_path = "15_blockchain_get_transaction.log"
		task_name = "15_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_TRANSACTION_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, [Conf.TX_HASH_CORRECT, Conf.TX_HASH_CORRECT])
		self.normal_finish(task_name, log_path, result, "")

	def test_16_blockchain_get_contact(self):
		log_path = "16_blockchain_get_contact.log"
		task_name = "16_blockchain_get_contact"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_CONTRACT_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.SCRIPT_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_17_blockchain_get_contact(self):
		log_path = "17_blockchain_get_contact.log"
		task_name = "17_blockchain_get_contact"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_CONTRACT_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.SCRIPT_HASH_INCORRECT_1)
		self.normal_finish(task_name, log_path, result, "")

	def test_18_blockchain_get_contact(self):
		log_path = "18_blockchain_get_contact.log"
		task_name = "18_blockchain_get_contact"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_CONTRACT_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.SCRIPT_HASH_INCORRECT_2)
		self.normal_finish(task_name, log_path, result, "")

	def test_20_blockchain_get_hash(self):
		log_path = "20_blockchain_get_hash.log"
		task_name = "20_blockchain_get_hash"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_HASH_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_22_blockchain_get_version(self):
		log_path = "22_blockchain_get_version.log"
		task_name = "22_blockchain_get_version"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_VERSION_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_24_blockchain_get_prehash(self):
		log_path = "24_blockchain_get_prehash.log"
		task_name = "24_blockchain_get_prehash"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_PREHASH_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_26_blockchain_get_index(self):
		log_path = "26_blockchain_get_index.log"
		task_name = "26_blockchain_get_index"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_INDEX_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_28_blockchain_get_merkle_root(self):
		log_path = "28_blockchain_get_merkle_root.log"
		task_name = "28_blockchain_get_merkle_root"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_MERKLEROOT_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_30_blockchain_get_timestamp(self):
		log_path = "30_blockchain_get_timestamp.log"
		task_name = "30_blockchain_get_timestamp"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_TIMESTAMP_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_32_blockchain_get_consensusdata(self):
		log_path = "32_blockchain_get_consensusdata.log"
		task_name = "32_blockchain_get_consensusdata"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_CONSENSUS_DATA_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_34_blockchain_get_next_consensus(self):
		log_path = "34_blockchain_get_next_consensus.log"
		task_name = "34_blockchain_get_next_consensus"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_HEADER_NEXT_CONSENSUS_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_36_blockchain_get_transaction_count(self):
		log_path = "36_blockchain_get_transaction_count.log"
		task_name = "36_blockchain_get_transaction_count"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_37_blockchain_get_transaction_count(self):
		log_path = "37_blockchain_get_transaction_count.log"
		task_name = "37_blockchain_get_transaction_count"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME, Conf.PARAM_TYPE_INT, "2")
		self.normal_finish(task_name, log_path, result, "")

	def test_38_blockchain_get_transactions(self):
		log_path = "38_blockchain_get_transactions.log"
		task_name = "38_blockchain_get_transactions"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTIONS_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.HEIGHT_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_39_blockchain_get_transactions(self):
		log_path = "39_blockchain_get_transactions.log"
		task_name = "39_blockchain_get_transactions"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTIONS_FUNC_NAME, Conf.PARAM_TYPE_INT, "2")
		self.normal_finish(task_name, log_path, result, "")

	def test_40_blockchain_get_transactions(self):
		log_path = "40_blockchain_get_transaction.log"
		task_name = "40_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTIONS_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.BLOCK_HEIGHT_WITH_TX, Conf.PARAM_TYPE_INT, "1")
		self.normal_finish(task_name, log_path, result, "")

	def test_41_blockchain_get_transaction(self):
		log_path = "41_blockchain_get_transaction.log"
		task_name = "41_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTION_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.BLOCK_HEIGHT_WITHOUT_TX, Conf.PARAM_TYPE_INT, "0")
		self.normal_finish(task_name, log_path, result, "")

	def test_42_blockchain_get_transaction(self):
		log_path = "42_blockchain_get_transaction.log"
		task_name = "42_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTIONS_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.BLOCK_HEIGHT_WITH_TX, Conf.PARAM_TYPE_INT, "-1")
		self.normal_finish(task_name, log_path, result, "")

	def test_43_blockchain_get_transaction(self):
		log_path = "43_blockchain_get_transaction.log"
		task_name = "43_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTIONS_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.BLOCK_HEIGHT_WITH_TX, Conf.PARAM_TYPE_INT, "0")
		self.normal_finish(task_name, log_path, result, "")

	def test_44_blockchain_get_transaction(self):
		log_path = "44_blockchain_get_transaction.log"
		task_name = "44_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTIONS_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.BLOCK_HEIGHT_WITH_TX, Conf.PARAM_TYPE_INT, "1")
		self.normal_finish(task_name, log_path, result, "")

	def test_45_blockchain_get_transaction(self):
		log_path = "45_blockchain_get_transaction.log"
		task_name = "45_blockchain_get_transaction"
		self.start(log_path)
		(result, response) = invoke_func_with_2_param(Conf.CONTRACT_ADDRESS, Conf.GET_BLOCK_TRANSACTIONS_FUNC_NAME, Conf.PARAM_TYPE_INT, Conf.BLOCK_HEIGHT_WITH_TX, Conf.PARAM_TYPE_INT, "2")
		self.normal_finish(task_name, log_path, result, "")

	def test_46_blockchain_get_transaction_hash(self):
		log_path = "46_blockchain_get_transaction_hash.log"
		task_name = "46_blockchain_get_transaction_hash"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_CONTRACTION_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.TX_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")
	
	def test_48_blockchain_get_transaction_type(self):
		log_path = "48_blockchain_get_transaction_type.log"
		task_name = "48_blockchain_get_transaction_type"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_CONTRACTION_TYPE_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.TX_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_50_gettransaction_attributes(self):
		log_path = "50_gettransaction_attributes.log"
		task_name = "50_gettransaction_attributes"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_TRANSACTIONS_ATTRIBUTE_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.TX_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_52_gettransactionattribute_usage(self):
		log_path = "52_gettransactionattribute_usage.log"
		task_name = "52_gettransactionattribute_usage"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_TRANSACTIONS_ATTRIBUTE_USAGE_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.TX_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_54_gettransactionattribute_data(self):
		log_path = "52_gettransactionattribute_data.log"
		task_name = "52_gettransactionattribute_data"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_TRANSACTIONS_ATTRIBUTE_DATA_FUNC_NAME, Conf.PARAM_TYPE_BYTEARRAY, Conf.TX_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_56_getcontract_script(self):
		log_path = "56_getcontract_script.log"
		task_name = "56_getcontract_script"
		self.start(log_path)
		(result, response) = invoke_func_with_1_param(Conf.CONTRACT_ADDRESS, Conf.GET_CONTRACT_SCRIPT_FUNC_TIME, Conf.PARAM_TYPE_BYTEARRAY, Conf.SCRIPT_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_58_getcontract_create(self):
		log_path = "58_getcontract_create.log"
		task_name = "58_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(Conf.CONTRACT_ADDRESS, Conf.SCRIPT_HASH_CORRECT)
		self.normal_finish(task_name, log_path, result, "")

	def test_59_getcontract_create(self):
		log_path = "59_getcontract_create.log"
		task_name = "59_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(Conf.CONTRACT_ADDRESS, Conf.SCRIPT_HASH_INCORRECT_1)
		self.normal_finish(task_name, log_path, result, "")

	def test_60_getcontract_create(self):
		log_path = "60_getcontract_create.log"
		task_name = "60_getcontract_create"
		self.start(log_path)
		(result, response) = invoke_contract_create(Conf.CONTRACT_ADDRESS, Conf.SCRIPT_HASH_INCORRECT_1)
		self.normal_finish(task_name, log_path, result, "")
	
####################################################
if __name__ == '__main__':
	suite = unittest.main()

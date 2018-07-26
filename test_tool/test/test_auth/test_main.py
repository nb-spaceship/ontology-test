# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')
sys.path.append('../..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

#from utils.selfig import selfig
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.config import Config

from api.apimanager import API
# from api.init_ong_ont import *
# from api.contract import *
# from api.nativecontract import *
# from api.rpc import *
# from api.contract import call_contract

from test_api import *
from test_config import test_config

####################################################
#test cases
class test_auth_1(ParametrizedTestCase):
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		# time.sleep(2)
		# print("stop all")
		# API.node().stop_all_nodes()
		# print("start all")
		# API.node().start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
		# time.sleep(10)
		# API.native().regid_with_publickey(0)
		# API.native().regid_with_publickey(1)
		# API.native().regid_with_publickey(2)
		# API.native().regid_with_publickey(3)
		# API.native().regid_with_publickey(4)
		# API.native().regid_with_publickey(5)
		# API.native().regid_with_publickey(6)
		# API.native().regid_with_publickey(7)
		# API.native().regid_with_publickey(8)
		# API.native().init_ont_ong()

		(test_config.contract_addr, test_config.contract_tx_hash) = API.contract().deploy_contract_full(test_config.deploy_neo_1)
		(test_config.contract_addr_1, test_config.contract_tx_hash_1) = API.contract().deploy_contract_full(test_config.deploy_neo_2)
		(test_config.contract_addr_2, test_config.contract_tx_hash_2) = API.contract().deploy_contract_full(test_config.deploy_neo_3)
		(test_config.contract_addr_3, test_config.contract_tx_hash_3) = API.contract().deploy_contract_full(test_config.deploy_neo_4)
		(test_config.contract_addr_10, test_config.contract_tx_hash_10) = API.contract().deploy_contract_full(test_config.deploy_neo_5)
		(test_config.contract_addr_11, test_config.contract_tx_hash_11) = API.contract().deploy_contract_full(test_config.deploy_neo_6)
		(test_config.contract_addr_12, test_config.contract_tx_hash_12) = API.contract().deploy_contract_full(test_config.deploy_neo_7)
		(test_config.contract_addr_138_1, test_config.contract_tx_hash_138_1) = API.contract().deploy_contract_full(test_config.deploy_neo_8)
		(test_config.contract_addr_138_2, test_config.contract_tx_hash_138_2) = API.contract().deploy_contract_full(test_config.deploy_neo_9)
		(test_config.contract_addr_139, test_config.contract_tx_hash_139) = API.contract().deploy_contract_full(test_config.deploy_neo_10)
		


	def tearDown(self):
		logger.close(self.result())
		
	
	def test_base_001_initContractAdmin(self):		
		try:
			init(register_ontid = True, restart = True)
			(process, response) = init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			self.ASSERT(response["result"]["Result"] == "01", "")
		except Exception as e:
			print(e.args)

	def test_abnormal_002_initContractAdmin(self):
		#log_path = "02_initContractAdmin.log"
		#task_name ="02_initContractAdmin"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = init_admin(test_config.CONTRACT_ADDRESS_INCORRECT_1, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_003_initContractAdmin(self):
		#log_path = "03_initContractAdmin.log"
		#task_name ="03_initContractAdmin"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = init_admin(test_config.CONTRACT_ADDRESS_INCORRECT_2, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_004_initContractAdmin(self):
		#log_path = "04_initContractAdmin.log"
		#task_name ="04_initContractAdmin"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = init_admin(test_config.CONTRACT_ADDRESS_INCORRECT_3, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_005_verifyToken(self):
		#log_path = "05_verifyToken.log"
		#task_name ="05_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_006_verifyToken(self):
		#log_path = "06_verifyToken.log"
		#task_name ="06_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_B)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_007_verifyToken(self):
		#log_path = "07_verifyToken.log"
		#task_name ="07_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_C)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_008_verifyToken(self):
		#log_path = "08_verifyToken.log"
		#task_name ="08_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_D)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_009_verifyToken(self):
		#log_path = "09_verifyToken.log"
		#task_name ="09_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_010_verifyToken(self):
		#log_path = "10_verifyToken.log"
		#task_name ="10_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_INCORRECT_10, test_config.FUNCTION_A, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_011_verifyToken(self):
		#log_path = "11_verifyToken.log"
		#task_name ="11_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_INCORRECT_11, test_config.FUNCTION_A, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_012_verifyToken(self):
		#log_path = "12_verifyToken.log"
		#task_name ="12_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_INCORRECT_12, test_config.FUNCTION_A, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_013_verifyToken(self):
		#log_path = "13_verifyToken.log"
		#task_name ="13_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_014_verifyToken(self):
		#log_path = "14_verifyToken.log"
		#task_name ="14_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, "C", test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_015_verifyToken(self):
		#log_path = "15_verifyToken.log"
		#task_name ="15_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_B, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_016_verifyToken(self):
		#log_path = "16_verifyToken.log"
		#task_name ="16_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, "", test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	
	def test_base_017_transfer(self):
		#log_path = "17_transfer.log"
		#task_name ="17_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_018_transfer(self):
		#log_path = "18_transfer.log"
		#task_name ="18_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_INCORRECT_1, test_config.ontID_A)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_019_transfer(self):
		#log_path = "19_transfer.log"
		#task_name ="19_transfer"
		try:
		# init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_020_transfer(self):
		#log_path = "20_transfer.log"
		#task_name ="20_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_INCORRECT_5, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_021_transfer(self):
		#log_path = "21_transfer.log"
		#task_name ="21_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_INCORRECT_6, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_022_transfer(self):
		#log_path = "22_transfer.log"
		#task_name ="22_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_023_transfer(self):
		#log_path = "23_transfer.log"
		#task_name ="23_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_24_transfer(self):
		#log_path = "24_transfer.log"
		#task_name ="24_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_C)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_025_transfer(self):
		#log_path = "25_transfer.log"
		#task_name ="25_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_D)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_026_transfer(self):
		#log_path = "26_transfer.log"
		#task_name ="26_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_027_transfer(self):
		#log_path = "27_transfer.log"
		#task_name ="27_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, public_key=test_config.KEY_NO_1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_028_transfer(self):
		#log_path = "28_transfer.log"
		#task_name ="28_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, public_key=test_config.KEY_NO_2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_029_transfer(self):
		#log_path = "29_transfer.log"
		#task_name ="29_transfer"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = transfer(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, public_key=test_config.KEY_NO_3)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	
	def test_base_030_assignFuncsToRole(self):
		#log_path = "30_assignFuncsToRole.log"
		#task_name ="30_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_031_assignFuncsToRole(self):
		#log_path = "31_assignFuncsToRole.log"
		#task_name ="31_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_INCORRECT_4, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_032_assignFuncsToRole(self):
		#log_path = "32_assignFuncsToRole.log"
		#task_name ="32_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_INCORRECT_5, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_033_assignFuncsToRole(self):
		#log_path = "33_assignFuncsToRole.log"
		#task_name ="33_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_INCORRECT_6, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_034_assignFuncsToRole(self):
		#log_path = "34_assignFuncsToRole.log"
		#task_name ="34_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_035_assignFuncsToRole(self):
		#log_path = "35_assignFuncsToRole.log"
		#task_name ="35_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_036_assignFuncsToRole(self):
		#log_path = "36_assignFuncsToRole.log"
		#task_name ="36_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_037_assignFuncsToRole(self):
		#log_path = "37_assignFuncsToRole.log"
		#task_name ="37_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_C, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_038_assignFuncsToRole(self):
		#log_path = "38_assignFuncsToRole.log"
		#task_name ="38_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_D, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_039_assignFuncsToRole(self):
		#log_path = "39_assignFuncsToRole.log"
		#task_name ="39_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_040_assignFuncsToRole(self):
		#log_path = "40_assignFuncsToRole.log"
		#task_name ="40_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_041_assignFuncsToRole(self):
		#log_path = "41_assignFuncsToRole.log"
		#task_name ="41_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_INCORRECT_1, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_042_assignFuncsToRole(self):
		#log_path = "42_assignFuncsToRole.log"
		#task_name ="42_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_INCORRECT_2, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_043_assignFuncsToRole(self):
		#log_path = "43_assignFuncsToRole.log"
		#task_name ="43_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_044_assignFuncsToRole(self):
		#log_path = "44_assignFuncsToRole.log"
		#task_name ="44_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_B, test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_045_assignFuncsToRole(self):
		#log_path = "45_assignFuncsToRole.log"
		#task_name ="45_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])		
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A, test_config.FUNCTION_B, test_config.FUNCTION_C])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_046_assignFuncsToRole(self):
		#log_path = "46_assignFuncsToRole.log"
		#task_name ="46_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])		
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_047_assignFuncsToRole(self):
		#log_path = "47_assignFuncsToRole.log"
		#task_name ="47_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])		
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_INCORRECT_2, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_048_assignFuncsToRole(self):
		#log_path = "48_assignFuncsToRole.log"
		#task_name ="48_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_D])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_049_assignFuncsToRole(self):
		#log_path = "49_assignFuncsToRole.log"
		#task_name ="49_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A, test_config.FUNCTION_D])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_050_assignFuncsToRole(self):
		#log_path = "50_assignFuncsToRole.log"
		#task_name ="50_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_051_assignFuncsToRole(self):
		#log_path = "51_assignFuncsToRole.log"
		#task_name ="51_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A], public_key = test_config.KEY_NO_1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_052_assignFuncsToRole(self):
		#log_path = "52_assignFuncsToRole.log"
		#task_name ="52_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A], public_key = test_config.KEY_NO_2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_053_assignFuncsToRole(self):
		#log_path = "53_assignFuncsToRole.log"
		#task_name ="53_assignFuncsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A], public_key = test_config.KEY_NO_3)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_054_assignOntIDsToRole(self):
		#log_path = "54_assignOntIDsToRole.log"
		#task_name ="54_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_055_assignOntIDsToRole(self):
		#log_path = "55_assignOntIDsToRole.log"
		#task_name ="55_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_INCORRECT_4, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_056_assignOntIDsToRole(self):
		#log_path = "56_assignOntIDsToRole.log"
		#task_name ="56_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_INCORRECT_5, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_057_assignOntIDsToRole(self):
		#log_path = "57_assignOntIDsToRole.log"
		#task_name ="57_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_INCORRECT_6, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_058_assignOntIDsToRole(self):
		#log_path = "58_assignOntIDsToRole.log"
		#task_name ="58_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_059_assignOntIDsToRole(self):
		#log_path = "59_assignOntIDsToRole.log"
		#task_name ="59_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_060_assignOntIDsToRole(self):
		#log_path = "60_assignOntIDsToRole.log"
		#task_name ="60_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B, test_config.ROLE_CORRECT, [test_config.ontID_A])
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_061_assignOntIDsToRole(self):
		#log_path = "61_assignOntIDsToRole.log"
		#task_name ="61_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_C, test_config.ROLE_CORRECT, [test_config.ontID_A])
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_062_assignOntIDsToRole(self):
		#log_path = "62_assignOntIDsToRole.log"
		#task_name ="62_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_D, test_config.ROLE_CORRECT, [test_config.ontID_A])
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_063_assignOntIDsToRole(self):
		#log_path = "63_assignOntIDsToRole.log"
		#task_name ="63_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_064_assignOntIDsToRole(self):
		#log_path = "64_assignOntIDsToRole.log"
		#task_name ="64_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_INCORRECT_3, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_065_assignOntIDsToRole(self):
		#log_path = "65_assignOntIDsToRole.log"
		#task_name ="65_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_INCORRECT_1, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_066_assignOntIDsToRole(self):
		#log_path = "66_assignOntIDsToRole.log"
		#task_name ="66_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A, test_config.ontID_B])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_067_assignOntIDsToRole(self):
		#log_path = "67_assignOntIDsToRole.log"
		#task_name ="67_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A, test_config.ontID_B, test_config.ontID_C])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_068_assignOntIDsToRole(self):
		#log_path = "68_assignOntIDsToRole.log"
		#task_name ="68_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_D])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_069_assignOntIDsToRole(self):
		#log_path = "69_assignOntIDsToRole.log"
		#task_name ="69_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_070_assignOntIDsToRole(self):
		#log_path = "70_assignOntIDsToRole.log"
		#task_name ="70_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A], public_key=test_config.KEY_NO_1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_071_assignOntIDsToRole(self):
		#log_path = "71_assignOntIDsToRole.log"
		#task_name ="71_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A], public_key=test_config.KEY_NO_2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_072_assignOntIDsToRole(self):
		#log_path = "72_assignOntIDsToRole.log"
		#task_name ="72_assignOntIDsToRole"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A], public_key=test_config.KEY_NO_3)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_073_delegate(self):
		#log_path = "73_delegate.log"
		#task_name ="73_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_074_delegate(self):
		#log_path = "74_delegate.log"
		#task_name ="74_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_4, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_075_delegate(self):
		#log_path = "75_delegate.log"
		#task_name ="75_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_5, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_076_delegate(self):
		#log_path = "76_delegate.log"
		#task_name ="76_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_6, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_077_delegate(self):
		#log_path = "77_delegate.log"
		#task_name ="77_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_078_delegate(self):
		#log_path = "78_delegate.log"
		#task_name ="78_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B, test_config.ontID_E, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT, node_index=2)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_079_delegate(self):
		#log_path = "79_delegate.log"
		#task_name ="79_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_080_delegate(self):
		#log_path = "80_delegate.log"
		#task_name ="80_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_C, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_081_delegate(self):
		#log_path = "81_delegate.log"
		#task_name ="81_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_082_delegate(self):
		#log_path = "82_delegate.log"
		#task_name ="82_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_083_delegate(self):
		#log_path = "83_delegate.log"
		#task_name ="83_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_A, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_084_delegate(self):
		#log_path = "84_delegate.log"
		#task_name ="84_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_C, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_085_delegate(self):
		#log_path = "85_delegate.log"
		#task_name ="85_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_D, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_086_delegate(self):
		#log_path = "86_delegate.log"
		#task_name ="86_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_087_delegate(self):
		#log_path = "87_delegate.log"
		#task_name ="87_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_INCORRECT_3, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_088_delegate(self):
		#log_path = "88_delegate.log"
		#task_name ="88_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_INCORRECT_1, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_089_delegate(self):
		#log_path = "89_delegate.log"
		#task_name ="89_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_090_delegate(self):
		#log_path = "90_delegate.log"
		#task_name ="90_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_INCORRECT_1, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_091_delegate(self):
		#log_path = "91_delegate.log"
		#task_name ="91_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_INCORRECT_2, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_092_delegate(self):
		#log_path = "92_delegate.log"
		#task_name ="92_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_INCORRECT_3, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_093_delegate(self):
		#log_path = "93_delegate.log"
		#task_name ="93_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_INCORRECT_4, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_094_delegate(self):
		#log_path = "94_delegate.log"
		#task_name ="94_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_INCORRECT_5, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_095_delegate(self):
		#log_path = "95_delegate.log"
		#task_name ="95_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_096_delegate(self):
		#log_path = "96_delegate.log"
		#task_name ="96_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_INCORRECT_1)		
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_097_delegate(self):
		#log_path = "97_delegate.log"
		#task_name ="97_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_INCORRECT_2)		
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_098_delegate(self):
		#log_path = "98_delegate.log"
		#task_name ="98_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_INCORRECT_3)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_099_delegate(self):
		#log_path = "99_delegate.log"
		#task_name ="99_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_INCORRECT_4)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_normal_100_delegate(self):
		#log_path = "100_delegate.log"
		#task_name ="100_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_101_delegate(self):
		#log_path = "101_delegate.log"
		#task_name ="101_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT, public_key=test_config.KEY_NO_1)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_102_delegate(self):
		#log_path = "102_delegate.log"
		#task_name ="102_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT, public_key=test_config.KEY_NO_2)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_103_delegate(self):
		#log_path = "103_delegate.log"
		#task_name ="103_delegate"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT, public_key=test_config.KEY_NO_3)		
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_104_withdraw(self):
		#log_path = "104_withdraw.log"
		#task_name ="104_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_abnormal_105_withdraw(self):
		#log_path = "105_withdraw.log"
		#task_name ="105_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_4, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_106_withdraw(self):
		#log_path = "106_withdraw.log"
		#task_name ="106_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_5, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_107_withdraw(self):
		#log_path = "107_withdraw.log"
		#task_name ="107_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_INCORRECT_6, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_108_withdraw(self):
		#log_path = "108_withdraw.log"
		#task_name ="108_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_109_withdraw(self):
		#log_path = "109_withdraw.log"
		#task_name ="109_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_B, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_110_withdraw(self):
		#log_path = "110_withdraw.log"
		#task_name ="110_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_111_withdraw(self):
		#log_path = "111_withdraw.log"
		#task_name ="111_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_C, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_112_withdraw(self):
		#log_path = "112_withdraw.log"
		#task_name ="112_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_D, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_113_withdraw(self):
		#log_path = "113_withdraw.log"
		#task_name ="113_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_114_withdraw(self):
		#log_path = "114_withdraw.log"
		#task_name ="114_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_A, test_config.ROLE_CORRECT)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_115_withdraw(self):
		#log_path = "115_withdraw.log"
		#task_name ="115_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_A, test_config.ROLE_CORRECT)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_116_withdraw(self):
		#log_path = "116_withdraw.log"
		#task_name ="116_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_A, test_config.ROLE_CORRECT)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_117_withdraw(self):
		#log_path = "117_withdraw.log"
		#task_name ="117_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_C, test_config.ROLE_CORRECT)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_118_withdraw(self):
		#log_path = "118_withdraw.log"
		#task_name ="118_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_D, test_config.ROLE_CORRECT)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_119_withdraw(self):
		#log_path = "119_withdraw.log"
		#task_name ="119_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_120_withdraw(self):
		#log_path = "120_withdraw.log"
		#task_name ="120_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_INCORRECT_3)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_121_withdraw(self):
		#log_path = "121_withdraw.log"
		#task_name ="121_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_INCORRECT_2)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_122_withdraw(self):
		#log_path = "122_withdraw.log"
		#task_name ="122_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_INCORRECT_1)
			process = (response["result"]["Result"] == "00")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	
	def test_normal_134_withdraw(self):
		#log_path = "134_withdraw.log"
		#task_name ="134_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_135_withdraw(self):
		#log_path = "135_withdraw.log"
		#task_name ="135_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, public_key=test_config.KEY_NO_1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_136_withdraw(self):
		#log_path = "136_withdraw.log"
		#task_name ="136_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, public_key=test_config.KEY_NO_2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_137_withdraw(self):
		#log_path = "137_withdraw.log"
		#task_name ="137_withdraw"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = bind_role_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.FUNCTION_A])
			(process, response) = bind_user_role( test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ROLE_CORRECT, [test_config.ontID_A])
			(process, response) = delegate_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, test_config.PERIOD_CORRECT, test_config.LEVEL_CORRECT)
			(process, response) = withdraw_user_role(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A, test_config.ontID_B, test_config.ROLE_CORRECT, public_key=test_config.KEY_NO_3)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_base_138_appcall(self):
		#log_path = "138_appcall.log"
		#task_name ="138_appcall"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_138, "contractA_Func_A", test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_139_appcall(self):
		#log_path = "139_appcall.log"
		#task_name ="139_appcall"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_139, "contractA_Func_A", test_config.ontID_A)
			process = (response["result"]["Result"] == "323232")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	
	
	def test_abnormal_140_appcall(self):
		#log_path = "140_appcall.log"
		#task_name ="140_appcall"
		try:
			init_admin(test_config.CONTRACT_ADDRESS_CORRECT, test_config.ontID_A)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, "contractA_Func_A", test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	
	def test_base_146_verifyToken(self):
		#log_path = "146_verifyToken.log"
		#task_name ="146_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_A)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_147_verifyToken(self):
		#log_path = "147_verifyToken.log"
		#task_name ="147_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_A, public_key=test_config.KEY_NO_1)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_148_verifyToken(self):
		#log_path = "148_verifyToken.log"
		#task_name ="148_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_A, public_key=test_config.KEY_NO_2)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_149_verifyToken(self):
		#log_path = "149_verifyToken.log"
		#task_name ="149_verifyToken"
		try:
			init(register_ontid = True, restart = True)
			(process, response) = invoke_function(test_config.CONTRACT_ADDRESS_CORRECT, test_config.FUNCTION_A, test_config.ontID_A, public_key=test_config.KEY_NO_3)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
	

####################################################
if __name__ == '__main__':
	unittest.main()
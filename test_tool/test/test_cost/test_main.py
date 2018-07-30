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

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API
from test_cost.test_config import test_config

#test cases
class test_cost_1(ParametrizedTestCase):
	def setUp(self):
		logger.open("test_auth/" + self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.result())

	def test_base_001_rpcapiTest(self):
		priceTest=20000
		try:
			(process1, response)= API.rpc().getbalance(test_config.address)
			print(process1)
			print(response["result"])
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
			
			ontract_address = API.contract().deploy_contract(test_config.cost1,price=priceTest)
			(process1, response)= API.rpc().getbalance(test_config.address)
			ong2=int(response["result"]["ong"])
			ont2=response["result"]["ont"]
			
			print(ong1-ong2==(priceTest*1000000000))
			print(priceTest*1000000000)
			print(ong1-ong2)
			
			if(ong1-ong2==(priceTest*1000000000)):
				process=True
			else:
				process=False
			#print(ong,ont)
			#self.finish(task_name, log_path, result,  "")\
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])
		
	def test_normal_004_rpcapiTest(self):
		priceTest=366780
		try:
			(process1, response)= API.rpc().getbalance(test_config.address)
			
			print(process1)
			print(response["result"])
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
			task=Task(test_config.filterfile)
			(process, response) = API.contract().call_contract(task,pre=False)
			
			(process1, response)= API.rpc().getbalance(test_config.address)
			ong2=int(response["result"]["ong"])
			ont2=response["result"]["ont"]
			
			print(ong1-ong2==(priceTest))
			print(priceTest)
			print(ong1-ong2)
			
			if(ong1-ong2==(priceTest)):
				process=True
			else:
				process=False
			self.ASSERT(process, "")
		except Exception as e:
			logger.print(e.args[0])

####################################################
if __name__ == '__main__':
	unittest.main()


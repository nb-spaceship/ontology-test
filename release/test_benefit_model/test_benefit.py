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
from test_api import *

from utils.commonapi import *
from utils.rpcapi import RPCApi

logger = LoggerInstance

CONTRACT_ADDRESS = ""
####################################################
# test cases
rpcapi = RPCApi()

priceTest = 100000

class TestBenefit(ParametrizedTestCase):
	def test_1(self):
		address = Config.SERVICES[0]["address"]
		logger.open("TestBenefit1.log", "TestBenefit1")
		result = False
		try:
			(result1, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
		
			contract_address = deploy_contract("contract.neo", price=priceTest)
			(result1, response) = rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
				
			ong2 = int(response["result"]["ong"])
			ont2 = response["result"]["ont"]
			
			print(ong1-ong2==(priceTest*1000000000))
			print(priceTest*1000000000)
			print(ong1-ong2)
			if(ong1-ong2==(priceTest*1000000000)):
				result=True
			else:
				result=False

		except Exception as e:
			print(e.msg)
		logger.close(result)

		
	def test_3(self):
		address = Config.SERVICES[0]["address"]
		logger.open("TestBenefit1.log", "TestBenefit1")
		result = False
		try:
			(result1, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
		
			contract_address = deploy_contract("contract.neo", price=999999999999999)
			(result1, response) = rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
				
			ong2 = int(response["result"]["ong"])
			ont2 = response["result"]["ont"]
			
			print(ong1-ong2==(priceTest*1000000000))
			print(priceTest*1000000000)
			print(ong1-ong2)
		
			if(ong1-ong2==(priceTest*1000000000)):
				result=True
			else:
				result=False

		except Exception as e:
			print(e.msg)
		logger.close(result)

	def test_7(self):
		address = Config.SERVICES[2]["address"]
		result = False
		logger.open("TestBenefit7.log", "TestBenefit7")
		try:
			invoke_function_update("updateGlobalParam","2000000000","10000","32","1","50","50","50","50")
			response = withdrawong(2)
			(result1, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]


			response = transfer_ont(0, 2, 1000)
			print (json.dumps(response))
			time.sleep(5)
			(result2, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong2=int(response["result"]["ong"])
			ont2=response["result"]["ont"]

			if ong1 == ong2:
				result = False
		
		except Exception as e:
			print(e.msg)
		logger.close(result)
		
####################################################
if __name__ == '__main__':
    unittest.main()

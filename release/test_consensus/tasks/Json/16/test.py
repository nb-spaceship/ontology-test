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
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.api.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

####################################################
#test cases
class Test3(ParametrizedTestCase):
	def test_main(self):
		logger.open("TestConsensus1.log", "TestConsensus1")
		try:
			#step 1
			task0 = Task("tasks/invoke_init.json")
			(result, response) = call_contract(task0)
			if not result:
				raise Error("error")
			
			#step 2
			task1 = Task("tasks/invoke_put.json")
			(result, response) = call_contract(task1)
			if not result:
				raise Error("error")

			#step 3
			if response['Result String"'] == "keytest":
				raise Error("key value can be getted")	
		except Exception as e:
			print(e.msg)
		logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	    

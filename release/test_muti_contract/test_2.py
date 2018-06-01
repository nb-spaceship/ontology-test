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
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

####################################################
#test cases
class TestSample1(ParametrizedTestCase):
	def test_main(self):
		logger.open("TestSample1.log")
		try:
			#step 1
			task1 = Task("tasks/invoke_init.json")
			(result, response) = call_contract(task1)
			if not result:
				raise Error("error")

			#step 2
			task2 = Task("tasks/role_A_have_func_A_C.json")
			(result, response) = call_contract(task2)
			if not result:
				raise Error("error")

			#step 3
			task3 = Task("tasks/role_B_have_func_B_C.json")
			(result, response) = call_contract(task3)
			if not result:
				raise Error("error")

			#step 4
			task4 = Task("tasks/user_A_become_role_A.json")
			(result, response) = call_contract(task4)
			if not result:
				raise Error("error")

			#step 5
			task5 = Task("tasks/user_A_invoke_func_C.json")
			(result, response) = call_contract(task4)
			if not result:
				raise Error("error")
		except Exception as e:
			print(e.msg)
		logger.close("TestSample1", result)

####################################################
if __name__ == '__main__':
	unittest.main()	    

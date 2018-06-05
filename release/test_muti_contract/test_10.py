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

####################################################
#test cases
class TestSample1(ParametrizedTestCase):
	def test_main(self):
		logger.open("TestSample1.log")
		try:
			#step 1 invoke_init
			task1 = Task("tasks/invoke_init.json")
			(result, response) = call_contract(task1)
			if not result:
				raise Error("invoke_init error")

			#step 2 role_A_have_func_A_C
			task2 = Task("tasks/role_A_have_func_A_C.json")
			(result, response) = call_contract(task2)
			if not result:
				raise Error("role_A_have_func_A_C error")

			#step 3 role_B_have_func_B_C
			task3 = Task("tasks/role_B_have_func_B_C.json")
			(result, response) = call_contract(task3)
			if not result:
				raise Error("role_B_have_func_B_C error")

			#step 4 user_A_bind_role_A
			task4 = Task("tasks/user_A_bind_role_A.json")
			(result, response) = call_contract(task4)
			if not result:
				raise Error("user_A_bind_role_A error")

			#step 5 user_A_delegate_role_A
			task5 = Task("tasks/user_A_delegate_role_A.json")
			(result, response) = call_contract(task5)
			if not result:
				raise Error("user_A_delegate_role_A error")
			
			time.sleep(10)

			#step 7 user_A_invoke_func_C
			task7 = Task("tasks/user_A_invoke_func_C.json")
			(result, response) = call_contract(task7)
			if not result:
				raise Error("user_A_invoke_func_C error")
				
		except Exception as e:
			print(e.msg)
		logger.close("TestSample1", result)

####################################################
if __name__ == '__main__':
	unittest.main()	    

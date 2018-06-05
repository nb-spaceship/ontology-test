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
			#step 1 初始化contractB的管理员
			task1 = Task("tasks/33/invoke_init.json")
			(result, response) = call_contract(task1)
			if not result:
				raise Error("invoke_init error")

			#step 2 user_A_invoke_func_A
			task2 = Task("tasks/33/user_A_invoke_func_A.json")
			(result, response) = call_contract(task2)
			if not result:
				raise Error("user_A_invoke_func_A error")		
				
		except Exception as e:
			print(e.msg)
		logger.close("TestSample1", result)

####################################################
if __name__ == '__main__':
	unittest.main()	    

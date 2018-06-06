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
			#step 1 初始化contractA的管理员为用户A
			task1 = Task("tasks/39/invoke_init.json")
			(result, response) = call_contract(task1)
			if not result:
				raise Error("invoke_init error")
			
			#step 2 管理员用户A创建角色A, 角色A拥有调用合约A中A方法的权限
			task2 = Task("tasks/39/role_A_have_func_A.json")
			(result, response) = call_contract(task2)
			if not result:
				raise Error("role_A_have_func_A error")


			#step 3 管理员用户A绑定角色A
			task3 = Task("tasks/39/user_A_bind_role_A.json")
			(result, response) = call_contract(task3)
			if not result:
				raise Error("user_A_invoke_func_A error")

			#step 4 用户A授权用户B拥有角色B, leven=1
			task4 = Task("tasks/39/user_A_delegate_role_B.json")
			(result, response) = call_contract(task4)
			if not result:
				raise Error("user_A_delegate_role_B.json error")

			#step 5 用户B调用智能合约A中的A方法
			task4 = Task("tasks/39/user_B_invoke_func_A.json")
			(result, response) = call_contract(task4)
			if not result:
				raise Error("user_B_invoke_func_A.json error")

		except Exception as e:
			print(e.msg)
		logger.close("TestSample1", result)

####################################################
if __name__ == '__main__':
	unittest.main()	    

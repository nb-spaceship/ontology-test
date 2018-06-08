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
from test_common import *
logger = LoggerInstance

####################################################
# test cases


class TestMutiContract_8(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_8.log", "TestMutiContract_8")
        result = False
        try:
            
            (contract_address, adminOntID, roleA_hex, roleB_hex, ontID_A, ontID_B, ontID_C) = set_premise("tasks/test_8.neo")

            # setp 1 绑定用户A拥有roleA角色
            (result, response) = bind_user_role(contract_address,adminOntID, roleA_hex, [ontID_A])
            if not result:
                raise("bind_user_role error")
			
			# setp 1 绑定用户B拥有roleB角色
            (result, response) = bind_user_role(contract_address,adminOntID, roleB_hex, [ontID_B])
            if not result:
                raise("bind_user_role error")
	
			# setp 1 用户B授权用户A拥有角色B的权限
            (result, response) = delegate_user_role(contract_address, ontID_B, ontID_A, roleB_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
			
			# setp 1 收回授权用户A拥有的roleB角色
            (result, response) = withdraw_user_role(contract_address, ontID_B, ontID_A, roleB_hex)
            if not result:
                raise("bind_user_role error")
                        
            # setp 2 用户A访问B函数
            (result, response) = invoke_function(contract_address, "B")
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
            logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()

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


class TestMutiContract_16(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_16.log", "TestMutiContract_16")
        result = False
        try:
            contract_address = set_premise("tasks/1-32/A.neo")

            # setp 1 绑定roleA角色绑定到用户A,B
            (result, response) = bind_user_role(contract_address,Common.ontID_A, Common.roleA_hex, [Common.ontID_A, Common.ontID_B])
            if not result:
                raise("bind_user_role error")
			
			# setp 2 用户A授权用户B拥有roleA角色
            (result, response) = delegate_user_role(contract_address, Common.ontID_A, Common.ontID_B, Common.roleA_hex, "10000", "1")
            if not result:
                raise("bind_user_role error")
			
			# setp 3 用户A收回用户B拥有的roleA角色，level1的授权
            (result, response) = withdraw_user_role(contract_address, Common.ontID_A, Common.ontID_B, Common.roleA_hex)
            if not result:
                raise("bind_user_role error")
            
            # setp 4 用户B访问A函数
            (result, response) = invoke_function(contract_address, "A", Common.ontID_B)
            if not result:
                raise Error("invoke_function error")
				
            result = (response["result"]["Result"] != "00")
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()

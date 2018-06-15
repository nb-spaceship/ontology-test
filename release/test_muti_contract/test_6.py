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


class TestMutiContract_6(ParametrizedTestCase):
    def test_main(self):
        roleA_hex = ByteToHex(b"rolexx6-3")
        roleB_hex = ByteToHex(b"roleXxx6-3")
        logger.open("TestMutiContract_6.log", "TestMutiContract_6")
        result = False
        try:
            contract_address = "c49ae2606bb0bc2cb9dea8ad2847c952d2a24124"#set_premise("tasks/test_6.neo", roleA_hex, roleB_hex)

            # setp 1 绑定roleA角色绑定到用户A
            #(result, response) = bind_user_role(contract_address, Common.ontID_Admin, roleA_hex, [Common.ontID_A])
            #if not result:
            #    raise("bind_user_role error")
			
			# setp 1 绑定roleB角色绑定到用户B
            #(result, response) = bind_user_role(contract_address, Common.ontID_Admin, roleB_hex, [Common.ontID_B])
            #if not result:
            #    raise("bind_user_role error")
			
			# setp 1 用户B授权用户A拥有角色B的权限
            #(result, response) = delegate_user_role(contract_address, Common.ontID_B, Common.ontID_A, roleB_hex, "5", "1", node_index = Common.node_B)
            #if not result:
            #    raise("bind_user_role error")
            
            #print("wait.......10s")
            #time.sleep(10)            

            # setp 2 用户A访问B函数
            (result, response) = invoke_function(contract_address, "B", Common.ontID_A, node_index = Common.node_A)
            if not result:
                raise Error("invoke_function error")
        
        except Exception as e:
            print(e.msg)
            logger.close(result)
    
####################################################
if __name__ == '__main__':
    unittest.main()

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
from test_conf import Conf

logger = LoggerInstance

####################################################
# test cases
class TestMutiContract_47(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_47.log", "TestMutiContract_47")
        result = False
        try:
            (contract_addressA, contract_addressB) = set_premise_c("tasks/44-47/A.neo", "tasks/44-47/B.neo")

			# setp 1 用户A授权用户B调用方法A的权限
            #(result, response) = delegate_user_role(contract_addressA, Common.ontID_A, Common.ontID_B, Common.roleA_hex, "10000", "1")
            #if not result:
            #    raise("bind_user_role error")  

            # 用户B调用智能合约A中的A方法
            (result, response) = invoke_function(contract_addressA, "A2", Common.ontID_B)

            result = (not result or response["result"]["Result"] == "00")        
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    
    
####################################################
if __name__ == '__main__':
    unittest.main()


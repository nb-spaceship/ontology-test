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
class TestMutiContract_58(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_58.log", "TestMutiContract_58")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")
	
            # 用户B调用智能合约A中的A方法查询用户A的账户ont余额
            (result, response) = invoke_function(contract_address, "balanceOf_ong", Common.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_A]["address"]))
																				}])
            result = (result and response["result"]["Result"] != "00")    

        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    
    
####################################################
if __name__ == '__main__':
    unittest.main()


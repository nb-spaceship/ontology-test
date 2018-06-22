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
class TestMutiContract_52(ParametrizedTestCase):
    def test_main(self):
        logger.open("TestMutiContract_52.log", "TestMutiContract_52")
        result = False
        try:
            contract_address = deploy_contract("tasks/38-43_48-59/A2.neo")

            # 用户A调用智能合约A中的A方法approve用户A给用户C 10 ont
            (result, response) = invoke_function(contract_address, "approve", Common.ontID_A, argvs = [ {
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
            if not result:
                raise Error("invoke_function error")			
			

            # 用户B调用智能合约A中的A方法提取用户A给用户C的10 ont
            (result, response) = invoke_function(contract_address, "transferFrom", Common.ontID_B, argvs = [ {
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_B]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_A]["address"]))
																				},
																				{
																					"type": "bytearray",
																					"value": script_hash_bl_reserver(base58_to_address(Config.SERVICES[Common.node_C]["address"]))
																				},
																				{
																					"type": "int",
																					"value": "10"
																				}])
            result = (not result or response["result"]["Result"] == "00")    
        
        except Exception as e:
            print(e.msg)
        logger.close(result)
    
    
####################################################
if __name__ == '__main__':
    unittest.main()


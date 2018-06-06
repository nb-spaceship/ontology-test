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

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *

logger = LoggerInstance

####################################################
# test cases


class TestMutiContract_1(ParametrizedTestCase):
    def test_main(self):
		logger.open("TestMutiContract_1.log", "TestMutiContract_1")
		result = False

        try:
            admin_address = "xxxxxxxxx"
            contract_address = None

            # deploy
            task1 = Task("tasks/test_1.json")
            contract_address = deploy_contract(task1)

            # step 1 invoke_init
            (result, response) = init_admin(contract_address, admin_address)
            if not result:
                raise("init_admin error")

            # step 2 role_A_have_func_A_C
            (result, response) = bind_role_function(
                contract_address, admin_address, "roleA", ["A", "C"])
            if not result:
                raise("bind_role_function error [1]")

            (result, response) = bind_role_function(
                contract_address, admin_address, "roleB", ["B", "C"])
            if not result:
                raise("bind_role_function error [2]")

            (result, response) = bind_user_role(contract_address,
                                                admin_address, "roleA", ["TA6CtF4hZwqAmXdc6opa4B79fRS17YJjX5"])
            if not result:
                raise("bind_user_role error")

            (result, response) = invoke_function(contract_address, "A")
            if not result:
                raise Error("invoke_function error")

        except Exception as e:
            print(e.msg)
        logger.close(result)


####################################################
if __name__ == '__main__':
    unittest.main()

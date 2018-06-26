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
from test_api import *


CONTRACT_ADDRESS = "92ed1b65d9549ce4a083af0dc83862fcba03d5c3"

ADDRESS_A = "da14e05b077d6147e487a4774455a57873fd07d0"  #"AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN"
ADDRESS_B = "24b453d1388732a9d78228b572e05f7a082b90a9" #"AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X"
ADDRESS_C = "e3462e4422c6317a93604fef74255117ed2b5328"
AMOUNT = "1000"
PUBLIC_KEY = "02b59d88bc4b2f5814b691d32e736bcd7ad018794f041235092f6954e23198cbcf"
PUBLIC_KEY_2 = "03e05d01e5df2c85e6a9a5526c70d080b6c7dce0fa7c66f8489c18b8569dc269dc"
PUBLIC_KEY_3 = "02f59dbaf056dedfbdc2fedd2cf700a585df1acdd777561d65ba484b5f519287ef"
PUBLIC_KEY_4 = "0354fe669e9df891698ef8c4cbc9e3fbfa503ee93e237e1b38d3e3e4c7869886ee"

#test cases
class TestConsensus(ParametrizedTestCase):
    def start(self, log_path):
        logger.open(log_path)

    def finish(self, task_name, log_path, result, msg):
        if result:
            logger.print("[ OK       ] ")
            logger.append_record(task_name, "pass", log_path)
        else:
            logger.print("[ Failed   ] " + msg)
            logger.append_record(task_name, "fail", log_path)
        logger.close()

    def test_19_consensus(self):
        log_path = "19_consensus.log"
        task_name = "19_consensus"
        self.start(log_path)
        (result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT)
        self.finish(task_name, log_path, result,  "")
        
    def test_20_consensus(self):
        log_path = "20_consensus.log"
        task_name = "20_consensus"
        self.start(log_path)
        (result, response) = transfer_20(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY)
        self.finish(task_name, log_path, result,  "")

    def test_21_consensus(self):
        log_path = "21_consensus.log"
        task_name = "21_consensus"
        self.start(log_path)
        (result, response) = transfer_21(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY)
        self.finish(task_name, log_path, result,  "")

    def test_22_consensus(self):
        log_path = "22_consensus.log"
        task_name = "22_consensus"
        self.start(log_path)
        (result, response) = transfer_22(CONTRACT_ADDRESS, ADDRESS_C, ADDRESS_B, AMOUNT, PUBLIC_KEY)
        self.finish(task_name, log_path, result,  "")

    def test_23_consensus(self):
        log_path = "23_consensus.log"
        task_name = "23_consensus"
        self.start(log_path)
        (result, response) = transfer_23(CONTRACT_ADDRESS, ADDRESS_C, ADDRESS_B, AMOUNT, PUBLIC_KEY)
        self.finish(task_name, log_path, result,  "")

    def test_24_consensus(self):
        log_path = "24_consensus.log"
        task_name = "24_consensus"
        self.start(log_path)
        (result, response) = transfer_24(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY, PUBLIC_KEY_2, PUBLIC_KEY_3, PUBLIC_KEY_4)
        self.finish(task_name, log_path, result,  "")

    def test_25_consensus(self):
        log_path = "25_consensus.log"
        task_name = "25_consensus"
        self.start(log_path)
        (result, response) = transfer_25(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT, PUBLIC_KEY, PUBLIC_KEY_2, PUBLIC_KEY_3, PUBLIC_KEY_4)
        self.finish(task_name, log_path, result,  "")

    def test_30_consensus(self):
        log_path = "30_consensus.log"
        task_name = "30_consensus"
        self.start(log_path)
        (result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT)
        (result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_C, AMOUNT)
        self.finish(task_name, log_path, result,  "")

    def test_31_consensus(self):
        log_path = "31_consensus.log"
        task_name = "31_consensus"
        self.start(log_path)
        (result, response) = approve_31(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", AMOUNT)
        (result, response) = approve_31(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AcVb7HZB4nMDscQHXXoqKvnNFwrpL3V1u3", AMOUNT)
        (result, response) = allowance(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", AMOUNT)
        (result, response) = allowance(CONTRACT_ADDRESS, "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", "AcVb7HZB4nMDscQHXXoqKvnNFwrpL3V1u3", AMOUNT)
        self.finish(task_name, log_path, result,  "")

    def test_32_consensus(self):
        log_path = "32_consensus.log"
        task_name = "32_consensus"
        self.start(log_path)
        (result, response) = approve_32(CONTRACT_ADDRESS, "AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN", AMOUNT)
        (result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_B, AMOUNT)
        (result, response) = transfer_19(CONTRACT_ADDRESS, ADDRESS_A, ADDRESS_C, AMOUNT)
        (result, response) = allowance_32("AK7wzmkdgjKxbXAJBiaW91YhUokTu9pa5X", "AbeyxqLpm3GZDVJdRP62raMfCmHxsDfKDN")
        self.finish(task_name, log_path, result,  "")

    


if __name__ == '__main__':
    unittest.main()

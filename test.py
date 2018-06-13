# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.restfulapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

####################################################
#test cases
class Test(ParametrizedTestCase):
    def test_07_get_blk_txs_by_height(self,height=1):
        logger.open("07_get_blk_txs_by_height.log", "07_get_blk_txs_by_height")
        (result, response) = RestfulApi().getblocktxsbyheight(height)
        logger.close(result)

####################################################
if __name__ == '__main__':
	unittest.main()	
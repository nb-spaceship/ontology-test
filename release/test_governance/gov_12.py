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
from utils.api.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *

####################################################
#test cases
class TestConsensus(ParametrizedTestCase):

	def test_main(self):
		result = False
		logger.open("TestGover12.log", "TestGover12")
		try:
			if (not pause("ensure that node A and node B is in the nodes network and node A has more than 10000 ont.")):
				raise Error("pre-condition unsatisfied")

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			'''
			# to ensure that the following operations are in the same round			
			while(True):
				if getblockcount() % blocks_per_round <= 2:
					time.sleep(1)
					continue
				else:
					break
			'''
			# step 1 wallet A vote for node B
			(result, response) = vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price])
			print (response)
			#if not result:
			#	raise Error("vote error")

			# step 2 black node b 
			if (not pause("black node over?")):
				pass
			#if not result:
			#	raise Error("black_node error")

			# step 3 withdraw ont
			(result, response) = withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price])
			#if not result:
			#	raise Error("withdraw_ont error")

			# this should be failed
			(result, response) = withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"])
			#if not result:
			#	raise Error("withdraw_ont error")

		
		except Exception as e:
			print(e.msg)
		logger.close(result)
####################################################
if __name__ == '__main__':
	unittest.main()	    
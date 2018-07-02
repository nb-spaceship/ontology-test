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
from utils.commonapi import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from test_api import *
from test_common import *
#from test_conf import Conf

logger = LoggerInstance



##########################################################
# params
nodeNow=7
nodeOthers=6
pubKey_pre = Config.NODES[7]["pubkey"] #准备用
walletAddress_pre= Config.NODES[7]["address"]
ontCount_1="10000"
ontID_1=ByteToHex((Config.NODES[7]["ontid"]).encode("utf-8"))
user_1 = "1" #正常的公钥序号

walletAddress_1 = Config.NODES[nodeNow]["address"] #自己的钱包地址
walletNode_1=nodeNow
walletAddress_2 = "AYcJKK6Bxhq7H6J9fmdAVmiESi6XjRZHAE" #其他人的钱包地址
walletNode_2=nodeOthers
walletAddress_3 = "abcd1234" #乱码
walletAddress_4 = "" #留空
voteList_1 = [Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"]]#已经在网络中的共识节点公钥数组
voteList_2 = [Config.NODES[7]["pubkey"]] #已经在网络中的候选节点公钥数组
voteList_2_count=["100"]
voteList_3 = ["141923c71f012b99280229e5225267ba22e50e61cba9f2d713fe785080c1733f0877"] #未申请的节点公钥数组
voteList_4 = [Config.NODES[7]["pubkey"]] #已经申请的节点公钥数组
voteList_5 = ["abcd1234"] #乱码
voteList_6 = [""] #留空
voteCount_1 = ["100","100"] #与公钥数组一一对应的不同票数的数组，数组总值低于钱包内存在的ont数量
voteCount_2 = ["10000000000","100"] #与公钥数组一一对应的不同票数的数组，数组总值高于钱包内存在的ont数量
voteCount_3 = ["100"] #比公钥数组数量少的票数数组
voteCount_4 = ["qwer","100"] #乱码
voteCount_5 = ["",""] #留空
####################################################

# test cases
class TestVoteForPeer(ParametrizedTestCase):
	def setUp(self):
		#restart all node
		init( candidate=True, register_ontid=True, restart=True, pub_key="1", ont_count="10000")
		time.sleep(10)
		
		
		# register ONTID
	def test(self):
		pass
	def test_48_VoteForPeer(self):
		logger.open("48_VoteForPeer.log", "48_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1,0,walletNode_1)
		time.sleep(2)
		nodeCountCheck(response,7)
		logger.close(result)

	def test_49_VoteForPeer(self):
		logger.open("49_VoteForPeer.log", "49_VoteForPeer")
		(result, response) = native_transfer(walletAddress_1,walletAddress_2,500,node_index=walletNode_1,errorcode=0)
		if result:
			time.sleep(10)
			(result, response) = invoke_function_vote("voteForPeer",walletAddress_2,voteList_1,voteCount_1,node_index=walletNode_1)
			time.sleep(2)
			nodeCountCheck(response,7)
		logger.close(result)
	
	def test_50_VoteForPeer(self):
		logger.open("50_VoteForPeer.log", "50_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_3,voteList_1,voteCount_1)

		logger.close(result)
	def test_51_VoteForPeer(self):
		logger.open("51_VoteForPeer.log", "51_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_4,voteList_1,voteCount_1)

		logger.close(result)
	
	def test_52_VoteForPeer(self):
		logger.open("52_VoteForPeer.log", "52_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1,0,walletNode_1)

		logger.close(result)
	
	def test_53_VoteForPeer(self):
		logger.open("53_VoteForPeer.log", "53_VoteForPeer")
		(result, response) = invoke_function_register("registerCandidate",pubKey_pre,walletAddress_pre,ontCount_1,ontID_1,user_1,0)
		time.sleep(15)
		(result, response) = invoke_function_candidate("approveCandidate",pubKey_pre,0)
		time.sleep(15)
		if result:
			(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_2,voteList_2_count,0,node_index=walletNode_1)
			time.sleep(2)
			nodeCountCheck(response,7)
		logger.close(result)

	def test_54_VoteForPeer(self):
		logger.open("54_VoteForPeer.log", "54_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_3,voteList_2_count,node_index=walletNode_1)

		logger.close(result)

	def test_55_VoteForPeer(self):
		logger.open("55_VoteForPeer.log", "55_VoteForPeer")
		(result, response) = invoke_function_register("registerCandidate",pubKey_pre,walletAddress_pre,ontCount_1,ontID_1,user_1,0)
		if result:
			time.sleep(15)
			(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_4,voteList_2_count,node_index=walletNode_1)
			time.sleep(2)
			nodeCountCheck(response,7)
		logger.close(result)

	def test_56_VoteForPeer(self):
		logger.open("56_VoteForPeer.log", "56_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_5,voteList_2_count,node_index=walletNode_1)

		logger.close(result)

	def test_57_VoteForPeer(self):
		logger.open("57_VoteForPeer.log", "57_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_6,voteList_2_count,node_index=walletNode_1)

		logger.close(result)
	
	def test_58_VoteForPeer(self):
		logger.open("58_VoteForPeer.log", "58_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_1,0,node_index=walletNode_1)

		logger.close(result)
	
	def test_59_VoteForPeer(self):
		logger.open("59_VoteForPeer.log", "59_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_2,node_index=walletNode_1)

		logger.close(result)
	
	def test_60_VoteForPeer(self):
		logger.open("60_VoteForPeer.log", "60_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_3,node_index=walletNode_1)

		logger.close(result)
	
	def test_61_VoteForPeer(self):
		logger.open("61_VoteForPeer.log", "61_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_4,node_index=walletNode_1)

		logger.close(result)
	
	def test_62_VoteForPeer(self):
		logger.open("62_VoteForPeer.log", "62_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_1,voteCount_5,node_index=walletNode_1)

		logger.close(result)
	
	def test_63_VoteForPeer(self):
		logger.open("63_VoteForPeer.log", "63_VoteForPeer")
		(result, response) = invoke_function_vote("voteForPeer",walletAddress_1,voteList_6,voteCount_5,node_index=walletNode_1)

		logger.close(result)
	
####################################################
if __name__ == '__main__':
	unittest.main()
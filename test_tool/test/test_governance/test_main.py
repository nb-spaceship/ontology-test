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
sys.path.append('../..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.taskrunner import TaskRunner
from api.apimanager import API

from test_api import get_config

####################################################
#test cases
class test_governance_1(ParametrizedTestCase):
    
	def setUp(self):
		logger.open("test_governance/" + self._testMethodName+".log",self._testMethodName)
		time.sleep(2)
		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)

		API.native().regid_with_publickey(0)
		API.native().regid_with_publickey(1)
		API.native().regid_with_publickey(2)
		API.native().regid_with_publickey(3)
		API.native().regid_with_publickey(4)
		API.native().regid_with_publickey(5)
		API.native().regid_with_publickey(6)
		API.native().regid_with_publickey(7)
		API.native().regid_with_publickey(8)
		
		API.native().init_ont_ong()
		time.sleep(5)
		
		API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000000", 0)
		API.native().transfer_ong(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000000000000", 0)
		API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000000", 0)
		API.native().transfer_ong(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000000000000", 0)

		try:
			print("--------", Config.NODES[0]["ontid"])
			# create role and bind ONTID with role
			(process, response) = API.native().bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
			if not process:
				raise Error("bind_role_function error")

			(process, response) = API.native().bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8"))])
			if not process:
				raise Error("bind_user_role error")

			(process, response) = API.native().register_candidate(Config.NODES[7]["pubkey"], Config.NODES[7]["address"] ,"10000", ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8")), "1", 7)
			if not process:
				raise Error("register_candidate error")

			(process, response) = API.native().approve_candidate(Config.NODES[7]["pubkey"])
			if not process:
				raise Error("approve_candidate error")
			time.sleep(10)
			
		except Exception as e:
			print(e.args)
			
	def tearDown(self):
		logger.close(self.result())
	
	def test_base_001_gover(self):
		process = False

		try:

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

			# step 1 before vote get balance of wallet A B
			print("*******", API.rpc().getbalance(wallet_A_address))
			balance_of_wallet_A_1 = int(API.rpc().getbalance(wallet_A_address)[1]["result"]["ont"]) 
			balance_of_wallet_B_1 = int(API.rpc().getbalance(wallet_B_address)[1]["result"]["ont"]) 

			# step 2 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			time.sleep(10)

			# step 3 after vote get balance of wallet A B
			balance_of_wallet_A_2 = int(API.rpc().getbalance(wallet_A_address)[1]["result"]["ont"]) 
			balance_of_wallet_B_2 = int(API.rpc().getbalance(wallet_B_address)[1]["result"]["ont"]) 

			# step 4 compare
			self.ASSERT(balance_of_wallet_B_1 == balance_of_wallet_B_2, "balance of wallte B changed.")

			self.ASSERT(balance_of_wallet_A_1 - balance_of_wallet_A_2 == int(vote_price), "the decrease of balance of wallet A is not %s." % vote_price)

		except Exception as e:
			print(e.args)
	

	def test_normal_002_gover(self):
		process = False
		try:
			
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			
			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")
			
			# step 2 wallet A unvote in the same round
			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")
						
			time.sleep(5)
			# step 3 wallet A withdraw ont
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")

			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")
			
		except Exception as e:
			print(e.args)

	def test_normal_003_gover(self):
		process = False
		try:

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 wallet A unvote in the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")

			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")


		except Exception as e:
			print(e.args)

	def test_normal_004_gover(self):
		process = False
		try:

			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			vote_price = "20000"

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 wallet A unvote in the second round
			API.native().commit_dpos()
			time.sleep(5)
			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(not process, "withdraw_ont error")

			# step 4 wallet A withdraw ont in the forth round
			API.native().commit_dpos()
			time.sleep(5)
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")

			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)


	def test_normal_015_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()		
			
			API.native().update_global_param("2000000000","10000","32","10","50","50","50","50")

			time.sleep(15)
			
			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(Config.NODES[8]["address"], [node_B_puiblic_key], ["90000"], 8)
			self.ASSERT(process, "vote_for_peer error")
			
			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], ["10000"])
			self.ASSERT(process, "vote_for_peer error")

		except Exception as e:
			print(e.args)


	def test_abnormal_016_gover(self):
		process = False

		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()		

			API.native().update_global_param("2000000000","10000","32","10","50","50","50","50")

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(Config.NODES[8]["address"], [node_B_puiblic_key], ["90000"], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], ["10001"])
			self.ASSERT(not process, "vote_for_peer error")

		except Exception as e:
			print(e.args)


	def test_normal_017_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()		

			API.native().update_global_param("2000000000","10000","32","10","50","50","50","50")

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(Config.NODES[8]["address"], [node_B_puiblic_key], ["90000"], 0)
			self.ASSERT(process, "vote_for_peer error")

			(process, response) = API.native().unvote_for_peer(Config.NODES[8]["address"], [node_B_puiblic_key], ["10000"], 0)
			self.ASSERT(process, "unvote_for_peer error")

			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], ["10001"], 8)
			self.ASSERT(process, "vote_for_peer error")

			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(Config.NODES[8]["address"], [node_B_puiblic_key], ["10000"], 0)
			self.ASSERT(process, "withdraw_ont error")

			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], ["1000"], 8)
			self.ASSERT(process, "vote_for_peer error")
		except Exception as e:
			print(e.args)


class test_governance_2(ParametrizedTestCase):

	def setUp(self):
		logger.open("test_governance/" + self._testMethodName + ".log",self._testMethodName)
		time.sleep(2)
		print("stop all")
		API.node().stop_all_nodes()
		print("start all")
		API.node().start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)

		API.native().regid_with_publickey(0)
		API.native().regid_with_publickey(1)
		API.native().regid_with_publickey(2)
		API.native().regid_with_publickey(3)
		API.native().regid_with_publickey(4)
		API.native().regid_with_publickey(5)
		API.native().regid_with_publickey(6)
		API.native().regid_with_publickey(7)
		API.native().regid_with_publickey(8)
		
		API.native().init_ont_ong()
		time.sleep(5)
		
		API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000000", 0)
		API.native().transfer_ong(Config.NODES[0]["address"], Config.NODES[7]["address"], "1000000000000", 0)
		API.native().transfer_ont(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000000", 0)
		API.native().transfer_ong(Config.NODES[0]["address"], Config.NODES[8]["address"], "1000000000000", 0)
		try:
			# create role and bind ONTID with role
			(process, response) = API.native().bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
			if not process:
				raise Error("bind_role_function error")

			(process, response) = API.native().bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8"))])
			if not process:
				raise Error("bind_user_role error")

			(process, response) = API.native().bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[8]["ontid"], encoding = "utf8"))])
			if not process:
				raise Error("bind_user_role error")

			(process, response) = API.native().register_candidate(Config.NODES[7]["pubkey"], Config.NODES[7]["address"] ,"10000", ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8")), "1", 7)
			if not process:
				raise Error("register_candidate error")
			
			(process, response) = API.native().approve_candidate(Config.NODES[7]["pubkey"])
			if not process:
				raise Error("approve_candidate error")

			(process, response) = API.native().register_candidate(Config.NODES[8]["pubkey"], Config.NODES[8]["address"] ,"10000", ByteToHex(bytes(Config.NODES[8]["ontid"], encoding = "utf8")), "1", 8)
			if not process:
				raise Error("register_candidate error")
			
			(process, response) = API.native().approve_candidate(Config.NODES[8]["pubkey"])
			if not process:
				raise Error("invoke_function_aapprove_candidatepprove error")
				
			time.sleep(10)
		except Exception as e:
			print(e.args)
			
	def tearDown(self):
		logger.close(self.result())

	def test_normal_005_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

			# step 1 before vote get balance of wallet A B
			balance_of_wallet_A_1 = int(API.rpc().getbalance(wallet_A_address)[1]["result"]["ont"]) 
			balance_of_wallet_B_1 = int(API.rpc().getbalance(wallet_B_address)[1]["result"]["ont"]) 

			# step 2 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 3 after vote get balance of wallet A
			balance_of_wallet_A_2 = int(API.rpc().getbalance(wallet_A_address)[1]["result"]["ont"]) 
			balance_of_wallet_B_2 = int(API.rpc().getbalance(wallet_B_address)[1]["result"]["ont"]) 

			# step 4 compare
			self.ASSERT(balance_of_wallet_B_1 == balance_of_wallet_B_2, "balance of wallte B changed.")

			self.ASSERT(balance_of_wallet_A_1 - balance_of_wallet_A_2 == int(vote_price), "the decrease of balance of wallet A is not %s." % vote_price)

		except Exception as e:
			print(e.args)
		self.ASSERT(process, "")


	def test_normal_006_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 wallet A unvote in the same round
			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 3 wallet A withdraw ont
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")
			
			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"])
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)


	def test_normal_007_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			
			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 wallet A unvote in the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price])
			self.ASSERT(process, "withdraw_ont error")

			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)


	def test_normal_008_gover(self):
		process = False

		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 wallet A unvote in the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")

			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)


	def test_normal_009_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			
			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 node b quit
			(process, response) = API.native().quit_node(node_B_puiblic_key, wallet_B_address, 7)
			self.ASSERT(process, "quit_node error")

			# step 2 wait until the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(not process, "withdraw_ont error")

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")
			
			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)

	def test_normal_010_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 wait until the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().quit_node(node_B_puiblic_key, wallet_B_address, 7)
			self.ASSERT(process, "quit_node error")
			
			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(not process, "withdraw_ont error")

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")
			
			# step 3 wallet A withdraw ont in the forth round
			API.native().commit_dpos()
			time.sleep(5)
			
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")
			
		except Exception as e:
			print(e.args)

	def test_normal_011_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			vote_price = "20000"

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 wait until the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().quit_node(node_B_puiblic_key, wallet_B_address, 7)
			self.ASSERT(process, "quit_node error")
			
			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(not process, "withdraw_ont error")

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 3 wallet A withdraw ont in the fifth round
			API.native().commit_dpos()
			time.sleep(5)

			API.native().commit_dpos()
			time.sleep(5)
			
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")

			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)


	def test_normal_012_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			
			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")

			# step 2 black node b 
			(process, response) = API.native().black_node([node_B_puiblic_key])
			self.ASSERT(process, "black_node error")

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			API.native().commit_dpos()
			time.sleep(5)

			# step 3 withdraw ont
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "withdraw_ont error")
			
			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1000"], 8)
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)


	def test_normal_013_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()
			API.native().update_global_param("2000000000","10000","32","1","50","50","50","50")

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")
			
			# step 2 wait until the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().black_node([node_B_puiblic_key])
			self.ASSERT(process, "black_node error")
			
			# step 3 wallet A withdraw ont in the third round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(not process, "withdraw_ont error")

			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 4 wallet A withdraw ont in the forth round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [str(int(punish_ratio*3000))], 8)	
			self.ASSERT(process, "withdraw_ont error")
			
			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")

		except Exception as e:
			print(e.args)


	def test_normal_014_gover(self):
		process = False
		try:
			(wallet_A_address, wallet_B_address, vote_price, node_B_puiblic_key, blocks_per_round, punish_ratio) = get_config()			
			API.native().update_global_param("2000000000","10000","32","1","50","50","50","50")

			# step 1 wallet A vote for node B
			(process, response) = API.native().vote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "vote_for_peer error")
			
			# step 2 wait until the second round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().black_node([node_B_puiblic_key])
			self.ASSERT(process, "black_node error")

			# step 3 wallet A withdraw ont in the third round
			# should failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(not process, "withdraw_ont error")
			
			(process, response) = API.native().unvote_for_peer(wallet_A_address, [node_B_puiblic_key], [vote_price], 8)
			self.ASSERT(process, "unvote_for_peer error")

			# step 4 wallet A withdraw ont in the forth round
			API.native().commit_dpos()
			time.sleep(5)

			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], [str(int(punish_ratio*3000))], 8)
			self.ASSERT(process, "withdraw_ont error")

			# this should be failed
			(process, response) = API.native().withdraw_ont(wallet_A_address, [node_B_puiblic_key], ["1"], 8)
			self.ASSERT(not process, "withdraw_ont error")


		except Exception as e:
			print(e.args)




####################################################
if __name__ == '__main__':
	unittest.main()	    
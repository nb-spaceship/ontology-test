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

from utils.commonapi import *
from utils.rpcapi import RPCApi
from utils.init_ong_ont import *
from utils.contractapi import *
from test_governance_api.test_api import nodeCountCheck
logger = LoggerInstance

####################################################
# test cases
# 请准备 9个节点进行测试
#
#

rpcapi = RPCApi()

PRICE_TEST = 10000
COST_RADIX = 20600000


xi_table = [
	0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000,
	1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2700000,
	2800000, 2900000, 3000000, 3100000, 3200000, 3300000, 3400000, 3500000, 3600000, 3700000, 3800000, 3900000, 4000000,
	4100000, 4200000, 4300000, 4400000, 4500000, 4600000, 4700000, 4800000, 4900000, 5000000, 5100000, 5200000, 5300000,
	5400000, 5500000, 5600000, 5700000, 5800000, 5900000, 6000000, 6100000, 6200000, 6300000, 6400000, 6500000, 6600000,
	6700000, 6800000, 6900000, 7000000, 7100000, 7200000, 7300000, 7400000, 7500000, 7600000, 7700000, 7800000, 7900000,
	8000000, 8100000, 8200000, 8300000, 8400000, 8500000, 8600000, 8700000, 8800000, 8900000, 9000000, 9100000, 9200000,
	9300000, 9400000, 9500000, 9600000, 9700000, 9800000, 9900000, 10000000,
	]

yi_table = [
	0, 95123, 180968, 258213, 327493, 389401, 444491, 493282, 536257, 573866, 606531, 634645, 658574, 678660, 695220, 708550,
	718927, 726606, 731826, 734808, 735759, 734870, 732317, 728265, 722867, 716262, 708583, 699949, 690472, 680254, 669391,
	657969, 646069, 633765, 621124, 608209, 595076, 581778, 568361, 554869, 541342, 527814, 514317, 500882, 487534, 474297,
	461191, 448236, 435447, 422839, 410425, 398217, 386223, 374452, 362910, 351604, 340537, 329713, 319135, 308805, 298723,
	288890, 279306, 269969, 260879, 252033, 243429, 235066, 226939, 219045, 211382, 203945, 196731, 189736, 182955, 176384,
	170018, 163854, 157887, 152113, 146526, 141122, 135896, 130845, 125963, 121246, 116690, 112290, 108041, 103940, 99981,
	96162, 92477, 88923, 85496, 82192, 79006, 75936, 72977, 70126, 67380,
	]

PRECISE = 1000000
yita = 5


def ASSERT(condition, error):
	if not condition:
		raise Error(error)

def get_yi(initpos, avgpos):
	xi = int(PRECISE * yita * 2 * initpos / (avgpos * 10))
	try:
		index = xi_table.index(xi)
		return yi_table[index]
	except Exception as e:
		print(e)
	return 0;
	
def get_benifit_value(totalgas, initpos, totalpos = [1000, 1000, 1000, 1000, 1000, 1000, 1000]):
	totalyi = 0
	totalposvalue = 0
	for pos in totalpos:
		totalposvalue = totalposvalue + pos
	
	avgpos = totalposvalue / len(totalpos)
	print("avgpos: " + str(avgpos))
	for pos in totalpos:
		totalyi = totalyi + get_yi(pos, avgpos)

	if totalyi == 0:
		return 0
	
	print("totalgas: " + str(totalgas)) 
	print("initpos: " + str(initpos)) 
	print("avgpos: " + str(avgpos)) 
	print("totalyi: " + str(totalyi)) 

	return totalgas * get_yi(initpos, avgpos) / totalyi



class TestBenefit(ParametrizedTestCase):
	@classmethod
	def setUpClass(cls):
		pass
	
	def setUp(self):
		stop_nodes([0,1,2,3,4,5,6,7,8])
		start_nodes([0,1,2,3,4,5,6], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(30)
		init_ont_ong()
		regIDWithPublicKey(0)
		time.sleep(5)
		self.m_current_node = 0
		self.m_stop_2_nodes = [5,6]
		self.m_new_2_nodes = [7, 8]
		self.m_candidate_cost = 500 #摩擦费
		
	def cost_ong(self, amount):
		address = Config.NODES[0]["address"]
		#消耗ong之前的状态
		(result, response)=rpcapi.getbalance(address)
		if not result:
			raise Error("get balance error")
		ong1=int(response["result"]["ong"])
	
		#消耗ong
		contract_address = deploy_contract("contract.neo", price=amount)
		(result, response) = rpcapi.getbalance(address)
		if not result:
			raise Error("get balance error")
			
		ong2 = int(response["result"]["ong"])
		
		#判断消耗ong是否正确
		#print(ong1-ong2==(amount*cost_radix))
		#print(amount*cost_radix)
		#print(ong1-ong2)
		print("before cost[0]: " + str(ong1))
		print("after cost[0]: " + str(ong2))
		if(ong1-ong2==(amount*COST_RADIX)):
			result=True
		else:
			result=False
		if not result:
			raise Error("cost ong error")
		
	def test_1(self):
		logger.open("TestBenefit1.log", "TestBenefit1")
		result = False
		try:
			address1 = Config.NODES[1]["address"]
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			
			result = self.cost_ong(PRICE_TEST)
			
			#判断是否分润，至少需要等待1个共识时间
			invoke_function_commitDpos()
			time.sleep(10)
			
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error")
			ong2=int(response["result"]["ong"])
			print("before cost[1]: " + str(ong1))
			print("after cost[1]: " + str(ong2))
			result = ong2 != ong1
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	#blocked
	def test_2(self):
		logger.open("TestBenefit2.log", "TestBenefit2")
		result = False
		try:
			address1 = Config.NODES[1]["address"]
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			
			result = self.cost_ong(priceTest)
			
			#判断是否分润，至少需要等待1个共识时间
			invoke_function_commitDpos()
	
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error")
			ong2=int(response["result"]["ong"])
			print("before cost[1]: " + str(ong1))
			print("after cost[1]: " + str(ong2))
			result = ong2 != ong1
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	def test_3(self):
		address = Config.NODES[0]["address"]
		logger.open("TestBenefit3.log", "TestBenefit3")
		result = False
		try:
			(result1, response)=rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			ont1=response["result"]["ont"]
		
			contract_address = deploy_contract("contract.neo", price=999999999999999)
			(result1, response) = rpcapi.getbalance(address)
			if not result1:
				raise Error("get balance error")
				
			ong2 = int(response["result"]["ong"])
			ont2 = response["result"]["ont"]
			
			print(ong1-ong2==(priceTest*1000000000))
			print(priceTest*1000000000)
			print(ong1-ong2)
		
			if(ong1-ong2==(priceTest*1000000000)):
				result=False
			else:
				result=True

		except Exception as e:
			print(e.msg)
		logger.close(result)
	
	#blocked
	def test_4(self):
		logger.open("TestBenefit4.log", "TestBenefit4")
		result = False
		try:
			address_stop = Config.NODES[self.m_stop_2_nodes[0]]["address"]
			(result, response) = rpcapi.getbalance(address_stop)
			if not result:
				raise Error("get balance error[1]")
			ong_stop1 = int(response["result"]["ong"])
			
			stop_nodes(self.m_stop_2_nodes)
			address1 = Config.NODES[1]["address"]
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error[2]")
			ong1=int(response["result"]["ong"])
			
			result = self.cost_ong(PRICE_TEST)
			
			#判断是否分润，至少需要等待1个共识时间
			invoke_function_commitDpos()
			time.sleep(10)
			
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error[3]")
			ong2=int(response["result"]["ong"])
			print("wait benefit, before cost[1]: " + str(ong1))
			print("wait benefit, after cost[1]: " + str(ong2))
			result = ong2 != ong1
			if not result:
				raise Error("no benefit")
			
			start_nodes(self.m_stop_2_nodes)
			time.sleep(10)
			
			(result, response) = rpcapi.getbalance(address_stop)
			if not result:
				raise Error("get balance error[4]")
			ong_stop2 = int(response["result"]["ong"])
			print("no benefit, before cost[1]: " + str(ong_stop1))
			print("no benefit, after cost[1]: " + str(ong_stop2))
			result = ong_stop2 == ong_stop1
			if not result:
				raise Error("has benefit")
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
		
	
	def test_5(self):
		logger.open("TestBenefit5.log", "TestBenefit5")
		result = False
		try:
			result = self.cost_ong(priceTest)
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	'''
	def test_6(self):
		logger.open("TestBenefit6.log", "TestBenefit6")
		result = False
		try:
			result = self.cost_ong(priceTest)
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	'''
	
	#前提: 7个节点initpos 都是 1000
	def test_7(self):
		logger.open("TestBenefit7.log", "TestBenefit7")
		result = False
		try:
			check_node = 4 #第一次检查节点
			
			address1 = Config.NODES[check_node]["address"]
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error")
			ong1=int(response["result"]["ong"])
			
			result = transfer_ont(0, 0, 1, PRICE_TEST)
			
			#判断是否分润，至少需要等待1个共识时间
			except_benifit = int(get_benifit_value(20000 * PRICE_TEST * 0.5, 1000, [1000, 1000, 1000, 1000, 1000, 1000, 1000]))
			logger.print("except_benifit: " + str(except_benifit))
			invoke_function_commitDpos()
			time.sleep(10)
			
			(result, response) = rpcapi.getbalance(address1)
			if not result:
				raise Error("get balance error")
			ong2=int(response["result"]["ong"])
			print("before cost[1]: " + str(ong1))
			print("after cost[1]: " + str(ong2))
			result = (int(ong2 - ong1) == int(except_benifit))
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	def add_candidate_node(self, new_node, init_ont = 5000000, init_ong = 1000, init_pos = 1000):
		#新加入节点, 并申请候选节点
		start_nodes([new_node], clear_chain = True, clear_log = True)
		time.sleep(5)
		regIDWithPublicKey(new_node)
		(result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
		if not result:
			return (result, response)
			
		(result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8"))])
		if not result:
			return (result, response)
			
		transfer_ont(0, new_node, init_ont)
		transfer_ong(0, new_node, init_ong)
		
		time.sleep(10)
		
		(result, response) = invoke_function_register(Config.NODES[new_node]["pubkey"], Config.NODES[new_node]["address"], str(init_pos), ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8")), "1")
		if not result:
			return (result, response)	
			
		(result, response) = invoke_function_candidate(Config.NODES[new_node]["pubkey"])		
		return (result, response)
	
	#第7个节点为新加入节点
	def test_8(self):
		logger.open("TestBenefit8.log", "TestBenefit8")
		result = False
		
		check_node = 4 #第一次检查节点
		candidate_initong = 1000 #候选节点初始ong
		
		candidate_pos = 1000 #候选节点初始pos
		new_node = self.m_new_2_nodes[0] #新加入节点
		
		try:
			(result, response) = invoke_function_update("updateGlobalParam", "0", "1000", "32", "1", "50", "50", "5", "5")
			ASSERT(result, "updateGlobalParam error")
			
			address4 = Config.NODES[check_node]["address"]
			(result, response) = rpcapi.getbalance(address4)
			ASSERT(result, "get balance error")
			ong1 = int(response["result"]["ong"])
			
			####################################################################################
			#发生一笔交易，并第一次分红
			result = transfer_ont(0, 0, 1, PRICE_TEST)
			#print("111111111111111: ")
			time.sleep(15)
			invoke_function_commitDpos()
			time.sleep(15)
			#print("222222222222222: ")

			#2.消耗的0.2ong的50%被平均分给七个节点
			except_benifit = int(get_benifit_value(20000 * PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit2 = int(get_benifit_value(20000 * PRICE_TEST * 0.5 * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit3 = int(get_benifit_value(20000 * PRICE_TEST * 0.5 * 0.5 *0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit4 = int(get_benifit_value(20000 * PRICE_TEST * 0.5 * 0.5 *0.5, candidate_pos, [candidate_pos]))
			logger.print("except_benifit: " + str(except_benifit))
			logger.print("except_benifit[2]: " + str(except_benifit2))
			logger.print("except_benifit[3]: " + str(except_benifit3))
			logger.print("except_benifit[4]: " + str(except_benifit4))
			(result, response) = rpcapi.getbalance(address4)
			ASSERT(result, "get balance error")
			
			ong2 = int(response["result"]["ong"])
			print("before cost[1]: " + str(ong1))
			print("after cost[1]: " + str(ong2))
			result = (int(ong2 - ong1) == int(except_benifit))
			ASSERT(result, "first benefit error")
			
			####################################################################################
			#添加候选节点1
			(result, response) = self.add_candidate_node(new_node, init_ong = candidate_pos)
			ASSERT(result, "add candidate node error")
			
			#4.消耗的0.2ong的50%被分配给刚加入的候选节点
			(result, response) = rpcapi.getbalance(Config.NODES[new_node]["address"])
			ASSERT(result, "get balance error")

			ong3 = int(response["result"]["ong"])
			
			#区块到达分红数量要求
			#print("33333333333333: ")
			#nodeCountCheck([], 7)
			time.sleep(15)
			invoke_function_commitDpos()
			time.sleep(15)
			invoke_function_commitDpos()
			time.sleep(15)
			#print("44444444444444: ")
			#nodeCountCheck([], 7)
			#4.消耗的0.2ong的50%被分配给刚加入的候选节点
			(result, response) = rpcapi.getbalance(Config.NODES[new_node]["address"])
			ASSERT(result, "get balance error")
			
			ong4 = int(response["result"]["ong"])
			
			print("before cost[1]: " + str(ong3))
			print("after cost[1]: " + str(ong4))
			result = abs((int(ong4 - ong3) - int(except_benifit4))) < 10
			
		except Exception as e:
			print(e.msg)
			result = False
		logger.close(result)
	
	#第7个节点为新加入节点
	def test_9(self):
		logger.open("TestBenefit9.log", "TestBenefit9")
		result = False
		
		candidate_initong = 1000 #候选节点初始ong
		check_node = 4 #第一次检查节点
		
		candidate_pos = 1000 #候选节点初始pos
		
		new_node1 = self.m_new_2_nodes[0]
		new_node2 = self.m_new_2_nodes[1]
		address1 = Config.NODES[check_node]["address"]
		try:
			invoke_function_update("updateGlobalParam", "0", "1000", "32", "1", "50", "50", "5", "5")
			
			#发生一笔交易
			transfer_ont(0, 0, 1, PRICE_TEST)
			time.sleep(5)

			#添加候选节点1
			(result, response) = self.add_candidate_node(new_node1, init_ong = candidate_initong)
			ASSERT(result, "add candidate error")
		
			#区块到达分红数量要求,获取共识前后的ong值
			(result, response) = rpcapi.getbalance(address1)
			ASSERT(result, "get balance error")
			normal_ong1 = int(response["result"]["ong"])
			(result, response) = rpcapi.getbalance(Config.NODES[new_node1]["address"])
			ASSERT(result, "get balance error")
			candidate1_ong_1 = int(response["result"]["ong"])
	
			#第一次分红，只分红共识节点的，因为候选节点要在下个周期才分红
			time.sleep(15)
			invoke_function_commitDpos()
			time.sleep(15)
			#第二次分红，候选节点也分红
			invoke_function_commitDpos()
			time.sleep(15)
			
			(result, response) = rpcapi.getbalance(address1)
			ASSERT(result, "get balance error")
			normal_ong2 = int(response["result"]["ong"])
			(result, response) = rpcapi.getbalance(Config.NODES[new_node1]["address"])
			ASSERT(result, "get balance error")
			candidate1_ong_2 = int(response["result"]["ong"])
			
			#计算分红值
			except_benifit1 = int(get_benifit_value(20000 * PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit2 = int(get_benifit_value(20000 * PRICE_TEST * 0.5 * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_candidate_benifit1 = int(get_benifit_value(20000 * PRICE_TEST * 0.5 * 0.5, candidate_pos, [candidate_pos]))
			
			#判断分红值
			#消耗的0.2ong的50%被平均分给七个节点，50%被分配给刚加入的候选节点
			logger.print("before cost[1]: " + str(normal_ong1))
			logger.print("after cost[1]: " + str(normal_ong2))
			result = abs(int(normal_ong2 - normal_ong1) - int(except_benifit1 + except_benifit2)) < 10
			ASSERT(result, "first benefit error[normal node]")
			
			result = abs(int(candidate1_ong_2 - candidate1_ong_1) - int(except_candidate_benifit1)) < 10
			ASSERT(result, "first benefit error[candidate node]")
		
			
			
			#添加候选节点2
			(result, response) = self.add_candidate_node(new_node2)
			ASSERT(result, "add candidate node error")

			#4.消耗的0.2ong的50%被分配给刚加入的候选节点
			result = transfer_ont(0, 0, 1, PRICE_TEST)
			ASSERT(result, "transfer ont error")
			time.sleep(5)
		
			
			#区块到达分红数量要求
			(result, response) = rpcapi.getbalance(address1)
			ASSERT(result, "get balance error")
			normal_ong3 = int(response["result"]["ong"])
			(result, response) = rpcapi.getbalance(Config.NODES[new_node2]["address"])
			ASSERT(result, "get balance error")
			candidate2_ong_1 = int(response["result"]["ong"])
			
			#第一次分红，只分红共识节点的，因为候选节点要在下个周期才分红
			time.sleep(15)
			invoke_function_commitDpos()
			time.sleep(15)
			#第二次分红，候选节点也分红
			invoke_function_commitDpos()
			time.sleep(15)
			
			(result, response) = rpcapi.getbalance(address1)
			ASSERT(result, "get balance error")
			normal_ong4 = int(response["result"]["ong"])
			
			(result, response) = rpcapi.getbalance(Config.NODES[new_node2]["address"])
			ASSERT(result, "get balance error")
			candidate2_ong_2 = int(response["result"]["ong"])
			
			#计算分红值
			except_benifit1 = int(get_benifit_value(20000 * PRICE_TEST * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_benifit2 = int(get_benifit_value(20000 * PRICE_TEST * 0.5 * 0.5, 10000, [10000, 10000, 10000, 10000, 10000, 10000, 10000]))
			except_candidate_benifit1 = int(get_benifit_value(20000 * PRICE_TEST * 0.5 * 0.5, candidate_pos, [candidate_pos]))
			#判断分红值
			#消耗的0.2ong的50%被平均分给七个节点，50%被分配给刚加入的候选节点

			logger.print("before cost[2]: " + str(normal_ong3))
			logger.print("after cost[2]: " + str(normal_ong4))
			result = abs(int(normal_ong4 - normal_ong3) - int(except_benifit1 + except_benifit2)) < 10
			ASSERT(result, "first benefit error[normal node]")
			
			#在10以内的误差
			result = abs((int(candidate2_ong_2 - candidate2_ong_1) - int(except_candidate_benifit1))) < 10
			ASSERT(result, "first benefit error[candidate node]")
			
		except Exception as e:
			logger.print(e.msg)
			result = False
		logger.close(result)
		
	def test_10(self):
		address = Config.NODES[2]["address"]
		result = False
		logger.open("TestBenefit10.log", "TestBenefit10")
		try:
			check_node = 4 #第一次检查节点
			candidate_initong = 1000 #候选节点初始ong
			candidate_cost = 500 #摩擦费
			candidate_pos = 1000 #候选节点初始pos
			new_node = self.m_new_2_nodes[0] #新加入节点
			
			address4 = Config.NODES[check_node]["address"]
			(result, response) = rpcapi.getbalance(address4)
			if not result:
				raise Error("get balance error")
			ong1 = int(response["result"]["ong"])

			# create role and bind ONTID with role
			(result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
			if not result:
				raise Error("bind_role_function error")

			(result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8"))])
			if not result:
				raise Error("bind_user_role error")

			(result, response) = invoke_function_register(Config.NODES[7]["pubkey"], Config.NODES[7]["address"] ,"2000", ByteToHex(bytes(Config.NODES[7]["ontid"], encoding = "utf8")), "1", 7)
			if not result:
				raise Error("invoke_function_register error")

			(result, response) = invoke_function_approve(Config.NODES[7]["pubkey"])
			if not result:
				raise Error("invoke_function_approve error")
			time.sleep(10)

			invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)

			response = transfer_ont(0, 2, 1000)
			print (json.dumps(response))
			time.sleep(5)
 
			invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)

			except_benifit = int(get_benifit_value(2 * PRICE_TEST, 1000, [1000, 1000, 1000, 1000, 1000, 1000, 1000]) / 2 * 10000)
		
		except Exception as e:
			print(e.msg)
		logger.close(result)		
		

class Test_Benefit_12_14(ParametrizedTestCase):
	def setUp(self):
		time.sleep(2)
		print("stop all")
		stop_nodes([0,1,2,3,4,5,6,7,8])
		print("start all")
		start_nodes([0,1,2,3,4,5,6,7,8], Config.DEFAULT_NODE_ARGS, True, True)
		time.sleep(10)
		for i in range(0, 14):
			regIDWithPublicKey(i)
		init_ont_ong()
		for i in range(7, 14):
			transfer_ont(0, i, 100000)
			transfer_ong(0, i, 100000)
		
		try:
			# create role and bind ONTID with role
			(result, response) = bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
			if not result:
				raise Error("bind_role_function error")

			for i in range(7, 14):
				(result, response) = bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[i]["ontid"], encoding = "utf8"))])
				if not result:
					raise Error("bind_user_role error")

				(result, response) = invoke_function_register(Config.NODES[i]["pubkey"], Config.NODES[i]["address"] ,"2000", ByteToHex(bytes(Config.NODES[i]["ontid"], encoding = "utf8")), "1", i)
				if not result:
					raise Error("invoke_function_register error")
				
				(result, response) = invoke_function_approve(Config.NODES[i]["pubkey"])
				if not result:
					raise Error("invoke_function_approve error")
				
			time.sleep(10)
		except Exception as e:
			print(e.msg)

	def test_11(self):
		address = Config.NODES[2]["address"]
		result = False
		logger.open("TestBenefit12.log", "TestBenefit12")
		try:
			invoke_function_update("updateGlobalParam","2000000000","10000","32","1","50","50","50","50")
			(result, response) = vote_for_peer_index(Config.NODES[0]["address"], [Config.NODES[7]["pubkey"], Config.NODES[8]["pubkey"], Config.NODES[9]["pubkey"]], ["50000", "50000", "50000"])
			if not result:
				raise Error("vote error")
			
			invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)

			response = transfer_ont(0, 2, 1000)
			print (json.dumps(response))
			time.sleep(5)

			invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)
		
		except Exception as e:
			print(e.msg)
		logger.close(result)

	def test_12(self):
		address = Config.NODES[2]["address"]
		result = False
		logger.open("TestBenefit13.log", "TestBenefit13")
		try:
			invoke_function_update("updateGlobalParam","2000000000","10000","32","1","100","0","50","50")

			response = transfer_ont(0, 2, 1000)
			print (json.dumps(response))
			time.sleep(5)

			invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)

		except Exception as e:
			print(e.msg)
		logger.close(result)

	def test_13(self):
		address = Config.NODES[2]["address"]
		result = False
		logger.open("TestBenefit14.log", "TestBenefit14")
		try:
			invoke_function_update("updateGlobalParam","2000000000","10000","32","1","0","100","50","50")

			response = transfer_ont(0, 2, 1000)
			print (json.dumps(response))
			time.sleep(5)

			invoke_function_consensus(Config.NODES[0]["pubkey"])
			time.sleep(5)

		except Exception as e:
			print(e.msg)
		logger.close(result)
		
####################################################
if __name__ == '__main__':
	'''
	print("55555555: ")
	nodeCountCheck([], 7)
	invoke_function_commitDpos()
	time.sleep(15)
	print("66666666: ")
	nodeCountCheck([], 7)
	'''
	unittest.main()

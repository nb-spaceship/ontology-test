# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt
import time

sys.path.append('..')
sys.path.append('../..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.common import Common

from api.apimanager import API

CONTRACT_API = API.contract()

class test_api:
	@staticmethod
	def getStorageConf(confName):
		return API.rpc().getstorage("0700000000000000000000000000000000000000",ByteToHex(confName.encode("utf-8")))

	@staticmethod
	def transfer(contract_address,from_address,to_address,amount, node_index = None):
		request = {
			"REQUEST": {
				"Qid": "t",
				"Method": "signeovminvoketx",
				"Params": {
					"gas_price": 0,
					"gas_limit": 1000000000,
					"address": contract_address,
					"version": 1,
					"params": [
						{
							"type": "string",
							"value": "transfer"
						},
						{	
							"type" : "string",
							"value" : ""
						},
						{
							"type": "array",
							"value":  [
								{
									"type": "bytearray",
									
									"value": Common.bl_reserver(Common.base58_to_address(from_address))
								},
								{
									"type": "bytearray",
									"value": Common.bl_reserver(Common.base58_to_address(to_address))
								},
								{
									"type": "int",
									"value": amount
								}
							]
						}
					]
				}
			},
			"RESPONSE":{"error" : 0},
			"NODE_INDEX":node_index
		}
		return API.contract().call_contract(Task(name="transfer", ijson=request), twice = True)

	@staticmethod
	def multi_sig_transfer(neo_contract_address, from_address, to_address, amount, m, pubkey_array, node_index=0):
		request = {
				"REQUEST":  {
				"Qid": "t",
				"Method": "signeovminvoketx",
				"Params": {
					"gas_price": 0,
					"gas_limit": 1000000000,
					"address": neo_contract_address,
					"version": 1,
					"params": [
						{
							"type": "string",
							"value": "transfer"
						},
						{
							"type": "array",
							"value": [
								{
									"type": "bytearray",
									"value": Common.bl_reserver(Common.base58_to_address(from_address))
								},
								{
									"type": "bytearray",
									"value": Common.bl_reserver(Common.base58_to_address(to_address))
								},
								{
									"type": "int",
									"value": amount
								}
							]
						}
					]
				}
			},
			"RESPONSE":{"error" : 0},
			"NODE_INDEX":node_index
		}

		return CONTRACT_API.call_multisig_contract(Task(name="multi_sig_transfer", ijson=request), m, pubkey_array)

	@staticmethod
	def add_candidate_node(new_node, init_ont = 5000000, init_ong = 1000, init_pos = 10000, from_node = 0):
		#新加入节点, 并申请候选节点
		API.native().start_nodes([new_node], clear_chain = True, clear_log = True)
		API.native().regid_with_publickey(new_node)
		(process, response) = API.native().bind_role_function("0700000000000000000000000000000000000000", ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),["registerCandidate"])
		if not process:
			return (process, response)
			
		(process, response) = API.native().bind_user_role("0700000000000000000000000000000000000000",ByteToHex(bytes(Config.NODES[0]["ontid"], encoding = "utf8")), ByteToHex(b"roleA"),[ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8"))])
		if not process:
			return (process, response)
			
		API.native().transfer_ont(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ont), 0)
		API.native().transfer_ong(Config.NODES[from_node]["address"], Config.NODES[new_node]["address"], str(init_ong), 0)
		
		time.sleep(10)
		
		(process, response) = API.native().register_candidate(Config.NODES[new_node]["pubkey"], Config.NODES[new_node]["address"], str(init_pos), ByteToHex(bytes(Config.NODES[new_node]["ontid"], encoding = "utf8")), "1", new_node)
		if not process:
			return (process, response)	
			
		(process, response) = API.native().approve_candidate(Config.NODES[new_node]["pubkey"])		
		return (process, response)
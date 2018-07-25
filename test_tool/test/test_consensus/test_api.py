# -*- coding:utf-8 -*-
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys
import getopt

sys.path.append('..')
sys.path.append('../..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error

from api.apimanager import API

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
									
									"value": bl_address(from_address)
								},
								{
									"type": "bytearray",
									"value": bl_address(to_address)
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
	def transfer_19(neo_contract_address, from_address, to_address, amount):
		
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
									"value": from_address
								},
								{
									"type": "bytearray",
									"value": to_address
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
			"RESPONSE": {}
		}

		return API.contract().call_contract(Task(name="test_1", ijson=request), twice = True) 

	@staticmethod
	def transfer_20(neo_contract_address, from_address, to_address, amount, public_key):
		
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
									"value": from_address
								},
								{
									"type": "bytearray",
									"value": to_address
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
			"RESPONSE": {}
		}

		(result, response) = API.contract().sign_transction(Task(name="test_1", ijson=request))

		signed_tx = response["result"]["signed_tx"]

		request = {
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":1,
					"pub_keys":[
						public_key
					]
				}
				},
				"RESPONSE": {}
		}

		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]
		(result, response) = API.contract().call_signed_contract(signed_tx, True)
		(result, response) = API.contract().call_signed_contract(signed_tx, False)
		return (result, response)

	@staticmethod
	def transfer_21(neo_contract_address, from_address, to_address, amount, public_key):
		
		request = {
				"NODE_INDEX" :1,
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
									"value": from_address
								},
								{
									"type": "bytearray",
									"value": to_address
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
			"RESPONSE": {}
		}

		(result, response) = API.contract().sign_transction(Task(name="test_1", ijson=request))

		signed_tx = response["result"]["signed_tx"]

		request = {
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":1,
					"pub_keys":[
						public_key
					]
				}
				},
				"RESPONSE": {}
		}

		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]
		(result, response) = API.contract().call_signed_contract(signed_tx, True)
		(result, response) = API.contract().call_signed_contract(signed_tx, False)
		return (result, response)

	@staticmethod
	def transfer_22(neo_contract_address, from_address, to_address, amount, public_key):
		
		request = {
				"NODE_INDEX" :1,
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
									"value": from_address
								},
								{
									"type": "bytearray",
									"value": to_address
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
			"RESPONSE": {}
		}

		(result, response) = API.contract().sign_transction(Task(name="test_1", ijson=request))

		signed_tx = response["result"]["signed_tx"]

		request = {
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":1,
					"pub_keys":[
						public_key
					]
				}
				},
				"RESPONSE": {}
		}

		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]
		(result, response) = API.contract().call_signed_contract(signed_tx, True)
		(result, response) = API.contract().call_signed_contract(signed_tx, False)
		return (result, response)

	@staticmethod
	def transfer_23(neo_contract_address, from_address, to_address, amount, public_key):
		
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
									"value": from_address
								},
								{
									"type": "bytearray",
									"value": to_address
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
			"RESPONSE": {}
		}

		(result, response) = API.contract().sign_transction(Task(name="test_1", ijson=request))

		signed_tx = response["result"]["signed_tx"]

		request = {
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":1,
					"pub_keys":[
						public_key
					]
				}
				},
				"RESPONSE": {}
		}

		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]
		(result, response) = API.contract().call_signed_contract(signed_tx, True)
		(result, response) = API.contract().call_signed_contract(signed_tx, False)
		return (result, response)

	@staticmethod
	def transfer_24(neo_contract_address, from_address, to_address, amount, public_key_1, public_key_2, public_key_3, public_key_4):
		
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
									"value": from_address
								},
								{
									"type": "bytearray",
									"value": to_address
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
			"RESPONSE": {}
		}

		(result, response) = API.contract().sign_transction(Task(name="test_1", ijson=request))

		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :1,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :2,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :3,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :4,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]


		(result, response) = API.contract().call_signed_contract(signed_tx, True)
		(result, response) = API.contract().call_signed_contract(signed_tx, False)
		return (result, response)

	@staticmethod
	def transfer_25(neo_contract_address, from_address, to_address, amount, public_key_1, public_key_2, public_key_3, public_key_4):
		
		request = {
			"NODE_INDEX":0,
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
									"value": from_address
								},
								{
									"type": "bytearray",
									"value": to_address
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
			"RESPONSE": {}
		}

		(result, response) = API.contract().sign_transction(Task(name="test_1", ijson=request))

		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :1,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :2,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :3,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]

		request = {
				"NODE_INDEX" :4,
				"REQUEST":  {
				"qid":"1",
				"method":"sigmutilrawtx",
				"params":{
					"raw_tx":signed_tx,
					"m":4,
					"pub_keys":[
						public_key_1,
						public_key_2,
						public_key_3,
						public_key_4
					]
				}
				},
				"RESPONSE": {}
		}
		API.contract().sign_multi_transction(Task(name="test_1", ijson=request)) 
		signed_tx = response["result"]["signed_tx"]


		(result, response) = API.contract().call_signed_contract(signed_tx, True)
		(result, response) = API.contract().call_signed_contract(signed_tx, False)
		return (result, response)

	@staticmethod
	def approve_31(neo_contract_address, from_address, to_address, amount):
		request = {
				"REQUEST":  {
				"Qid": "t",
				"Method": "signativeinvoketx",
				"Params": {
					"gas_price": 0,
					"gas_limit": 1000000000,
					"address": "0100000000000000000000000000000000000000",
					"method":"approve",
					"version": 1,
					"params": [
						
							from_address,
							to_address,
							amount
						
					]
					
				}
			},
			"RESPONSE": {}
		}
		return API.contract().call_contract(Task(name="test_1", ijson=request), twice = True) 

	@staticmethod
	def approve_32(neo_contract_address, from_address, to_address, amount):
		request = {
				"NODE_INDEX":3,
				"REQUEST":  {
				"Qid": "t",
				"Method": "signativeinvoketx",
				"Params": {
					"gas_price": 0,
					"gas_limit": 1000000000,
					"address": "0100000000000000000000000000000000000000",
					"method":"approve",
					"version": 1,
					"params": [
						
							from_address,
							to_address,
							amount
						
					]
					
				}
			},
			"RESPONSE": {}
		}
		return API.contract().call_contract(Task(name="test_1", ijson=request), twice = True) 

	@staticmethod
	def allowance(neo_contract_address, from_address, to_address, amount):

		request = {
					"REQUEST":  {
					"Qid": "t",
					"Method": "signativeinvoketx",
					"Params": {
						"gas_price": 0,
						"gas_limit": 1000000000,
						"address": "0100000000000000000000000000000000000000",
						"method":"allowance",
						"version": 1,
						"params": [
							
								from_address,
								to_address
							
						]
						
					}
				},
				"RESPONSE": {}
			}
		return API.contract().call_contract(Task(name="test_1", ijson=request), twice = True) 

	@staticmethod
	def allowance_32(from_address, to_address):

		request = {
					"NODE_INDEX":3,
					"REQUEST":  {
					"Qid": "t",
					"Method": "signativeinvoketx",
					"Params": {
						"gas_price": 0,
						"gas_limit": 1000000000,
						"address": "0100000000000000000000000000000000000000",
						"method":"allowance",
						"version": 1,
						"params": [
							
								from_address,
								to_address
							
						]
						
					}
				},
				"RESPONSE": {}
			}
		return API.contract().call_contract(Task(name="test_1", ijson=request), twice = True) 
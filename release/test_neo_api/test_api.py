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
import subprocess

sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.contractapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

def get_height(contract_address, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neoぴ.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "GetHeight"
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": "string",
                            "value": ""
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def get_header(contract_address, height, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "GetHeader"
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": "int",
                            "value": height
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def get_block(contract_address, block_hash, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "GetBlock"
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": "bytearray",
                            "value": block_hash
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def get_transaction(contract_address, tx_hash, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "GetTransaction"
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": "bytearray",
                            "value": tx_hash
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def get_contract(contract_address, script_hash, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "GetContract"
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": "bytearray",
                            "value": script_hash
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def get_hash(contract_address, script_hash, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": "GetContract"
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": "bytearray",
                            "value": script_hash
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def invoke_contract_create(contract_address, script_hash, node_index = None):
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
					"value": "GetContract_Create"
				},
				{
					"type": "array",
					"value": [
						{
							"type": "bytearray",
							"value": script_hash
						},
						{
							"type": "bool",
							"value": "true"
						},
						{
							"type": "string",
							"value": "testContract"
						},
						{
							"type": "string",
							"value": "1"
						},
						{
							"type": "string",
							"value": "yangjc"
						},
						{
							"type": "string",
							"value": "378986991@qq.com"
						},
						{
							"type": "string",
							"value": "this is my first test contract"
						}
					]
				}
			]
		}
	},
	"RESPONSE": {}
}
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)



def invoke_func_with_1_param(contract_address, func_name, param_type, param_value, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": func_name
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": param_type,
                            "value": param_value
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def invoke_func_with_0_param(contract_address, func_name, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": func_name
                    },
                    {
                        "type": "array",
                        "value": [{
                            "type": "string",
                            "value": ""
                        }]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

def invoke_func_with_2_param(contract_address, func_name, param_type_1, param_value_1, param_type_2, param_value_2, node_index = None):
    request = {
        "DEPLOY" : true,
        "CODE_PATH" : "tasks/neo.neo",
        "REQUEST": {
            "Qid": "t",
            "Method": "signeovminvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": contract_address,
                "version": 0,
                "params": [
                    {
                        "type": "string",
                        "value": func_name
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": param_type_1,
                                "value": param_value_1
                            },
                            {
                                "type": param_type_2,
                                "value": param_value_2
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE": {}
    }
    
    return call_contract(Task(name="init_admin", ijson=request), twice = True)

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

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.parametrizedtestcase import ParametrizedTestCase

def init_admin(contract_address, admin_address, node_index = None):
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
                        "value": "init"
                    },
                    {
                        "type": "array",
                        "value": [
							{
								"type" : "string",
								"value" : ""
							}
                        ]
                    },
					{
                        "type": "array",
                        "value": [
							{
								"type" : "string",
								"value" : ""
							}
                        ]
                    }
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
	
    return call_contract(Task(name="init_admin", ijson=request), twice = True)


def bind_role_function(contract_address, admin_address, role_str, functions, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0600000000000000000000000000000000000000",
                "method": "assignFuncsToRole",
                "version": 0,
                "params": [
                    contract_address,
                    admin_address,
                    role_str,
                    functions,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index

    return call_contract(Task(name="bind_role_function", ijson=request), twice = True)


def bind_user_role(contract_address, admin_address, role_str, ontIDs, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0600000000000000000000000000000000000000",
                "method": "assignOntIDsToRole",
                "version": 0,
                "params": [
                    contract_address,
                    admin_address,
                    role_str,
                    ontIDs,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index

    return call_contract(Task(name="bind_user_role", ijson=request), twice = True)


def delegate_user_role(contract_address, owner_user, delegate_user, delegate_role, period, level, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0600000000000000000000000000000000000000",
                "method": "delegate",
                "version": 0,
                "params": [
                    contract_address,
                    owner_user,
                    delegate_user,
                    delegate_role,
                    period,
                    level,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index    

    return call_contract(Task(name="delegate_user_role", ijson=request), twice = True)


def withdraw_user_role(contract_address, call_user, delegate_user, delegate_role, public_key="1", node_index = None):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
                "address": "0600000000000000000000000000000000000000",
                "method": "withdraw",
                "version": 0,
                "params": [
                    contract_address,
                    call_user,
                    delegate_user,
                    delegate_role,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index  
    return call_contract(Task(name="withdraw_user_role", ijson=request), twice = True)


def invoke_function(contract_address, function_str, callerOntID, public_key="1", node_index = None):
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
                        "value": function_str
                    },
                    {
                        "type": "array",
                        "value": [
                            {
                                "type": "bytearray",
                                "value": callerOntID
                            },
                            {
                                "type": "int",
                                "value": public_key
                            }
                        ]
                    },
					{
                        "type": "array",
                        "value": [
                            {
                                "type": "string",
                                "value": ""
                            }
                        ]
                    }
                ]
            }
        },
        "RESPONSE":{"error" : 0}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    return call_contract(Task(name="invoke_function", ijson=request), twice = True)

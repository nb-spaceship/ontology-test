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

class Common:
    ontid_map = {}

    node_Admin = 2
    ontID_Admin = Config.SERVICES[node_Admin]["pubkey"]
    ontid_map[ontID_Admin] = node_Admin
    
    node_A = 3
    ontID_A = Config.SERVICES[node_A]["pubkey"]
    ontid_map[ontID_A] = node_A
    
    node_B = 4
    ontID_B = Config.SERVICES[node_B]["pubkey"]
    ontid_map[ontID_B] = node_B
    
    node_C = 5
    ontID_C = Config.SERVICES[node_C]["pubkey"]
    ontid_map[ontID_C] = node_C
    
    node_D = 6
    ontID_D = Config.SERVICES[node_D]["pubkey"]
    ontid_map[ontID_D] = node_D
    
    roleA_hex = ByteToHex(b"roleA")
    roleB_hex = ByteToHex(b"roleB")
    

def regIDWithPublicKey(ontId, public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "regIDWithPublicKey",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="regIDWithPublicKey", ijson=request), twice = True)

def addKey(ontId, new_public_key,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "addKey",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					new_public_key,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="addKey", ijson=request), twice = True)
	
def removeKey(ontId, remove_public_Key,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "removeKey",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					remove_public_Key,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="removeKey", ijson=request), twice = True)
def addRecovery(ontId, recovery_address,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "addRecovery",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					recovery_address,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="addRecovery", ijson=request), twice = True)
	
def changeRecovery(ontId, new_recovery_address,old_recovery_address,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "changeRecovery",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					new_recovery_address,
                    old_recovery_address
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="changeRecovery", ijson=request), twice = True)

def regIDWithAttributes(ontId, attributes_array,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "regIDWithAttributes",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					public_key,
					attributes_array
                    
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="regIDWithAttributes", ijson=request), twice = True)
	
def addAttributes(ontId, attributes_array,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "addAttributes",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					attributes_array,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="addAttributes", ijson=request), twice = True)
def removeAttribute(ontId, attributePath,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "removeAttribute",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					attributePath,
                    public_key
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="removeAttribute", ijson=request), twice = True)
	
def getPublicKeys(ontId,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "getPublicKeys",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="getPublicKeys", ijson=request), twice = True)
def getKeyState(ontId,keyNum,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "getKeyState",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					keyNum
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="getKeyState", ijson=request), twice = True)
		
def getAttributes(ontId,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "getAttributes",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="getAttributes", ijson=request), twice = True)
		
def getDDO(ontId,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "getDDO",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="getDDO", ijson=request), twice = True)
	
def verifySignature(ontId,keyNum,public_key, node_index = None,errorcode=47001):
    request = {

        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": 0,
                "gas_limit": 1000000000,
				"method": "verifySignature",
                "address": "0300000000000000000000000000000000000000",
                "version": 1,
                "params": [
                    ontId,
					keyNum
                ]
            }
        },
        "RESPONSE":{"error" : errorcode}
    }

    if node_index != None:
        request["NODE_INDEX"] = node_index
    else:
        node_index = Common.ontid_map[public_key]
        request["NODE_INDEX"] = node_index      
    
    return call_contract(Task(name="verifySignature", ijson=request), twice = True)
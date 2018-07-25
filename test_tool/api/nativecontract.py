# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import shutil
import sys
import getopt
import time
import requests
import subprocess
import tempfile

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.parametrizedtestcase import ParametrizedTestCase
from api.contract import ContractApi

CONTRACT_API = ContractApi()

class NativeApi:
    ADMIN_NUM = 5
    ADMIN_PUBLIST = [Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]
    
    def native_transfer_ont(self, pay_address, get_address, amount, node_index=0, errorcode=0, gas_price=0):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": gas_price,
                    "gas_limit": 1000000000,
                    "address": "0100000000000000000000000000000000000000",
                    "method": "transfer",
                    "version": 1,
                    "params": [
                        [
                            [
                                pay_address,
                                get_address,
                                amount
                            ]
                        ]
                    ]
                }
            },
            "RESPONSE": {"error": errorcode},
            "NODE_INDEX": node_index
        }
        return CONTRACT_API.call_contract(Task(name="transfer", ijson=request), twice=True)

    #regIDWithPublicKey
    def regid_with_publickey(self, node_index):
        ontid = Config.NODES[int(node_index)]["ontid"]
        pubkey = Config.NODES[int(node_index)]["pubkey"]
        request = {
            "REQUEST": {
            "Qid":"t",
            "Method":"signativeinvoketx",
            "Params":{
            "gas_price":0,
            "gas_limit":1000000000,
            "address":"0300000000000000000000000000000000000000",
            "method":"regIDWithPublicKey",
            "version":0,
            "params":[
                ontid,
                pubkey
            ]
            }
            },
            "RESPONSE": {
            "error":0
            }
        }
        
        request["NODE_INDEX"] = node_index
        return CONTRACT_API.call_contract(Task(name ="regIDWithPublicKey", ijson=request), twice = True)

    def bind_role_function(self, contract_address, admin_address, role_str, functions, public_key="1", node_index = None):
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
        else:
            node_index = Config.ontid_map[admin_address]
            request["NODE_INDEX"] = node_index
            
        return CONTRACT_API.call_contract(Task(name="bind_role_function", ijson=request), twice = True)


    def bind_user_role(self, contract_address, admin_address, role_str, ontIDs, public_key="1", node_index = None):
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
        else:
            node_index = Config.ontid_map[admin_address]
            request["NODE_INDEX"] = node_index
            
        return CONTRACT_API.call_contract(Task(name="bind_user_role", ijson=request), twice = True)


    def delegate_user_role(self, contract_address, owner_user, delegate_user, delegate_role, period, level, public_key="1", node_index = None):
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
        else:
            node_index = Config.ontid_map[owner_user]
            request["NODE_INDEX"] = node_index

        return CONTRACT_API.call_contract(Task(name="delegate_user_role", ijson=request), twice = True)


    def withdraw_user_role(self, contract_address, call_user, delegate_user, delegate_role, public_key="1", node_index = None):
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
        else:
            node_index = Config.ontid_map[call_user]
            request["NODE_INDEX"] = node_index
            
        return CONTRACT_API.call_contract(Task(name="withdraw_user_role", ijson=request), twice = True)

    def invoke_function_vote(self, walletAddress,voteList,voteCount,errorcode=0,node_index=None):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "voteForPeer",
                    "version": 0,
                    "params": [
                                walletAddress,
                                voteList,
                                voteCount
                            ]
                        }
                    },
            "RESPONSE":{"error" : errorcode}
        }
        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            for node in Config.NODES:
                if node["address"] == walletAddress:
                    request["NODE_INDEX"] = Config.NODES.index(node)
                    break
            
        return CONTRACT_API.call_contract(Task(name="invoke_function_vote", ijson=request), twice = True)
        
    def invoke_function_update(self, func_,param0,param1,param2,param3,param4,param5,param6,param7, sig_num = ADMIN_NUM, sig_publist = ADMIN_PUBLIST):
        request = { 
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": func_,
                    "version": 0,
                    "params": [
                                param0,
                                param1,
                                param2,
                                param3,
                                param4,
                                param5,
                                param6,
                                param7
                              ]
                        }
                    },
            "RESPONSE":{"error" : 0}
        }
            
        return CONTRACT_API.multi_contract(Task(name="invoke_function_update", ijson=request), sig_num, sig_publist)

    def invoke_function_register(self, pubKey, walletAddress, ontCount, ontID, user, node_index = None):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "registerCandidate",
                    "version": 0,
                    "params": [
                                pubKey,
                                walletAddress,
                                ontCount,
                                ontID,
                                user
                              ]
                        }
                    },
            "RESPONSE":{"error" : 0}
        }
           
        if node_index != None:
            request["NODE_INDEX"] = node_index
        else:
            node_index = Config.ontid_map[ontID]
            request["NODE_INDEX"] = node_index
        
        return CONTRACT_API.call_contract(Task(name="invoke_function_register", ijson=request), twice = True)

    def invoke_function_candidate(self, pubKey,errorcode=0):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "approveCandidate",
                    "version": 0,
                    "params": [
                                pubKey
                              ]
                        }
                    },
            "RESPONSE":{"error" : errorcode}
        }
            
        return CONTRACT_API.multi_contract(Task(name="invoke_function_candidate", ijson=request), ADMIN_NUM, ADMIN_PUBLIST)

    def invoke_function_node(self, func_,pubKey):
        request = {
            "NODE_INDEX":0,
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": func_,
                    "version": 0,
                    "params": [
                                [pubKey]
                              ]
                        }
                    },
            "RESPONSE":{"error" : 0}
        }

        return CONTRACT_API.call_contract(Task(name="invoke_function_node", ijson=request), twice = True)

    def invoke_function_quitNode(self, func_,pubKey,walletAddress):
        request = {
            "NODE_INDEX":0,
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": func_,
                    "version": 0,
                    "params": [
                                pubKey,
                                walletAddress
                              ]
                        }
                    },
            "RESPONSE":{"error" : 0}
        }

        return CONTRACT_API.call_contract(Task(name="invoke_function_quitNode", ijson=request), twice = True)

    #invoke_function_SplitCurve
    def invoke_function_splitcurve(self, func_,array):
        request = {
            "NODE_INDEX":0,
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": func_,
                    "version": 0,
                    "params": [
                                array
                              ]
                        }
                    },
            "RESPONSE":{"error" : 0}
        }
        return CONTRACT_API.call_contract(Task(name="invoke_function_SplitCurve", ijson=request), twice = True)
    

    ###multi##
    def invoke_function_commitDpos(self, nodeIndex=0, sig_num = ADMIN_NUM, sig_pubkeys = ADMIN_PUBLIST):
        request = {
            "NODE_INDEX":nodeIndex,
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params": {
                    "gas_price": 0,
                    "gas_limit": 1000000000,
                    "address": "0700000000000000000000000000000000000000",
                    "method": "commitDpos",
                    "version": 0,
                    "params": [
                              ]
                        }
                    },
            "RESPONSE":{"error" : 0}
        }

        return CONTRACT_API.call_multisig_contract(Task(name="invoke_function_commitDpos", ijson=request), sig_num, sig_pubkeys)

    def transferFrom_multi(self, put_address, amount, node_index = None,errorcode=0,public_key_Array=[], errorkey = "error"):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "signativeinvoketx",
                "Params":{
                
                    "gas_price":0,
                    "gas_limit":1000000000,
                    "address":"0200000000000000000000000000000000000000",
                    "method":"transferFrom",
                    "version":0,
                    "params":[
                            put_address,
                            "0100000000000000000000000000000000000000",
                            put_address,
                            amount
                    ]
                }
            },
            "RESPONSE":{errorkey : errorcode}
        }
        if (errorkey =="error_code"):
            request["SIGN_RESPONSE"]={errorkey : errorcode}

        request["NODE_INDEX"] = node_index    
        return CONTRACT_API.call_multisig_contract(Task(name="transferFrom_multi", ijson=request),public_key_Array[0],public_key_Array[1])
        
    def transfer_multi(self, assetStr,put_address, get_address,amount, node_index = None,errorcode=0,public_key_Array=[], errorkey = "error"):
        request = {
            "REQUEST": {
                "Qid": "t",
                "Method": "sigtransfertx",
                "Params": {
                    "gas_price":0,
                    "gas_limit":1000000000,
                    "asset":assetStr,
                    "from":put_address,
                    "to":get_address,
                    "amount":amount
                }
            },
            "RESPONSE":{errorkey : errorcode}
        }
        if (errorkey =="error_code"):
            request["SIGN_RESPONSE"]={errorkey : errorcode}

        request["NODE_INDEX"] = node_index    
        return CONTRACT_API.call_multisig_contract(Task(name="transfer_multi", ijson=request),public_key_Array[0],public_key_Array[1])

    def init_ont_ong(self):
        for i in range(7):
            (result, response)=self.transfer_multi("ont",Config.MULTI_SIGNED_ADDRESS,Config.NODES[i]["address"],100000000,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])
            if not result:
                return (result, response)
        time.sleep(5)
        #TODO
        (result, response) = self.transferFrom_multi(Config.MULTI_SIGNED_ADDRESS,Config.INIT_AMOUNT_ONG,5,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])       
        if not result:
            return (result, response)
        time.sleep(5)
        #TODO
        for i in range(7):
            (result, response)=self.transfer_multi("ong",Config.MULTI_SIGNED_ADDRESS,Config.NODES[i]["address"],1000000000000000,public_key_Array=[5,[Config.NODES[0]["pubkey"],Config.NODES[1]["pubkey"],Config.NODES[2]["pubkey"],Config.NODES[3]["pubkey"],Config.NODES[4]["pubkey"],Config.NODES[5]["pubkey"],Config.NODES[6]["pubkey"]]])
            if not result:
                return (result, response)
        #TODO
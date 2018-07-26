# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')
sys.path.append('../..')
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

#from utils.selfig import selfig

from utils.hexstring import *
from utils.error import Error
from utils.config import Config

from api.apimanager import API

class test_config():
	deploy_neo_1="./resource/auth.neo"
	deploy_neo_2="./resource/auth_2.neo"
	deploy_neo_3="./resource/auth_3.neo"
	deploy_neo_4="./resource/auth_4.neo"
	deploy_neo_5="./resource/auth_10.neo"
	deploy_neo_6="./resource/auth_11.neo"
	deploy_neo_7="./resource/auth_12.neo"
	deploy_neo_8="./resource/auth_138_A.neo"
	deploy_neo_9="./resource/auth_138_B.neo"
	deploy_neo_10="./resource/auth_139_A.neo"
	
	contract_addr = API.contract().deploy_contract(deploy_neo_1)
	contract_addr_1 = API.contract().deploy_contract_full(deploy_neo_2)
	contract_addr_2 = API.contract().deploy_contract_full(deploy_neo_3)
	contract_addr_3 = API.contract().deploy_contract_full(deploy_neo_4)
	contract_addr_10 = API.contract().deploy_contract_full(deploy_neo_5)
	contract_addr_11 = API.contract().deploy_contract_full(deploy_neo_6)
	contract_addr_12 = API.contract().deploy_contract_full(deploy_neo_7)
	contract_addr_138_1 = API.contract().deploy_contract_full(deploy_neo_8)
	contract_addr_138_2 = API.contract().deploy_contract_full(deploy_neo_9)
	contract_addr_139 = API.contract().deploy_contract_full(deploy_neo_10)
	
	CONTRACT_ADDRESS_CORRECT = contract_addr               # correct
	CONTRACT_ADDRESS_INCORRECT_1 = contract_addr_1         # wrong ontid
	CONTRACT_ADDRESS_INCORRECT_2 = contract_addr_2         # null ontid
	CONTRACT_ADDRESS_INCORRECT_3 = contract_addr_3         # init twice
	CONTRACT_ADDRESS_INCORRECT_4 = contract_addr + "11"    # not real contract
	CONTRACT_ADDRESS_INCORRECT_5 = "45445566"              # messy code
	CONTRACT_ADDRESS_INCORRECT_6 = ""                      # null
	CONTRACT_ADDRESS_INCORRECT_10 = contract_addr_10       # verifytoken contract with wrong address
	CONTRACT_ADDRESS_INCORRECT_11 = contract_addr_11       # verifytoken contract with messy code address
	CONTRACT_ADDRESS_INCORRECT_12 = contract_addr_12       # verifytoken contract with wrong address

	CONTRACT_ADDRESS_138 = contract_addr_138_1             # appcall contract with correct address
	CONTRACT_ADDRESS_139 = contract_addr_139               # appcall contract with messy code address

	ontID_A = ByteToHex(bytes(Config.NODES[0]['ontid'], encoding = "utf8"))       # contract ontid
	ontID_B = ByteToHex(bytes(Config.NODES[2]['ontid'], encoding = "utf8"))     # the first ontid
	ontID_C = ByteToHex(b"did:ont:123")                    # messy code
	ontID_D = ""                
	ontID_E = ByteToHex(bytes(Config.NODES[3]['ontid'], encoding = "utf8"))                           # null

	ROLE_CORRECT = Config.roleA_hex                                              # roleA
	ROLE_INCORRECT_1 = ""                                                        # null
	ROLE_INCORRECT_2 = "7e21402324255e262a2820295f2b"                            # role "~!@#$%^&*( )_+"
	ROLE_INCORRECT_3 = "31313131313131"                                          # role not exist

	FUNCTION_A = "A"                                                             # function A
	FUNCTION_B = "B"                                                             # function B
	FUNCTION_C = "InvokeTransfer"                                                # function InvokeTransfer
	FUNCTION_D = "xxx"                                                           # function not exist

	KEY_NO_1 = "10"                                                              # wrong keyno
	KEY_NO_2 = "abc"                                                             # wrong keyno
	KEY_NO_3 = ""                                                                # null

	PERIOD_CORRECT = "20"                                                        # correct period
	PERIOD_INCORRECT_1 = "0"                                                     # period 0
	PERIOD_INCORRECT_2 = "-1"                                                    # wrong period -1
	PERIOD_INCORRECT_3 = "2.04"                                                  # wrong period 2.04
	PERIOD_INCORRECT_4 = "abc"                                                   # wrong period abc
	PERIOD_INCORRECT_5 = ""                                                      # null

	LEVEL_CORRECT = "1"                                                          # correct level 1
	LEVEL_INCORRECT_1 = "2"                                                      # wrong level 2
	LEVEL_INCORRECT_2 = "0"                                                      # wrong level 0
	LEVEL_INCORRECT_3 = "abc"                                                    # wrong level abc
	LEVEL_INCORRECT_4 = ""                                                       # null
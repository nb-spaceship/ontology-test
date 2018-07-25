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
from utils.api.commonapi import *
from utils.api.contractapi import *
from utils.api.rpcapi import *
from utils.api.init_ong_ont import *

from test_api import *


class test_config():
	testpath = os.path.dirname(os.path.realpath(__file__))
	deploy_neo_1=testpath + "/resource/A.neo"
	deploy_neo_2=testpath + "/resource/B.neo"
	name1="name"
	name2="nameB"
	desc="desc"
	desc2="descB"
	price=0

	(m_contract_addr, m_contract_txhash) = deploy_contract_full(deploy_neo_1, name1, desc, price)
	(m_contract_addr2, m_contract_txhash2) = deploy_contract_full(deploy_neo_2, name2, desc2, price)
		
	#A�ڵ���Admin�ڵ�
	(process, response) = init_admin(m_contract_addr, Config.ontID_A)
	(process, response) = bind_role_function(m_contract_addr, Config.ontID_A, Config.roleA_hex, ["auth_put"])
		
	m_current_node = 0
	m_storage_key = ByteToHex(b'Test Key')
	m_storage_value = ByteToHex(b'Test Value')
	m_stop_2_nodes = [5,6]
	
	CONTRACT_ADDRESS = ""
	ADDRESS_A = script_hash_bl_reserver(base58_to_address(Config.NODES[0]["address"]))
	ADDRESS_B = script_hash_bl_reserver(base58_to_address(Config.NODES[1]["address"]))
	ADDRESS_C = script_hash_bl_reserver(base58_to_address(Config.NODES[2]["address"]))
	AMOUNT = "1001"
	PUBLIC_KEY = Config.NODES[0]["pubkey"]
	PUBLIC_KEY_2 = Config.NODES[1]["pubkey"]
	PUBLIC_KEY_3 = Config.NODES[2]["pubkey"]
	PUBLIC_KEY_4 = Config.NODES[3]["pubkey"]
	PUBLIC_KEY_5 = Config.NODES[4]["pubkey"]
	
	
	vote_node = 13 #ͶƱ�ڵ�
	peer_node1 = 7 #��ͶƱ�ڵ�1
	peer_node2 = 8 #��ͶƱ�ڵ�2
	peer_node3 = 9 #��ͶƱ�ڵ�3
	

		

	
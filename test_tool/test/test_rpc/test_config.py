# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from utils.config import Config
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *

class test_config():
		(m_contractaddr_right, m_txhash_right) = deploy_contract_full("tasks/A.neo", "name", "desc", 0)
		m_txhash_wrong = "is a wrong tx hash"
		
		#(result, reponse) = rpcApi.getblockhash(height = 1)
		#m_block_hash_right = reponse["result"]
		m_block_hash_right = ""
		
		m_block_hash_error = "this is a wrong block hash"
		
		m_block_height_right = 1
		
		m_block_height_wrong = 9999
		
		m_block_height_overflow = 99999999
		
		#(result, reponse) = sign_transction(Task("tasks/cli/siginvoketx.json"), False)
		#m_signed_txhash_right = reponse["result"]["signed_tx"]
		#m_signed_txhash_wrong = self.m_signed_txhash_right + "0f0f0f0f"
		m_signed_txhash_right=""
		m_signed_txhash_wrong=m_signed_txhash_right + "0f0f0f0f"
		
		m_getstorage_contract_addr = m_contractaddr_right
		m_getstorage_contract_addr_wrong = m_contractaddr_right + "0f0f0f0f"
		m_getstorage_contract_key = ByteToHex(b'key1')
		m_getstorage_contract_value = ByteToHex(b'value1')
		
		getsmartcodeevent_height = 5

		getbalance_address_true = Config.NODES[0]["address"]
		getbalance_address_false = "ccccccccccccccc"
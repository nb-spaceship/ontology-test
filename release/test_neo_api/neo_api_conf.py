# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.commonapi import *
from utils.contractapi import *
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.rpcapi import RPCApi

rpcApi = RPCApi()

class Conf():
    CONTRACT_ADDRESS = ""

    (contract_addr, contract_tx_hash) = deploy_contract_full(Config.UTILS_PATH + "/test.neo")
    (contract_addr_1, contract_tx_hash_1) = deploy_contract_full(Config.UTILS_PATH + "/test.neo", price=1000000000)
    block_height = int(rpcApi.getblockcount()[1]["result"]) - 1
    block_hash = rpcApi.getblockhash(block_height - 1)[1]["result"]

    BLOCK_HEIGHT_WITH_TX = rpcApi.getblockheightbytxhash(contract_tx_hash)[1]["result"]
    BLOCK_HEIGHT_WITHOUT_TX = rpcApi.getblockheightbytxhash(contract_tx_hash)[1]["result"]+1

    HEIGHT_CORRECT = str(block_height - 1)
    HEIGHT_BORDER_BOTTON = "0"
    HEIGHT_BORDER_TOP = "4294967291"
    HEIGHT_INCORRECT_1 = "-1"
    HEIGHT_INCORRECT_2 = str(block_height + 1000)
    HEIGHT_INCORRECT_3 = "abc"
    HEIGHT_INCORRECT_4 = ""

    BLOCK_HASH_CORRECT = block_hash
    BLOCK_HASH_INCORRECT_1 = "" # NULL
    BLOCK_HASH_INCORRECT_2 = block_hash[:-2] # HASH NOT EXISTENT
    BLOCK_HASH_INCORRECT_3 = block_hash + "1111"
    BLOCK_HASH_INCORRECT_4 = "1234"

    TX_HASH_CORRECT = contract_tx_hash
    TX_HASH_INCORRECT_1 = "" # NULL
    TX_HASH_INCORRECT_2 = contract_tx_hash[:-2] # TX HASH NOT EXISTENT
    TX_HASH_INCORRECT_3 = contract_tx_hash + "1111"
    TX_HASH_INCORRECT_4 = "1234"

    SCRIPT_HASH_CORRECT = ByteToHex(contract_tx_hash, encoding = "utf8")
    SCRIPT_HASH_INCORRECT_1 = "31313131"
    SCRIPT_HASH_INCORRECT_2 = ByteToHex(contract_tx_hash_1, encoding = "utf8")
 
    GET_HEADER_FUNC_NAME = "GetHeader"
    GET_HEIGHT_FUNC_NAME = "GetHeight"
    GET_BLOCK_FUNC_NAME = "GetBlock"
    GET_TRANSACTION_FUNC_NAME = "GetTransaction"
    GET_CONTRACT_FUNC_NAME = "GetContract"
    GET_HEADER_HASH_FUNC_NAME = "GetHeaderHash"
    GET_HEADER_VERSION_FUNC_NAME = "GetHeaderVersion"
    GET_HEADER_PREHASH_FUNC_NAME = "GetHeaderPrevHash"
    GET_HEADER_INDEX_FUNC_NAME = "GetHeaderIndex"
    GET_HEADER_MERKLEROOT_FUNC_NAME = "GetHeaderMerkleRoot"
    GET_HEADER_TIMESTAMP_FUNC_NAME = "GetHeaderTimestamp"
    GET_HEADER_CONSENSUS_DATA_FUNC_NAME = "GetHeaderConsensusData"
    GET_HEADER_NEXT_CONSENSUS_FUNC_NAME = "GetHeaderNextConsensus"
    GET_BLOCK_TRANSACTION_COUNT_FUNC_NAME = "GetBlockTransactionCount"
    GET_BLOCK_TRANSACTIONS_FUNC_NAME = "GetBlockTransactions"
    GET_BLOCK_TRANSACTION_FUNC_NAME = "GetBlockTransaction_40"
    GET_CONTRACTION_FUNC_NAME = "GetTransaction_Hash"
    GET_CONTRACTION_TYPE_FUNC_NAME = "GetTransaction_Type"
    GET_TRANSACTIONS_ATTRIBUTE_FUNC_NAME = "GetTransaction_Attributes"
    GET_TRANSACTIONS_ATTRIBUTE_USAGE_FUNC_NAME = "GetTransactionAttribute_Usage"
    GET_TRANSACTIONS_ATTRIBUTE_DATA_FUNC_NAME = "GetTransactionAttribute_Data"
    GET_CONTRACT_SCRIPT_FUNC_TIME = "GetContract_Script"
    GET_CONTRACT_CREATE_FUNC_TIME = "GetContract_Create"

    PARAM_TYPE_INT = "int"
    PARAM_TYPE_BYTEARRAY = "bytearray"

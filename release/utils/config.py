# -*- coding: utf-8 -*-
import json

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase

class Config():
	cfg_file = open("../config.json", "rb")
	cfg_json = json.loads(cfg_file.read().decode("utf-8"))
	cfg_file.close()

	#ERRCODE
	ERR_CODE = {
        0 : "SUCCESS",
	    41001 : "SESSION_EXPIRED: invalided or expired session",
	    41002 : "SERVICE_CEILING: reach service limit",
	    41003 : "ILLEGAL_DATAFORMAT: illegal dataformat",
	    41004 : "INVALID_VERSION: invalid version",
	    42001 : "INVALID_METHOD: invalid method",
	    42002 : "INVALID_PARAMS: invalid params",
	    43001 : "INVALID_TRANSACTION: invalid transaction",
	    43002 : "INVALID_ASSET: invalid asset",
	    43003 : "INVALID_BLOCK: invalid block",
	    44001 : "UNKNOWN_TRANSACTION: unknown transaction",
	    44002 : "UNKNOWN_ASSET: unknown asset",
	    44003 : "UNKNOWN_BLOCK: unknown block",
	    45001 : "INTERNAL_ERROR: internel error",
	    47001 : "SMARTCODE_ERROR: smartcode error"
	}

	THREAD = 1

	TEST_SERVICE_PORT = 23635
	NODES = cfg_json["NODES"]

	RPC_HEADERS = {'content-type': 'application/json'}
	#RPC CONFIG
	RPC_URL = cfg_json["RPC_URL"]

	#Restful CONFIG
	RESTFUL_URL = cfg_json["RESTFUL_URL"]
	
	#WebSocket CONFIG
	WS_URL = cfg_json["WS_URL"]

	#CLIRPC_URL CONFIG
	CLIRPC_URL = cfg_json["CLIRPC_URL"]

	ROOT_PATH = cfg_json["ROOT_PATH"]

	TOOLS_PATH = ROOT_PATH + "/" + "tools"

	UTILS_PATH = ROOT_PATH + "/" + "utils"

	BASEAPI_PATH = UTILS_PATH + "/baseapi"

	DEFAULT_NODE_ARGS = "--ws --rest --loglevel=0 --networkid=299"


#####################################################################################
    ontid_map = {}

    node_Admin = 0
    ontID_Admin = ByteToHex(bytes(NODES[node_Admin]["ontid"], encoding = "utf8"))
    ontid_map[ontID_Admin] = node_Admin
	
    node_A = 1
    ontID_A = ByteToHex(bytes(NODES[node_A]["ontid"], encoding = "utf8"))
    ontid_map[ontID_A] = node_A
	
    node_B = 2
    ontID_B = ByteToHex(bytes(NODES[node_B]["ontid"], encoding = "utf8"))
    ontid_map[ontID_B] = node_B
	
    node_C = 3
    ontID_C = ByteToHex(bytes(NODES[node_C]["ontid"], encoding = "utf8"))
    ontid_map[ontID_C] = node_C
	
    node_D = 4
    ontID_D = ByteToHex(bytes(NODES[node_D]["ontid"], encoding = "utf8"))
    ontid_map[ontID_D] = node_D
	
    node_E = 5
    ontID_E = ByteToHex(bytes(NODES[node_E]["ontid"], encoding = "utf8"))
    ontid_map[ontID_E] = node_E
	
    node_F = 6
    ontID_F = ByteToHex(bytes(NODES[node_F]["ontid"], encoding = "utf8"))
    ontid_map[ontID_F] = node_F
	
    roleA_hex = ByteToHex(b"roleA")
    roleB_hex = ByteToHex(b"roleB")    
    roleC_hex = ByteToHex(b"roleC")
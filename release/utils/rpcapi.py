# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time
import requests
import subprocess

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.commonapi import *

class RPCApi:
	def getbestblockhash(self):
		task = Task(Config.BASEAPI_PATH + "/rpc/getbestblockhash.json")
		taskrequest = task.request()
		params = []
		taskrequest["params"] = params
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblock(self, height, blockhash, verbose = None):
		task = Task(Config.BASEAPI_PATH + "/rpc/getblock.json")
		taskrequest = task.request()
		params = []
		if height:
			params.append(height)

		if blockhash:
			params.append(blockhash)

		if verbose:
			params.append(verbose)

		taskrequest["params"] = params
		task.set_request(taskrequest)
		return run_single_task(task)

	def getblockcount(self):
		task = Task(Config.BASEAPI_PATH + "/rpc/getblockcount.json")
		return run_single_task(task)

	def getblockhash(self, height):
		task = Task(Config.BASEAPI_PATH + "/rpc/getblockhash.json")
		taskrequest = task.request()
		params = []
		if height:
			params.append(height)
		taskrequest["params"] = params
		task.set_request(taskrequest)

		return run_single_task(task)

	def getconnectioncount(self):
		task = Task(Config.BASEAPI_PATH + "/rpc/getconnectioncount.json")
		return run_single_task(task)

	def getgenerateblocktime(self):
		task = Task(Config.BASEAPI_PATH + "/rpc/getgenerateblocktime.json")
		return run_single_task(task)

	def getrawtransaction(self, transactionhash):
		task = Task(Config.BASEAPI_PATH + "/rpc/getrawtransaction.json")
		taskrequest = task.request()
		params = []
		if transactionhash:
			params.append(transactionhash)
		taskrequest["params"] = params
		task.set_request(taskrequest)
		return run_single_task(task)

	def sendrawtransaction(self, _hex, pre = True):
		task = Task(Config.BASEAPI_PATH + "/rpc/sendrawtransaction.json")
		taskrequest = task.request()
		params = []
		if _hex:
			params.append(_hex)
		if pre:
			params.append(pre)
		taskrequest["params"] = params
		task.set_request(taskrequest)

		return run_single_task(task)

	def getstorage(self, script_hash, key):
		task = Task(Config.BASEAPI_PATH + "/rpc/getstorage.json")
		taskrequest = task.request()
		params = []
		if script_hash:
			params.append(script_hash)

		if key:
			params.append(key)
		taskrequest["params"] = params
		task.set_request(taskrequest)

		return run_single_task(task)

	def getversion(self):
		task = Task(Config.BASEAPI_PATH + "/rpc/getversion.json")
		return run_single_task(task)

	def getblocksysfee(self):
		task = Task(Config.BASEAPI_PATH + "/rpc/getblocksysfee.json")
		return run_single_task(task)

	def getcontractstate(self, script_hash, verbose = None):
		task = Task(Config.BASEAPI_PATH + "/rpc/getcontractstate.json")
		taskrequest = task.request()
		params = []
		if script_hash:
			params.append(script_hash)
		if verbose:
			params.append(verbose)
		taskrequest["params"] = params
		task.set_request(taskrequest)

		return run_single_task(task)

	def getmempooltxstate(self, tx_hash):
		task = Task(Config.BASEAPI_PATH + "/rpc/getmempooltxstate.json")
		taskrequest = task.request()
		params = []
		if tx_hash:
			params.append(tx_hash)
		taskrequest["params"] = params
		task.set_request(taskrequest)

		return run_single_task(task)

	def getsmartcodeevent(self, height, tx_hash):
		task = Task(Config.BASEAPI_PATH + "/rpc/getsmartcodeevent.json")
		taskrequest = task.request()
		params = []
		if height:
			params.append(height)
		if tx_hash:
			params.append(tx_hash)
		taskrequest["params"] = params

		return run_single_task(task)

	def getblockheightbytxhash(self, tx_hash):
		task = Task(Config.BASEAPI_PATH + "/rpc/getblockheightbytxhash.json")
		params = []
		if tx_hash:
			params.append(tx_hash)

		return run_single_task(task)

	def getbalance(self, address):
		task = Task(Config.BASEAPI_PATH + "/rpc/getbalance.json")
		params = []
		if address:
			params.append(address)
		return run_single_task(task)

	def getmerkleproof(self, tx_hash):
		task = Task(Config.BASEAPI_PATH + "/rpc/getmerkleproof.json")
		params = []
		if tx_hash:
			params.append(tx_hash)
		return run_single_task(task)

	def getgasprice(self):
		task = Task(Config.BASEAPI_PATH + "/rpc/getgasprice.json")
		return run_single_task(task)

	def getallowance(self, asset, _from, _to):
		task = Task(Config.BASEAPI_PATH + "/rpc/getallowance.json")
		params = []
		if asset:
			params.append(asset)
		if _from:
			params.append(_from)
		if _to:
			params.append(_to)
		return run_single_task(task)
import time
import os
import unittest
import sys
import json
import fileinput

sys.path.append('..')
sys.path.append('../..')

from utils.logger import LoggerInstance as logger 
from api.apimanager import API

TRY_RECOVER_TIMES = 2
CHECK_LOOP = 50
FAILED_RADIO = 40 # 40%

class TestMonitor:
	#分析环境，未知错误的检查
	def __init__(self):
		self.faild_step_count = 0
		self.total_step_count = 0
		self.case_count = 0
		self.retry_cases = []
		self.retry_logger_path = []
		self.initmap = {}
		self.alltestcase = []
		self.unittestrunner = None

	def reset(self):
		self.faild_step_count = 0
		self.total_step_count = 0
		self.case_count = 0
		self.retry_cases = []
		self.retry_logger_path = []
		self.initmap = {}

	def need_retry():
		if self.case_count >= CHECK_LOOP and self.faild_step_count * 100 / self.total_step_count < FAILED_RADIO:
			return False
		else:
			return True

	def analysis_case(self, case, logpath):
		if not os.path.exists(logpath):
			return

		f = open(logpath, 'r')
		org_failed_count = self.faild_step_count
		JSONBody = ""
		for line in f.readlines():
			line = line.strip()
			if line.startswith('[ CALL CONTRACT ] {') or line.startswith("[ SIGNED TX ] {"):
				JSONBody = "{"
			elif JSONBody != "":
				JSONBody = JSONBody + line
			try:
				JSONObj = json.loads(JSONBody)
				if JSONObj:
					if "RESPONSE" in JSONObj:
						RESPONSE = JSONObj["RESPONSE"]
						if "result" in RESPONSE and "State" in RESPONSE["result"]:
							#for contract pre called.
							if RESPONSE["result"]["State"] != 1:
								self.faild_step_count = self.faild_step_count + 1
						elif "error" in RESPONSE:
							if RESPONSE["error"] != 0:
								self.faild_step_count = self.faild_step_count + 1
						elif "error_code" in RESPONSE:
							if RESPONSE["error_code"] != 0:
								self.faild_step_count = self.faild_step_count + 1
					else:
						self.faild_step_count = self.faild_step_count + 1

					self.total_step_count = self.total_step_count + 1
			except Exception as e:
				print(e.args)
				pass
		f.close()

		self.case_count = self.case_count + 1
		if org_failed_count != self.faild_step_count:
			self.retry_cases.append(case)
			self.retry_logger_path.append(logpath)
			if not self.need_retry():
				self.reset()

	#恢复测试环境
	def recover_env(self):
		print("recover env...")
		#restart node
		API.node().stop_all_nodes()
		for node_index in range(len(Config.NODES)):
			self.start_nodes([node_index], clear_chain = True, clear_log = True)

		#restart sigserver
		#API.node().stop_all_nodes()
		#for node_index in range(len(Config.NODES)):
		#	self.start_nodes([node_index], clear_chain = True, clear_log = True)

		return True

	def retry(self):
		self.recover_env()
		testcaseremain = self.retry_cases
		self.reset()
		for case in testcases:
			self.run_case(case)

	def run_case(self, case):
		testmethodname = case._testMethodName
		testcaseclass = case.__class__
		if (testcaseclass in self.initmap) and (self.initmap[testcaseclass] == True):
			print("already ran init..")
		else:
			for initcase in self.alltestcase:
				if initcase.__class__ == testcaseclass and initcase._testMethodName == "test_init":
					testsuit = unittest.TestSuite()
					testsuit.addTest(initcase)
					self.unittestrunner.run(testsuit)
					self.initmap[testcaseclass] = True

		testsuit = unittest.TestSuite()
		testsuit.addTest(case)
		self.unittestrunner.run(testsuit)
		self.analysis_case(case, logger.logPath())

	def set_retry_block(self):
		for path in self.retry_logger_path:
			with open(path, 'a+') as f:
				f.write('[ BLOCK ]')

			collectionlogpath = os.path.dirname(path) + "/collection_log.csv"
			for line in fileinput.input(collectionlogpath, backup='.bak', inplace=1):
				if os.path.basename(path) in line.rstrip():
					line.rstrip().replace('pass', 'block')
					line.rstrip().replace('fail', 'block')

	def exec(self, runner, testcases):
		self.alltestcase = testcases.copy()
		self.unittestrunner = runner
		testcaseremain = testcases.copy()
		for case in testcaseremain:
			try:
				self.run_case(case)
				continue
				
				self.run_case(case)
				if self.need_retry():
					retry_ret = False
					for i in range(TRY_RECOVER_TIMES):
						self.retry()
						retry_ret = self.need_retry()
						if retry_ret == True:
							break
					if retry_ret == False:
						self.set_retry_block()
			except Exception as e:
				print(e.args)
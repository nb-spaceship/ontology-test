import time
import os
import unittest

sys.path.append('..')
sys.path.append('../..')

from utils.logger import LoggerInstance as logger 

TRY_RECOVER_TIMES = 2
CHECK_LOOP = 200
FAILED_RADIO = 40 # 40%

class TestMonitor:
	#分析环境，未知错误的检查
	def __init__(self):
		self.faild_step_count = 0
		self.total_step_count = 0
		self.case_count = 0
		self.retry_cases = []
		self.retry_logger_path = []

	def reset(self):
		self.faild_step_count = 0
		self.total_step_count = 0
		self.case_count = 0
		self.retry_cases = []
		self.retry_logger_path = []

	def analysis_case(self, case, logpath):
		f = open(logpath, 'r')
		org_failed_count = self.faild_step_count
		for line in f.readlines():
			line = line.strip()
		    if line.startswith('[ Failed   ]'):
				self.faild_step_count = self.faild_step_count + 1
		    	self.total_step_count = self.total_step_count + 1
			else:
				self.total_step_count = self.total_step_count + 1
		f.close()

		self.case_count = self.case_count + 1
		if org_failed_count != self.faild_step_count
			self.retry_cases.append(case)
			self.retry_logger_path.append(logpath)

		if self.case_count >= CHECK_LOOP and self.faild_step_count / self.total_step_count < 0.4:
			self.reset()

	#恢复测试环境
	def recover_env(self):
		return False

	def retry(self, runner):
		recover_env()
		testcaseremain = self.retry_cases
		self.retry_cases = []
		for case in testcases:
			testcaseremain.remove(case)
			run_case(runner, case)
			if self.faild_step_count >= MAX_BLOCK_TIMES:
				return False
		return True

	def run_case(self, runner, case):
		testmethodname = case._testMethodName
		testcaseclass = case.__class__
		if (testcaseclass in initmap) and (initmap[testcaseclass] == True):
			print("already ran init..")
		else
			#TODO ran test_init
			initmap[testcaseclass] = True

		testsuit = unittest.TestSuite()
		testsuit.addTest(case)
		runner.run(testsuit)
		analysis_case(case, logger.logPath())

	def exec(self, runner, testcases):
		initmap = {}
		testcaseremain = testcases
		for case in testcases:
			testcaseremain.remove(case)
			run_case(runner, case)

			if self.faild_step_count >= MAX_BLOCK_TIMES:
				retry_ret = False
				for i in range(TRY_RECOVER_TIMES)
					retry_ret = retry(runner)
					if retry_ret == True:
						break
				if retry_ret == False:
					#set_block

if __name__ == '__main__':
	TestMonitor().analysis_env("../")
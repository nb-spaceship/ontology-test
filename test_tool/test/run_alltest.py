# coding:utf-8
import unittest
import os
import sys, getopt

sys.path.append('..')
sys.path.append('../..')

from monitor.monitor import TestMonitor


class TestCaseRunner():
	#通过读config文件，来获取测试例
	def valid_suite(self, config):
		return True
		pass

	def run_testcase(self, runner, case):
		testmethodname = case._testMethodName
		testcaseclass = case.__class__
		print("---------------------:" + test_case._testMethodName)
		print("---------------------:" + str(test_case.__class__))
		runner.run(case)

	def run(self, monitor):
		print("11111111111111")
		filterfile = ""
		filtertype = ""
		filterstr = ""
		opts, args = getopt.getopt(sys.argv[1:], "c:t:f:", ["config=", "type=","filter="])
		for op, value in opts:
			if op in ("-c", "--config"):
				filterfile = value
			if op in ("-t", "--type"):
				filtertype = value
			if op in ("-f", "--filter"):
				filterstr = value
		print("2222222222222222")

		case_path = os.path.dirname(os.path.realpath(__file__))
		print("333333333333333333")

		test_suites = unittest.defaultTestLoader.discover(case_path,
		                                            pattern="test_*.py",
		                                            top_level_dir=None)
		print("444444444444444")

		#filter
		filter_test_suite = []
		for test_suite in test_suites:
			if not self.valid_suite(filterfile):
				continue

			for test_cases in test_suite:
				try:
					for test_case in test_cases:
						#print('\n'.join(['%s:%s' % item for item in test_case.__dict__.items()]))
						#alltestcase.addTest(test_case)
						filter_test_suite.append(test_case)
						print("---------------------:" + test_case._testMethodName)
						print("---------------------:" + str(test_case.__class__))
				except:
					print("error case???")

		runner = unittest.TextTestRunner()
		monitor.exec(runner, filter_test_suite)

if __name__ == "__main__":
	tmonitor = TestMonitor()
	caserunner = TestCaseRunner()
	caserunner.run(tmonitor)
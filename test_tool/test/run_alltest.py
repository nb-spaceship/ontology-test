# coding:utf-8
import unittest
import os
import sys, getopt

sys.path.append('..')
sys.path.append('../..')

from monitor.monitor import TestMonitor

#通过读config文件，来获取测试例
def run_suite(config):
	pass

if __name__ == "__main__":
	tmonitor = TestMonitor()

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

	case_path = os.path.dirname(os.path.realpath(__file__))
	test_suites = unittest.defaultTestLoader.discover(case_path,
	                                            pattern="test_*.py",
	                                            top_level_dir=None)

	#runner = unittest.TextTestRunner()
	#alltestcase = unittest.TestSuite()
	filter_test_suites = []
	for test_suite in test_suites:
		if not run_suite(filterfile):
			continue

		filter_test_suite = unittest.TestSuite()
		for test_cases in test_suite:
			for test_case in test_cases:
				#print('\n'.join(['%s:%s' % item for item in test_case.__dict__.items()]))
				#alltestcase.addTest(test_case)
				filter_test_suite.addTest(test_case)
				print("---------------------:" + test_case._testMethodName)
				print("---------------------:" + str(test_case.__class__))
				filter_test_suites.append(filter_test_suite)
	#runner.run(alltestcase)
	tmonitor.exec(filter_test_suites)

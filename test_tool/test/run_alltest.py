# coding:utf-8
import unittest
import os
import sys, getopt
import json

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

	def filter_test_cases(self, test_suites, filterfile, filtertype, filterstr):
		filter_condition = {"files":None, "class":None, "method":None, "except":[]}

		result = []
		try:
			if filterstr:
				if "!" in filterstr:
					except_cases = filterstr.strip("()!").split(",")
					except_cases = list(map(lambda x : x.strip(" "), except_cases))
					filter_condition["except"] = [t.split(".")[1] for t in except_cases]
				else:
					test_cases = filterstr.split(",")
					test_cases = list(map(lambda x : x.strip(" "), test_cases))
					filter_condition["class"] = [t.split(".")[0] for t in test_cases]
					filter_condition["method"] = [t.split(".")[1] for t in test_cases]

					filter_condition["class"] = list(set(filter_condition["class"]))
					filter_condition["method"] = list(set(filter_condition["method"]))

			if filterfile:
				files = []
				with open(filterfile) as f:
					config_json = json.load(f)
					print(config_json)
				for (key, value) in config_json.items():
					if value :
						files.append(key)
				filter_condition["files"] = list(set(files))

			if filtertype:
				if filtertype == "base":
					filter_condition["method"] = ["_base"]
				elif filtertype == "normal":
					filter_condition["method"] = ["_base", "_normal"]
				elif  filtertype == "abnormal":
					filter_condition["method"] = ["_abnormal"]
				else:
					pass
				filter_condition["method"] = list(set(filter_condition["method"]))

			print(filter_condition)

			for test_suite in test_suites:
				if filter_condition["files"] == []:
					continue
				print(test_suite)
				if filter_condition["files"] and test_suite._tests and test_suite._tests[-1]._tests and not str(test_suite._tests[-1]._tests[0].__class__).strip('<class \'').split('.')[-3] in filter_condition["files"]:
					continue
				for test_cases in test_suite:
					if test_cases._tests and filter_condition["method"]:
						filter_condition["method"].append("test_init")
						filter_condition["method"] = list(set(filter_condition["method"]))
					if filter_condition["class"] and test_cases._tests and not str(test_cases._tests[0].__class__).strip('\'>').split('.')[-1] in filter_condition["class"]:
						continue
					for test_case in test_cases:
						if filter_condition["method"]:
							for m in filter_condition["method"]:
								if test_case._testMethodName and ((not m in test_case._testMethodName) or test_case._testMethodName in filter_condition["except"]):
									continue
								result.append(test_case)
						else:
							if filter_condition["except"] and test_case._testMethodName in filter_condition["except"]:
								continue
							result.append(test_case)

		except Exception as e:
			print(e.args)

		result.sort(key=lambda tc:tc._testMethodName.split("_")[2] if tc._testMethodName != "test_init" else "0")
		return result
	
	def run(self, monitor):
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
		print("---------" + case_path)
		try:
			test_suites = unittest.defaultTestLoader.discover(case_path,
														pattern="test_*.py",
														top_level_dir=None)
		except Exception as e:
			print(e)
			
		print(test_suites)

		cases = self.filter_test_cases(test_suites, filterfile, filtertype, filterstr)
		if cases == None:
			print("no test case found...")
			return

		print(len(cases))
		print(cases)
		runner = unittest.TextTestRunner()
		monitor.exec(runner, cases)

if __name__ == "__main__":
	tmonitor = TestMonitor()
	caserunner = TestCaseRunner()
	caserunner.run(tmonitor)
import time
import os
import unittest

sys.path.append('..')
sys.path.append('../..')

from utils.logger import LoggerInstance as logger 

TRY_RECOVER_TIMES = 3

class TestMonitor:
	#分析环境，未知错误的检查
	def __init__(self):
		self.faild_count = 0
		self.total_count = 0

	def reset(self):
		self.faild_count = 0
		self.total_count = 0

	def analysis_log(self, logpath):
		f = open(logpath, 'r')
		for line in f.readlines():
			line = line.strip()
		    if line.startswith('[ Failed   ]'):
				self.faild_count = self.faild_count + 1
		    	self.total_count = self.total_count + 1
			else:
				self.total_count = self.total_count + 1
		f.close()

	def analysis_env(self, logpath):
		for fpathe, dirs, fs in os.walk(logpath):
			for f in fs:
				fullpath = os.path.join(fpathe, f) 
				if os.path.isfile(fullpath) and os.path.splitext(fullpath)[1] == ".log":
					analysis_log(fullpath)

		return False

	#恢复测试环境
	def recover_env(self):
		return False

	def exec(self, testsuits):
		runner = unittest.TextTestRunner()
		for testsuit in testsuits:
			runner.run(testsuit)

			self.reset()
			self.analysis_env(logger.prefix + "/" + )

if __name__ == '__main__':
	TestMonitor().analysis_env("../")
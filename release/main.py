# -*- coding: utf-8 -*-
import sys, getopt
from utils.rpc import RPC
from utils.cli import CLI
from utils.restful import Restful
from utils.websocket import WS
from utils.logger import LoggerInstance
from utils.taskdata import *

#init doc
__doc__ = "[1] -h --help    \n[2] -t --type    \n[3] -n --test_config_name"
#end doc


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def run(connection, name):
	connection = None
	if name == "":
		for task in TaskData("tasks/rpc").tasks():
			LoggerInstance.new_log(task.name())
			connection.run(task, LoggerInstance)
	else:
		task = Task(test_name)
		LoggerInstance.new_log(task.name())
		connection.run(task, LoggerInstance)

def main(argv = None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(sys.argv[1:], "ht:n:", ["help", "type=", "name=", "long"])
		except getopt.error as msg:
			raise Usage(msg)

		test_type = ""
		test_name = ""
		#opts = [('-t', 'restful'), ('-n', 'get_blk_by_hash.json')]
		for op, value in opts:
			if op == "--long":
				wstest = WS()
				wstest.long_live_connnet()
				return 0
			if op in ("-t", "--type"):
				test_type = value
			if op in ("-n", "--name"):
				test_name = value
			if op in ("-h", "--help"):
				print(__doc__)
				return 0

		task_runner = None
		if test_type == "rpc":
			task_runner = RPC()
		elif test_type == "restful":
			task_runner = Restful()
		elif test_type == "ws":
			task_runner = WS()
		elif test_type == "cli":
			task_runner = CLI()
		else:
			raise Usage("no test name")

		if test_name == "":
			for task in TaskData("tasks/" + test_type).tasks():
				LoggerInstance.open(test_type + "/" + task.name())
				task_runner.run(task, LoggerInstance)
				LoggerInstance.close()
		else:
			task = Task(test_name)
			LoggerInstance.open(test_type + "/" + task.name())
			task_runner.run(task, LoggerInstance)
			LoggerInstance.close()

	except Usage as err:
		print >> sys.stderr, err.msg
		print >> sys.stderr, "for help use --help"
		return 2

if __name__ == "__main__":
	sys.exit(main())

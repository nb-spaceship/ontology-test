import sys, getopt
from RPC import RPCApi
from Restful import RestfulApi
from WebSocket import WSApi

#init doc
__doc__ = "[1] -h --help    \n[2] -t --type    \n[3] -n --test_config_name"
#end doc


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv = None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(sys.argv[1:], "ht:n:", ["help", "type=", "name="])
		except getopt.error, msg:
			raise Usage(msg)

		test_type = ""
		test_name = ""
		#opts = [('-t', 'restful'), ('-n', 'get_blk_by_hash.json')]
		for op, value in opts:
			if op in ("-t", "--type"):
				test_type = value
			if op in ("-n", "--name"):
				test_name = value if ".json" in value else value+'.json'
			if op in ("-h", "--help"):
				print __doc__
				return 0

		if test_type == "rpc":
			rpctest = RPCApi()
			if test_name == "":
				rpctest.runAll()
			else:
				rpctest.run(test_name)

		elif test_type == "restful":
			rftest = RestfulApi()
			if test_name == "":
				rftest.runAll()
			else:
				rftest.run(test_name)
				
		elif test_type == "ws":
			wstest = WSApi()
			if test_name == "":
				wstest.runAll()
			else:
				wstest.run(test_name)
		else:
			raise Usage("no test name")

	except Usage, err:
		print >> sys.stderr, err.msg
		print >> sys.stderr, "for help use --help"
		return 2

if __name__ == "__main__":
	sys.exit(main())

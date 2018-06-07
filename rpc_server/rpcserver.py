# -*- coding: utf-8 -*-

import leveldb
import hashlib
import socket
import urllib
import json
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from config import Configure as config

def get_db_md5(db_name):
  db = leveldb.LevelDB(db_name)
  md5 = hashlib.md5()
  iter = db.RangeIter()
  
  for (key, value) in iter:
    md5.update(key)
    md5.update(value)
  
  return md5.hexdigest()

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def con_cli(request):
  try:
    url = "http://127.0.0.1:20000/cli"
    response = requests.post(url, data=json.dumps(request), headers={'content-type': 'application/json'})
    return response.json()
  except Exception as e:
    print(e)
    return json.loads("{\"Desc\": \"Connection Error\", \"Error\": \"Connection Error\"}")


@dispatcher.add_method
def get_states_md5(**kwargs):
	"""
	Get md5 value of leveldb named states
	"""
	return get_db_md5(config.NODE_PATH + "/Chain/states")

@dispatcher.add_method
def get_block_md5(**kwargs):
	"""
	Get md5 value of leveldb named block
	"""
	return get_db_md5(config.NODE_PATH + "/Chain/block")

@dispatcher.add_method
def get_ledgerevent_md5(**kwargs):
	"""
	Get md5 value of leveldb named ledgerevent
	"""
	return get_db_md5(config.NODE_PATH + "/Chain/ledgerevent")

@dispatcher.add_method
def siginvoketx(**kwargs):
  request = {
    "Qid": "t",
    "Method": "siginvoketx",
    "Params": kwargs
  }
  return con_cli(request)

@dispatcher.add_method
def signeovminvoketx(**kwargs):
  request = {
    "Qid": "t",
    "Method": "signeovminvoketx",
    "Params": kwargs
  }
  return con_cli(request)

@dispatcher.add_method
def signativeinvoketx(**kwargs):
  request = {
    "Qid": "t",
    "Method": "signativeinvoketx",
    "Params": kwargs
  }
  return con_cli(request)

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["get_states_md5"] = get_states_md5
    dispatcher["get_block_md5"] = get_block_md5
    dispatcher["get_ledgerevent_md5"] = get_ledgerevent_md5
    dispatcher["signeovminvoketx"] = signeovminvoketx
    dispatcher["signativeinvoketx"] = signativeinvoketx
    dispatcher["siginvoketx"] = siginvoketx
    
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple(get_host_ip(), config.PORT, application)

# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from api.apimanager import API

class test_config():
	testpath = os.path.dirname(os.path.realpath(__file__))
	node_index = API.node().get_current_node()   ###7-25暂时不存在
	address=Config.NODES[node_index]["address"]
	cost1 = testpath + "/resource/cost_1.json"
	filterfile = testpath + "/resource/004.json"
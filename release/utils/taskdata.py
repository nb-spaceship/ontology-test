# -*- coding: utf-8 -*-

import os
import json

from utils.config import Config

class Task:
	def __init__(self, path = None):
		if path:
			self._taskjson = self.load_cfg(path)
		if self._taskjson:
			self._type = "";
			self._name = os.path.basename(path).replace('.json', '')
			self._data = self._taskjson

	def type(self):
		return self._type

	def name(self):
		return self._name

	def data(self):
		return self._data

	def to_json(self):
		return self._taskjson

	def load_cfg(self, cfg):
		if ".json" not in cfg:
			cfg = cfg + ".json"
		cfg_file = open(cfg, "rb")
		cfg_json = json.loads(cfg_file.read().decode("utf-8"))
		cfg_file.close()
		return cfg_json

class TaskData:
	def __init__(self, path):
		self.PATH = path

	def tasks(self):
		ret = []   
		for filename in os.listdir(self.PATH):
			fullfilename = os.path.join(self.PATH, filename)
			if os.path.isfile(fullfilename):
				ret.append(Task(fullfilename))
		return ret
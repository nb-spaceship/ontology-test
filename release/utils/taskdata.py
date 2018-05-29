# -*- coding: utf-8 -*-

import os
import json

from utils.config import Config

class Task:
	def __init__(self, path = ""):
		self.path = path
		if path:
			self._taskjson = self.load_cfg(path)
			self._name = os.path.basename(path).replace('.json', '')

		if self._taskjson:
			self._type = "";
			self._data = self._taskjson

	def path(self):
		return self.path

	def log_path(self):
		return self.path.replace('tasks/', '').replace(".json", ".log")

	def dir(self):
		return self.path.replace(os.path.basename(path), '')

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
		self.PATH = "tasks/" + path

	def tasks(self, recursive = False):
		ret = []
		if recursive:
			for filename in os.listdir(self.PATH):
				fullpath = os.path.join(self.PATH, filename)
				if os.path.isfile(fullpath) and os.path.splitext(fullpath)[1] == ".json":
					ret.append(Task(fullpath))
		else:
			for root, dirs, files in os.walk(self.PATH):
				for file in files:
					fullpath = root + "/" + file
					if os.path.isfile(fullpath) and os.path.splitext(fullpath)[1] == ".json":
						ret.append(Task(fullpath))

		return ret
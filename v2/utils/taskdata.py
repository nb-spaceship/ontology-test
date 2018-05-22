# -*- coding: utf-8 -*-

import os
import json

class TaskData:
	def __init__(self, path):
		print("path: " + path)
		self.PATH = path
		self.INDEX = 0

	def next(self):
		ret = []   
		for filename in os.listdir(self.PATH):
			fullfilename = os.path.join(self.PATH, filename)
			if os.path.isfile(fullfilename):
				ret.append(fullfilename)
				self.INDEX = self.INDEX + 1
		return ret
# -*- coding: utf-8 -*-
import urllib
import urllib.request

from utils.config import Config
import json
import os
from utils.baseapi import BaseApi

class Restful(BaseApi):
	def __init__(self):
		self.TYPE = "restful"

	def con(self, ip, api_request):
		try:
			url = ""
			if ip:
				url = "http://" + ip + ":20334"
			else:
				url = Config.RESTFUL_URL

			api_url = url + api_request["api"]
			api_command = "GET"
			if "command" in api_request:
				api_command = api_request["command"]

			if api_command == "POST":
				api_post_data = None
				if "params" in api_request:
					api_post_data = api_request["params"]
				api_post_data_encode = urllib.parse.urlencode(api_post_data).encode(encoding='UTF8')
				req = urllib.request.Request(url = api_url, data = api_post_data_encode)
				response = urllib.request.urlopen(req)
				return json.loads(response.read().decode("utf-8"))
			else:
				response = urllib.request.urlopen(api_url)
				return json.loads(response.read().decode("utf-8"))
		except Exception as e:
			return json.loads("{\"Desc\": \"Connection Error\", \"Error\": \"Connection Error\"}")
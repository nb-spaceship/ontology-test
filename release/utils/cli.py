# -*- coding: utf-8 -*-

import requests
import json
import os
from utils.config import Config
from utils.baseapi import BaseApi

class CLI(BaseApi):
    def __init__(self):
        BaseApi.TYPE = "clirpc"
        BaseApi.CONFIG_PATH = "tasks/clirpc"

    def con(self, request):
        response = requests.post(Config.CLIRPC_URL, data=json.dumps(request), headers=Config.RPC_HEADERS)
        return response.json()
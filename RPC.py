import requests
import json
import os
from config import Config
from BaseApi import BaseApi

class RPCApi(BaseApi):
    def __init__(self):
        BaseApi.TYPE = "RPC"
        BaseApi.CONFIG_PATH = "rpc"

    def connnet(self, request):
        response = requests.post(Config.RPC_URL, data=json.dumps(request), headers=Config.RPC_HEADERS)
        return response.json()
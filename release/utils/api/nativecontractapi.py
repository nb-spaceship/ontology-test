# -*- coding:utf-8 -*-
import re
import ddt
import unittest
import urllib
import urllib.request
import json
import os
import shutil
import sys
import getopt
import time
import requests
import subprocess
import tempfile

import utils.base
from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.api.commonapi import *
from utils.api.multi_sig import *

def native_transfer_ont(pay_address, get_address, amount, node_index=0, errorcode=0, gas_price=0):
    request = {
        "REQUEST": {
            "Qid": "t",
            "Method": "signativeinvoketx",
            "Params": {
                "gas_price": gas_price,
                "gas_limit": 1000000000,
                "address": "0100000000000000000000000000000000000000",
                "method": "transfer",
                "version": 1,
                "params": [
                    [
                        [
                            pay_address,
                            get_address,
                            amount
                        ]
                    ]
                ]
            }
        },
        "RESPONSE": {"error": errorcode},
        "NODE_INDEX": node_index
    }
    return call_contract(Task(name="transfer", ijson=request), twice=True)


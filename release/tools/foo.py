# -*- coding: utf-8 -*-
import sys, getopt
import time
sys.path.append('..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.commonapi import *
from utils.contractapi import *

#regIDWithPublicKey(0)
#regIDWithPublicKey(1)
#regIDWithPublicKey(2)
#regIDWithPublicKey(3)
#regIDWithPublicKey(4)
#regIDWithPublicKey(5)
#regIDWithPublicKey(6)

print(len("1234"))

strs = "qwertyuiop"
rstrs = strs[::-1]
output = ""
for i in range(0, len(strs), 2):
    output = output + rstrs[i + 1]
    output = output + rstrs[i]

print(output)
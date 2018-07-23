# -*- coding:utf-8 -*-
import unittest

from utils.error import Error

class ParametrizedTestCase(unittest.TestCase):    
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """    

    def __init__(self, methodName='runTest', param=None):    
        super(ParametrizedTestCase, self).__init__(methodName)    
        self.param = param
        self.m_result = "pass" #pass, fail, block

    def ASSERT(result, info = ""):
    	if not result:
    		self.m_result = "fail"
    		raise Error(info)

    def BLOCK(result, info = ""):
    	if not result:
    		self.m_result = "block"
    		raise Error(info)
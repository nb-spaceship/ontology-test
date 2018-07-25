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
        self.m_result = "block" #pass, fail, block
        self.m_assertcount = 0

    def setUp(self):
        self.m_assertcount = 0
        pass
                
    def result():
        if self.m_result == "block" and self.m_assertcount > 0:
            self.m_result = "pass"
        return self.m_result   

    def ASSERT(self, result, info = ""):
        self.m_assertcount = self.m_assertcount + 1
        if not result:
            self.m_result = "fail"
            raise Error(info)

    def BLOCK(self, result, info = ""):
        self.m_assertcount = self.m_assertcount + 1
        if not result:
            self.m_result = "block"
            raise Error(info)        
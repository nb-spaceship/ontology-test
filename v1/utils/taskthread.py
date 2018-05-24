# -*- coding: utf-8 -*-

import threading

class TaskThread(threading.Thread):

    def __init__(self,func,args=()):
        super(TaskThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
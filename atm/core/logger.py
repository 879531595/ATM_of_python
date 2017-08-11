#!/usr/bin/env python3

"""
@author: __Evin__
@file :  logger.py
@time :  2017/08/{10}
@email:  879531595@qq.com
需求：写日志
"""
import time
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))

def user_op_logger(user, op):
    _time = time.time()
    Logging_path = '%s\\log\\%s_op.log' % (BASE_DIR,user)
    with open(Logging_path,'a') as f:
        f.write(str(_time) + '\t' +op+'\n')

def user_transact(user, op):
    _time = time.time()
    Logging_path = '%s\\log\\%s_transact.log' % (BASE_DIR,user)
    with open(Logging_path,'a') as f:
        f.write(str(_time) + '\t' +op+'\n')



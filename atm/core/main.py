#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: __Evin__
@file :  main.py
@time :  2017/08/{10}
@email:  879531595@qq.com
"""
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from db import account_sample
from core.auth import *
from core.transaction import *

@user_auth
def login():
    print('welcome login ！！！')
    pass

def main():
    u = login()
    Transact(u,True)


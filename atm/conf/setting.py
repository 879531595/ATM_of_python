#!/usr/bin/env python3

"""
@author: __Evin__
@file :  setting.py
@time :  2017/08/{10}
@email:  879531595@qq.com
"""
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print(BASE_DIR)

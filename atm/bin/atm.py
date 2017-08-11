#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: __Evin__
@file :  atm.py.py
@time :  2017/08/{10}
@email:  879531595@qq.com
"""
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    main.main()



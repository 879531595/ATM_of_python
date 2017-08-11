#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: __Evin__
@file :  account_sample.py
@time :  2017/08/{10}
@email:  879531595@qq.com

"""
import json
import sys
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


userData = {
        'username': 'admin',
        'password': '123456',
        'limit': 15000,
        'congelation': 'yes',
        'peo': '1',
        'AlsoMoney': 0,#需还的钱
        'Money':15000,
        'create_time' : time.strftime('%Y/%m/%d',time.localtime(time.time())),
        'AlsoMoney_time' : time.strftime('%Y/%m/%d',time.localtime(time.time()+3600*24*30)),
    }
path = '%s\\db\\accounts\\admin.json' % BASE_DIR

if not os.path.exists(path):
    '''初始账号生成'''
    try:
        f = open(path,'w')
        json.dump(userData,f)
        f.close()
    except Exception as e:
        print(e)
    else:
        print('账号初始化成功')
else:
    pass

if __name__ == '__main__':
    pass
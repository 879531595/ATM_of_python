#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: __Evin__
@file :  accounts.py
@time :  2017/08/{10}
@email:  879531595@qq.com
功能：从文件中加载账户信息
"""
import json
import time
import os
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))


def getJsonData(user):
    path = BASE_DIR+'\\db\\accounts\\%s.json' % user
    if os.path.exists(path):
        f = open(path)
        data = json.load(f)
        f.close()
        return data
    else:
        # print('用户不存在！！')
        return None
def setJsonData(user,data):
    path = BASE_DIR+'\\db\\accounts\\%s.json' % user
    if os.path.exists(path):
        f = open(path,'w')
        json.dump(data,f)
        f.close()
        return 'success'
    else:
        # print('用户不存在')
        return None


def getCheckData(user):
    CheckData = {}
    Logging_path = '%s\\log\\%s_transact.log' % (BASE_DIR,user)
    with open(Logging_path,'r') as f:
        infos = f.readlines()
    for info in infos:
        _t, content = info.split('\t')
        _time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(float(_t)))
        CheckData[_time] = content.strip()

    return CheckData



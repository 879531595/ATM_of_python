#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: __Evin__
@file :  auth.py
@time :  2017/08/{10}
@email:  879531595@qq.com
"""
import json

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import logger
from core import accounts

def user_auth(func):
    def wrapper(*args,**kwargs):
        u = input('请输入账户名：')
        data = accounts.getJsonData(u)
        if data:
            if data['congelation'] == 'yes':
                for i in range(3):
                    p = input('请输入密码：')
                    if p == data['password']:
                        print('您的账户还款时间是：【%s】'%data['AlsoMoney_time'])
                        logger.user_op_logger(u,'【%s】登陆成功' % u)
                        func(*args,**kwargs)
                        return u
                    else:
                        print('密码错误！！！')
                else:
                    data['congelation'] = 'no'
                    if accounts.setJsonData(u,data):
                        print('账户【%s】被冻结')
                        logger.user_op_logger(u,'【%s】账户密码错误三次被冻结' % u)
            else:
                print('账户【%s】已被冻结，无法登陆')
        else:
            print('该账户不存在')
    return wrapper



#!/usr/bin/env python3

"""
@author: __Evin__
@file :  manage.py.py
@time :  2017/08/{10}
@email:  879531595@qq.com
所需功能：
    1、添加账号，
    2、冻结账户
    3、解冻账号

"""
import json
import time
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import logger
from core import accounts

# from db import account_sample

userData = {
    'username': '',
    'password': '',
    'limit': 15000,
    'congelation': 'yes',
    'peo': 0,
    'create_time':'',
    'AlsoMoney_time':'',
    'AlsoMoney': 0,#需还的钱
    'Money':15000,

}


# print(USER_ADD_PATH)
class Manage(object):
    def __init__(self):
        self.runMean()
    def runMean(self):
        while True:
            print("1、\t添加账户\n2、\t冻结账户\n3、\t解冻账户\n")
            choose = input('请输入你的选择：')
            if choose.isdigit():
                choose = int(choose)
                if choose in [1,2,3]:
                    if choose == 1:
                        self.fun_of_add()
                    else:
                       self.congelation(choose)
                else:
                    print('您输入的序号有误')
            elif choose == 'b':
                break
            else:
                print('请正确输入')
    def fun_of_add(self):
        '''add user'''
        userData['username'] = input('请输入你要添加账户号：')
        userData['password'] = input('请输入密码：')
        userData['limit'] = int(input('请设置账户的额度：'))
        userData['congelation'] = 'yes'
        userData['Money'] = userData['limit']
        userData['create_time'] = time.strftime('%Y/%m/%d',time.localtime(time.time()))
        userData['AlsoMoney_time'] = time.strftime('%Y/%m/%d',time.localtime(time.time()+3600*24*30))
        USER_ADD_PATH = '%s\\db\\accounts\\%s.json' %( BASE_DIR,userData['username'])

        try:
            f = open(USER_ADD_PATH,'w')
            json.dump(userData,f)
            f.close()
        except Exception as e:
            pass
        else:
            print('账号创建成功')
            logger.user_op_logger(userData['username'],'创建【%s】账号' %userData['username'])


    def congelation(self,choose):
        '''setting congelation'''
        op = {
            2:'冻结',
            3:'解冻'
        }
        user = input('请输入您要%s的账号:' % op[choose])
        data = accounts.getJsonData(user)
        if data == None:
            print('账号不存在！！')
            time.sleep(2)
        else:
            info = input('你确定要%s？（y/n）：' % op[choose])
            if info in ['y','Y'] and choose == 2:
                data['congelation'] = 'no'
                if not accounts.setJsonData(user,data) is None:
                    print('%s成功' % op[choose])

            elif info in ['y','Y'] and choose == 3:
                data['congelation'] = 'yes'
                if not accounts.setJsonData(user,data) is None:
                    print('%s成功' % op[choose])
            else:
                pass
            logger.user_op_logger(user,'【%s】进行了【%s】操作' % (user,op[choose]))







if __name__ == '__main__':
    Manage()
    pass
#!/usr/bin/env python3
"""
@author: __Evin__
@file :  transaction.py
@time :  2017/08/{10}
@email:  879531595@qq.com
消费、还钱、取钱
"""
import sys
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import logger
from core import accounts
class Transact:
    def __init__(self,user,flag):
        self.user = user
        self.data = accounts.getJsonData(user)
        if flag == True:
            self.showMean()


    def showMean(self):
        while True:
            print('1、\t还款\n2、\t套现\n3、\t余额查询\n4、\t账单查询\n5、\t转账\n')
            op = input('请输入您的操作：')
            if op.isdigit():
                op = int(op)
                if op <= 5 and op >= 1:
                    if op == 1:
                        self.fun_of_AlsoMoney()
                    elif op == 2:
                        self.fun_of_CashOut()
                    elif op == 3:
                        self.fun_of_selectMoney()
                    elif op == 4:
                        self.fun_of_selectCheck()
                    elif op == 5:
                        self.fun_of_TransferMoney()
                    else:
                        pass

                else:
                    print('Error 请输入正确选项')
            elif op == 'b':
                break
            else:
                print('Error 请正确输入')

    def fun_of_AlsoMoney(self):
        '''还款'''
        AlsoMoney = input('请输入还款额度:')
        if AlsoMoney.isdigit():
            AlsoMoney = int(AlsoMoney)
            self.data['AlsoMoney'] -= AlsoMoney
            self.data['Money'] += AlsoMoney
            if accounts.setJsonData(self.user,self.data) :
                print('还款成功！！')
            else:
                pass
        else:
            pass

    def fun_of_CashOut(self):
        '''套现'''
        print('你好，套现的利息为%5')
        choose = input('您确定要套现么？（y/n）：')
        if choose in ['y','Y']:
            Money = input('请输入套现金额：')

            if Money.isdigit():
                Money = int(Money)
                if self.data['Money'] - Money >= 0:
                    self.data['Money'] -= Money
                    self.data['AlsoMoney'] += Money
                    try:
                        accounts.setJsonData(self.user,self.data)
                    except Exception as e:
                        print(e)
                    else:
                        print('套现成功！！请收好你的现金【%s】' % (Money * 0.95))
                        logger.user_transact(self.user,'账户【%s】套现【%s】利息【%s】' %(self.user, Money, Money * 0.05))
                else:
                    print('用户余额不足')

            else:
                print('您的输入有误！！')
        elif choose in ['n','N']:
            pass
        else:
            print('您的输入有误')

    def fun_of_selectMoney(self):
        '''余额查询'''
        print('查询结果:')
        print('\t你的额度是【%s】' % self.data['limit'])
        print('\t你的可用额度是【%s】' % self.data['Money'])
        print('\t你的还账时间是【%s】' % self.data['AlsoMoney_time'])
        print('\t你的所需还账金额是【%s】' % self.data['AlsoMoney'])
        logger.user_op_logger(self.user,'账户【%s】进行了余额查询操作' % self.user)
        time.sleep(3)

    def fun_of_selectCheck(self):
        '''账单查询'''
        CheckData = accounts.getCheckData(self.user)
        print('账单信息如下：')
        for key in CheckData:
            print('\t[%s]\t[%s]' % (key,CheckData[key]))
        logger.user_op_logger(self.user,'账户【%s】进行了账单查询操作' % self.user)
        time.sleep(3)


    def fun_of_TransferMoney(self):
        '''转账'''
        to_user = input('请输入转账对象：')
        data = accounts.getJsonData(to_user)
        if data:
            Money = input('请输入转账金额：')
            if Money.isdigit():
                Money = int(Money)
                if self.data['Money'] - Money > 0:
                    self.data['AlsoMoney'] += Money
                    self.data['Money'] -= Money
                    data['AlsoMoney'] -= Money
                    data['Money'] += Money
                    try:
                        accounts.setJsonData(to_user,data)
                        accounts.setJsonData(self.user,self.data)
                    except Exception as e:
                        print(e)
                    else:
                        logger.user_transact(self.user, '账户：【%s】向账户【%s】转账【%s】金额' % (self.user,to_user,Money))
                        print('转账成功')
                else:
                    print('用户余额不足')
            else:
                print('请正确输入')
        else:
            print("转账对象不存在！！")

    def payment(self,AlsoMoney):
        '''支付接口'''
        print('欢迎使用atm支付')
        if type(AlsoMoney) in [type(1),type(1.0)]:
            for i in range(3):
                p = input('请输入密码：')
                if p == self.data['password']:
                    self.data['AlsoMoney'] += AlsoMoney
                    self.data['Money'] -= AlsoMoney
                    try:
                        accounts.setJsonData(self.user,self.data)
                    except Exception as e:
                        print(e)
                    else:
                        print('支付成功！！')
                        logger.user_transact(self.user,'【%s】账户网上支付，消费【%s】' % (self.user, AlsoMoney))
                        return True
                else:
                    print('密码输入错误')
            else:
                self.data['congelation'] = 'no'
                if accounts.setJsonData(self.user,self.data):
                    print('账户【%s】被冻结')
                    logger.user_op_logger(self.user,'【%s】账户支付时密码错误三次被冻结' % self.user)

        else:
            raise AttributeError



if __name__ == '__main__':
    # Transact('zsc',False).payment(10)

    pass
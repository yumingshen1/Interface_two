# -*- coding:utf-8 -*-
# @Time : 2022/7/15 17:43
# Auther : shenyuming
# @File : handle_zhuangshiqi.py
# @Software : PyCharm

'''
装饰器：  在不改变原函数功能和调用的基础上，增加功能
'''
import time

def show_time(func):
    def inner(*args,**kwargs):
        starttime = time.time()
        res = func(*args,**kwargs)
        endtime = time.time()
        print(f'执行时间：',endtime-starttime)
        return res      #内函数返回方法的返回值
    return inner ##外函数返回内函数对象
# -*- coding:utf-8 -*-
# @Time : 2022/6/14 22:00
# Auther : shenyuming
# @File : login.py
# @Software : PyCharm
import copy

from common.baseApi import BaseAPI
from configs.config import NAMEPASS
from utils.handle_md5 import get_hash_data

class Login(BaseAPI):
    #登录
    def login(self,inData,getToken=False):
        inData = copy.copy(inData)  #copy数据
        inData['password'] = get_hash_data(inData['password'])  #加密密码
        respData = self.request_send(inData=inData) #请求

        print('登录的数据：', respData)

        if getToken:## 获得token
            return respData['data']['token']
        else:   #响应数据
            return respData



if __name__ == '__main__':
    print(Login().login(NAMEPASS,getToken=False))
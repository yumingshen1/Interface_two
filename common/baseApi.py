# -*- coding:utf-8 -*-
# @Time : 2022/6/14 21:59
# Auther : shenyuming
# @File : baseApi.py
# @Software : PyCharm


"""
封装： 请求方法 机制+log ,  截图(ui), 一般常用方法增删改查等

项目接口不变的是 method,url :
    可在配置文件配置， .yml文件
    utils层读取，
    初始化方法中， 调用读取方法取值
    
"""
import inspect
from utils.handle_path import datas_path,config_path
import requests,os
from utils.handle_yml import get_yml_data
from configs.config import *
from utils.handle_loguru import log

class BaseAPI:
    def __init__(self,inToken=None):
        #token
        if inToken:
            self.header = {'Authorization':inToken}
        else:
            self.header = None

        ## 获得继承类的类名，所对应的yml数据
        self.data = get_yml_data(os.path.join(config_path,'apiConfig.yml'))[self.__class__.__name__]
        ## 如果是restful风格的接口，，host和url可能一样，就直接从类里获取就行，因此只写一遍，不需要inspect.stack()[1][3]在获得函数名了
        # id='' 删除接口时url拼接空字符串不影响
    def request_send(self,inData=None,json=None,param=None,file=None,id=''):
        try:
            #获得类下的函数名作为键 -----》 inspect.stack()[1][3] 获得调用该方法的函数名
            methodName = inspect.stack()[1][3]
            ## 获得 键对应的值
            print(f'{methodName}得path和method值：',self.data[methodName])
            method = self.data[methodName]['method']
            url = self.data[methodName]['path']
            resp = requests.request(method = method, url=f'{HOST}{url}{id}',data=inData,json=json,params=param,files=file,headers=self.header)

            return resp.json() #返回响应体
        except:
            raise


    def add(self):
        pass


    def delete(self):
        pass

    def update(self,inData):
        return self.request_send(inData)

    def query(self,inData):
        return self.request_send(inData)

    # 文件上传
    '''
    固定格式：  变量名是抓包的name的值
    userfile = {'变量名':(文件名，文件对象(打开文件路径)，文件类型)}
    '''
    def file_upload(self,filedir:str):
        fileName = filedir.split('/')[-1]
        fileType= filedir.split('.')[-1]
        userFile = {'file':(fileName,open(filedir,mode='rb'),fileType)}
        return self.request_send(file=userFile)


##断言
class ApiAssert:
    @classmethod
    def define_api_assert(cls,result,condition,exp_result):
        try:
            if condition == '=':
                assert result == exp_result
            elif condition == 'in':
                assert result in exp_result
        except Exception as error:
            ##日志
            raise error


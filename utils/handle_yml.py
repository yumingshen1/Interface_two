# -*- coding:utf-8 -*-
# @Time : 2022/6/14 22:30
# Auther : shenyuming
# @File : handle_yml.py
# @Software : PyCharm
import yaml,os
from utils.handle_path import config_path,datas_path

#读取yml数据
def get_yml_data(filedir):
    with open(filedir,'r',encoding='utf-8') as f:
        return yaml.safe_load(f.read())


#处理yml测试用例数据 [(),(),()]
def get_yml_caseData(fileDir):
    resList = [] #存放数据 [(),()]
    res = get_yml_data(fileDir)
    for one in res:
        resList.append((one['detail'],one['data'],one['resp']))
    return resList


if __name__ == '__main__':
    # print(get_yml_data('../configs/apiConfig.yml')
    filepath = os.path.join(datas_path,'loginCase.yml')
    print(get_yml_data(filepath))
    print(get_yml_caseData(filepath))
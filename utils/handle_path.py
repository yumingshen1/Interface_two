# -*- coding:utf-8 -*-
# @Time : 2022/6/15 23:05
# Auther : shenyuming
# @File : handle_path.py
# @Software : PyCharm

import os


# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))  ##工程路径

##工程路径          abspath 转换成绝对路径
product_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(product_path)
#配置路径
config_path = os.path.join(product_path,'configs')
# print(config_path)
#测试数据路径
datas_path = os.path.join(product_path,'data')
# print(datas_path)
#报告路径
report_path = os.path.join(product_path,'outfiles/report')
# print(report_path)
#日志路径
log_path = os.path.join(product_path,'outfiles/log')
# print(log_path)



def get_path():
    pass
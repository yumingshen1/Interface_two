# -*- coding:utf-8 -*-
# @Time : 2022/6/14 22:30
# Auther : shenyuming
# @File : handle_yml.py
# @Software : PyCharm
import yaml,os
from utils.handle_path import config_path,datas_path


def get_yml_data(filedir):
    with open(filedir,'r',encoding='utf-8') as f:
        return yaml.safe_load(f.read())




if __name__ == '__main__':
    # print(get_yml_data('../configs/apiConfig.yml')
    filepath = os.path.join(datas_path,'data_type.yml')
    print(get_yml_data(filepath))
# -*- coding:utf-8 -*-
# @Time : 2022/6/15 11:02
# Auther : shenyuming
# @File : handle_md5.py
# @Software : PyCharm

import hashlib

def get_hash_data(pwd:str):
    ##创建md5实例
    md5 = hashlib.md5()
    #调用加密方法
    md5.update(pwd.encode(encoding='utf-8'))
    return md5.hexdigest()
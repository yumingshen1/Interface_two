# -*- coding:utf-8 -*-
# @Time : 2022/6/22 16:38
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

import pytest
from libs.login import Login
from libs.shop import Shop
from configs.config import NAMEPASS


@pytest.fixture(scope='session',autouse=True)
def start_running():
    print('测试开始，，，，')
    yield
    print('测试结束，，，')


@pytest.fixture(scope='session',autouse=False)
def login_init():
    print('fixtrue登陆')
    _token = Login().login(NAMEPASS,getToken=True)
    yield _token
    print('fixtrue登录完成')


@pytest.fixture(scope='class',autouse=False)
def shop_init(login_init):
    print('fixtrue店铺实例开始')
    shopPage = Shop(login_init)
    yield shopPage
    print('fixtrue店铺实例结束')
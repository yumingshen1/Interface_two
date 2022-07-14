# -*- coding:utf-8 -*-
# @Time : 2022/6/29 16:42
# Auther : shenyuming
# @File : handle_mock.py
# @Software : PyCharm

'''
jar+配置文件： moco.jar+xxx.json
moco一个类似mock的工具框架，jar包，
xx.json文件：是写好的接口参数，入参，出参

准备一个xx.sh文件，写入命令：java -jar moco-runner-1.1.0-standalone.jar http -p 9999 -c test.json
moco-runner-1.1.0-standalone.jar： moco的包名，
http： 协议
-p 9999： 定义的端口
-c test.json： 配置文件--> 数据
'''
## 本机启动 moco.jar 后的地址
HOST= "http://127.0.0.1:9999"
import requests
##不带参数的
def test1():
    res = requests.get(url=f'{HOST}/xintian_1')
    print(res.text)

#带参数的
def test2():
    payload= {
        "key1": "abc",
        "key2": "123"
    }
    res2 = requests.get(url=f'{HOST}/sym',params=payload)
    print(res2.text)

#froms表单的 ，json配置文件是froms的入参
def test3():
    payload = {
        "key1": "abc"
    }
    res3 = requests.get(url=f'{HOST}/sq2', data=payload)
    print(res3.text)


##json格式的, json配置文件是json格式的入参
def test4():
    payload = {
        "key1":"value1",
		"key2":"value2"
    }
    res4 = requests.get(url=f'{HOST}/sq3', json=payload)
    print(res4.text)


if __name__ == '__main__':
    test4()

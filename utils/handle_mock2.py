# -*- coding:utf-8 -*-
# @Time : 2022/6/29 20:27
# Auther : shenyuming
# @File : handle_mock2.py
# @Software : PyCharm
''''
main中都是主线程 ，
只有threading.Thread(target=被作为子线程的函数名,args=(函数的变量)) 是子线程

主线程停止，子线程也就停止，，，
'''

import threading

HOST= "http://127.0.0.1:9999"
import requests,time

##创建订单
def cread_order(jsondata):
    method ='POST'
    payload = jsondata
    resp = requests.request(url=f'{HOST}/api/order/create/',method=method,json=payload)
    # resp = requests.post(url=f'{HOST}/api/order/create/',json=payload)
    return resp.json()

##查询订单
def get_order(orderid,interval=3,timeout=20):
    starttime = time.time()  #开始时间
    endtime = starttime + timeout  #结束时间
    payload = {'order_id': orderid}
    con= 1
    while time.time() < endtime:
        resp2 = requests.get(url=f'{HOST}/api/order/get_result_1/',params=payload)
        if resp2:
            print(f'第{con}次查询,查询到，结束')
            break
        else:
            print(f'第{con}次查询,没查到，继续查')
        time.sleep(interval)
        con += 1
    print('查询结束！！！')

if __name__ == '__main__':
    starttime = time.time()
    jsondata = {
        "user_id": "sq123456",
        "goods_id": "20200815",
        "num": 1,
        "amount": 200.6
    }
    res = cread_order(jsondata)
    orderid = res['order_id']
    print(res)

    ##开启单个线程
    #-----get_order()设置成子线程------target=函数名(被当做子线程的函数）----args=元组（函数需要使用的变量）------)
    t1 = threading.Thread(target=get_order,args=(orderid,))
    #主线程结束或异常退出，子线程强制结束
    t1.setDaemon(True)  #守护进程
    t1.start()  #开启子线程

    ##开启多个子线程
    # threadinglist = []
    # for i in range(10):
    #     threadinglist.append(threading.Thread(target=get_order,args=(orderid,)))
    # for one in threadinglist:
    #     one.setDaemon(True)
    #     one.start()

    ##其他业务代码
    for i in range(10):
        time.sleep(1)
        print(f'{i}---执行其他代码业务')

    endtime = time.time()
    print('整个自动化测试时间：',endtime-starttime)
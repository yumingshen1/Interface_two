# -*- coding:utf-8 -*-
# @Time : 2022/6/21 15:51
# Auther : shenyuming
# @File : shop.py
# @Software : PyCharm
import os
from common.baseApi import BaseAPI
from libs.login import Login
from configs.config import NAMEPASS
from utils.handle_path import datas_path

class Shop(BaseAPI):

    def add(self):
        pass

    '''
        店铺id从用例取， 但是需要修改值，
        需要传入图片，调用文件上传
    '''
    def update(self,inData,shopID,fileInfo):

        if inData['id'] == 'id不存在的值':   #如果用例中写如反向测试用例，就不改id的值
            inData['id'] = '00000'
        else:
            #更新店铺id
            inData['id'] = shopID
        #更新文件信息
        inData['image_path'] =fileInfo
        inData['image'] =f'/file/getImgStream?fileName={fileInfo}'

        return super(Shop,self).update(inData) ## 调动父类的方法，子类本身不具备发送请求



if __name__ == '__main__':
    ##列出店铺
    token = Login().login(NAMEPASS,getToken=True)
    shop = Shop(token)
    data = {"page":1,"limit":20}
    res = shop.query(data)
    print('shop列表的返回值',res)

    #获得店铺id
    shopid = res['data']['records'][0]['id']
    print('店铺ID：',shopid)

    #上传文件
    res2 = shop.file_upload(os.path.join(datas_path,'test_1.jpg'))
    realFileName = res2['data']['realFileName']
    print('添加图片返回realFileName值：',realFileName)

    # 更新店铺
    inData = {
            "name": "dsddsds",
            "address": "上海市静安区秣陵路303号",
            "id": "3269",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }
    res3 = shop.update(inData,shopid,realFileName)
    print(res3)
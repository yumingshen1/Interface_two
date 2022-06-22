# -*- coding:utf-8 -*-
# @Time : 2022/6/22 15:45
# Auther : shenyuming
# @File : test_shop.py
# @Software : PyCharm
import pytest,os,allure

from utils.handle_path import report_path,datas_path
from utils.handles_excel import get_excel_data
from common.baseApi import ApiAssert

@allure.epic('测试-商品')
@allure.feature('测试-shop接口')
class TestShop:
    @allure.story('列出商品')
    @allure.title('{title}')
    @pytest.mark.parametrize('title,inData,expData',get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    def test_shop_list(self,title,inData,expData,shop_init):
        res = shop_init.query(inData)
        #断言
        ApiAssert().define_api_assert(res['code'],'=',expData['code'])


    @allure.story('商品修改')
    @allure.title('{title}')
    @pytest.mark.parametrize('title,inData,expData', get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    def test_shop_update(self,title,inData,expData,shop_init):
        with allure.step('1,登录'):
            pass
        with allure.step('2,获得店铺id'):
            data = {"page": 1, "limit": 20}
            res = shop_init.query(data)
            shopID =  res['data']['records'][0]['id']
        with allure.step('3,上传文件'):
            res2 = shop_init.file_upload(os.path.join(datas_path,'test_1.jpg'))
            realFileName = res2['data']['realFileName']
        with allure.step('4,更新店铺'):
            res3 = shop_init.update(inData,shopID,realFileName)
        with allure.step('5,断言'):
            ApiAssert.define_api_assert(res3['code'],'=',expData['code'])




if __name__ == '__main__':
    pytest.main(['test_shop.py','-sq','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')
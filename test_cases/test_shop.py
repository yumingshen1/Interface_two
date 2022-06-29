# -*- coding:utf-8 -*-
# @Time : 2022/6/22 15:45
# Auther : shenyuming
# @File : test_shop.py
# @Software : PyCharm
import pytest,os,allure
from libs.login import Login
from utils.handle_path import report_path,datas_path
from utils.handles_excel import get_excel_data
from utils.handle_yml import get_yml_caseData
from common.baseApi import ApiAssert
from configs.config import NAMEPASS

@allure.epic('测试-商品')
@allure.feature('测试-shop接口')
# @pytest.mark.skipif(not Login().login(NAMEPASS),reason='条件为真，跳过')
@pytest.mark.shop
class TestShop:
    @allure.story('商品列表')
    @allure.title('{title}')
    # @pytest.mark.parametrize('title,inData,expData',get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @pytest.mark.parametrize('title,inData,expData',get_yml_caseData(os.path.join(datas_path,'listshopCase.yml')))
    @pytest.mark.shop_list
    def test_shop_list(self,title,inData,expData,shop_init):
        res = shop_init.query(inData)
        #断言
        if not expData['code']:
            ApiAssert().define_api_assert(res['error'], '=', expData['error'])
        else:
            ApiAssert().define_api_assert(res['code'],'=',expData['code'])


    @allure.story('商品修改')
    @allure.title('{title}')
    # @pytest.mark.parametrize('title,inData,expData', get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    @pytest.mark.parametrize('title,inData,expData', get_yml_caseData(os.path.join(datas_path,'updateshop.yml')))
    @pytest.mark.shop_update
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
    pytest.main(['test_shop.py','-sq','-m','shop_update','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')
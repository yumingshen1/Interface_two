# -*- coding:utf-8 -*-
# @Time : 2022/6/16 10:46
# Auther : shenyuming
# @File : test_login.py
# @Software : PyCharm


import pytest,allure,os
from libs.login import Login
from utils.handle_path import report_path,datas_path
from utils.handles_excel import get_excel_data
from utils.handle_yml import get_yml_caseData
from common.baseApi import ApiAssert

@allure.epic('接口测试-登录')
@allure.feature('登录模块的接口测试')
class TestLogin:

    @allure.story('登录测试')
    @allure.title('{title}')
    # @pytest.mark.parametrize('title,inData,expData',get_excel_data('登录模块','Login','标题','请求参数','响应预期结果'))
    @pytest.mark.parametrize('title,inData,expData',get_yml_caseData(os.path.join(datas_path,'loginCase.yml')))
    def test_login(self,title,inData,expData):
        res = Login().login(inData)
        #断言
        # assert res['msg'] == expData['msg']
        ApiAssert.define_api_assert(res['msg'],'=',expData['msg'])

if __name__ == '__main__':
    pytest.main(['test_login.py','-sq','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')
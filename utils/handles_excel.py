# -*- coding:utf-8 -*-
# @Time : 2022/6/16 11:01
# Auther : shenyuming
# @File : handles_excel.py
# @Software : PyCharm
"""
xlrd 读
xlet 新建写
xlutils 在已有的文件写
"""
import xlrd,os
from utils.handle_path import datas_path

def get_excel_data(sheetName=None,caseName=None,*args,runCase=['all'],exceldir=None):

    '''
    :param exceldir:   excel地址
    :param sheetName:  sheet 名 （登录，商品等）
    :param caseName: 模块下的用例名，例如登录模块下的，登录，非退出
    :param args:  excel用例的哪几个字段 （地址、参数、预期结果等）
    :param runCase: 筛选用例，列表给是
    :return:
    '''
    exceldir = os.path.join(datas_path,'test_devolop.xls')
    resList = []  #存放用例数据

    #打开一个文件返回一个文件对象     formatting_info保持原样式打开
    workbook = xlrd.open_workbook(exceldir,formatting_info=True)

    #获取所有的sheet
    sheets = workbook.sheet_names()
    # print(sheets)

    ##h获取需要操作的子表
    workSheet = workbook.sheet_by_name(sheetName)
    ##获得操作子表的第一列
    # print(workSheet.col_values(0))
    #获得操作子表的第一行
    # print(workSheet.row_values(0))

    ##读取单元格数据
    # print(workSheet.cell(0, 0).value)


    ## -----获得*args的数据----> 测试用例 列--------------
    colIndex = []  # 存放列-- 用例需要那几列
    for i in args:
        row_index = workSheet.row_values(0).index(i)
        colIndex.append(row_index)
    print('读取测试用例-->列',colIndex)

    ## ------测试用例筛选------runCase = ['all','003','003-007']-------------
    runList = []
    if 'all' in runCase:
        runList = workSheet.col_values(0) #选择全部用例
    else: #筛选
        for one in runCase:     #循环筛选用例
            if '-' in one:  #连续
                start,end = one.split('-')   #字符串，闭区间
                for i in range(int(start),int(end)+1):
                    runList.append(caseName+f'{i:0>3}')
            else:
                runList.append(caseName+f'{one:0>3}')

    ##获取测试数据
    rowNum=0  #从第一行开始循环
    for one in workSheet.col_values(0):         #one in runList: 判断是否在在所筛选的用例中
        if caseName in one and one in runList: ## 判断每个模块的测试用例名称是否在本列，登录的只获取登录的，退出的只获取退出的
            get_colData = []    #存每一列的数据
            for num in colIndex:    ##循环args的列 下标
                temp = workSheet.cell(rowNum,num).value     # 获取每一个单元格内容
                if is_json(temp):   #json转字典
                    temp = json.loads(temp)
                get_colData.append(temp)            # 将每一列的数据存入list
            resList.append(tuple(get_colData))      # 将所有列数据存入list

            # reqdata = workSheet.cell(rowNum,9).value
            # respdata = workSheet.cell(rowNum,11).value
            # resList.append((reqdata,respdata)) # [(),()] 符合pytest参数化格式
        rowNum+=1
    # print(resList)
    for i in resList:
        print('获取所需数据：',i)
    return resList

## ----判断数据是否可以转成json
import json
def is_json(inData):
    try:
        json.loads(inData)  #是否可以转字典
        return True     #是json
    except:
        return False


if __name__ == '__main__':
    filepath = os.path.join(datas_path,'test_devolop.xls')
    # get_excel_data(filepath,'登录模块','Login','标题','请求参数','响应预期结果',runCase=['001','02-4','all'])

    get_excel_data('登录模块','Login','标题','请求参数','响应预期结果',runCase=['001','02-4','all'])
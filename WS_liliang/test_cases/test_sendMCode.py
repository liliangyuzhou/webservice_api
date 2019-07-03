#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_sendMCode.py
# @Author: LILIANG
# @Date  : 2019/7/1
# @Desc  :  test

import unittest
from common.do_excel import DoExcel
from common import constants
from common.logger import mylogger
logger=mylogger(__name__)
from common.do_mysql import DoMysql
import warnings
from ddt import ddt,data
from common.ws_https import HttpRequests
from common.context import *
from common.context import CheckSql

@ddt
class TestSendMCode(unittest.TestCase):
    excel=DoExcel(constants.case_files,'sendMCode')
    cases=excel.get_cases()
    @classmethod
    def setUpClass(cls):
        logger.info('测试前置，连接数据库')
        cls.mysql=DoMysql()
        warnings.simplefilter('ignore',ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置，关闭数据库')
        cls.mysql.close_mysql()

    @data(*cases)
    def test_SendMCode(self,case):
        logger.info("测试用例的标题是{0}".format(case.title))
        data=replace(case.data)

        logger.info(("替换data中的参数化值，并用data接收，返回的data的值是{0}".format(data)))
        resp=HttpRequests().Wshttps(case.url,data,case.method)
        try:
            self.assertEqual(case.expected,resp)
            if case.case_id==1:
                code=CheckSql(self.mysql).query_mvcode(eval(data)['mobile'])
                self.assertIsNotNone(code)
            self.excel.writeResult(case.case_id+1,str(resp),'PASS')
        except AssertionError as e:
            self.excel.writeResult(case.case_id+1,str(resp),'FAIL')



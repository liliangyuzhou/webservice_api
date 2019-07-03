#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_verifyUserAuth.py
# @Author: LILIANG
# @Date  : 2019/7/2
# @Desc  :  test
import unittest
from common.do_excel import DoExcel
from common.constants import *
from ddt import ddt,data
from common.ws_https import HttpRequests
from common.context import *
from common.do_mysql import DoMysql
import warnings
from common.logger import mylogger
from common.context import CheckSql
logger=mylogger(__name__)
@ddt
class TestVerifyUserAuth(unittest.TestCase):


    excel=DoExcel(case_files,'verifyUserAuth')
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info('前置操作，连接数据库')
        cls.mysql=DoMysql()
        warnings.simplefilter('ignore',ResourceWarning)



    @classmethod
    def tearDownClass(cls):
        cls.mysql.close_mysql()

    @data(*cases)
    def test_verifyUserAuth(self,case):
        logger.info("测试执行，测试用例的名称是{}".format(case.title))
        data=replace(case.data)
        resp=HttpRequests().Wshttps(case.url,data,case.method)
        try:
            self.assertEqual(case.expected,resp)
            if case.case_id ==1:
                code=CheckSql(self.mysql).query_mvcode(eval(data)['mobile'])
                setattr(Context,'code',code)

            if case.case_id ==2:
                uuid = CheckSql(self.mysql).query_uuid(eval(data)['user_id'])
                setattr(Context, 'uuid', str(uuid))

            logger.info('测试通过，测试结果回写excel')
            self.excel.writeResult(case.case_id+1,str(resp),'PASS')

        except AssertionError as e:
            logger.info('测试失败，测试结果回写excel')
            self.excel.writeResult(case.case_id+1,str(resp),'FAIL')
            raise e




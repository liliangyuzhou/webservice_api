#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_userRegister.py
# @Author: LILIANG
# @Date  : 2019/6/28
# @Desc  :  test

from  common import logger
import unittest
from common.do_excel import DoExcel
from common.constants import *
from ddt import ddt,data
from common.context import *
from common.do_mysql import DoMysql
import warnings
from common.ws_https import  HttpRequests
logger=logger.mylogger(__name__)

@ddt
class TestUserRegister(unittest.TestCase):

    excel = DoExcel(case_files, 'userRegister')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.mysql = DoMysql()
        warnings.simplefilter("ignore", ResourceWarning)

    @data(*cases)
    def test_register(self,case):

        data=replace(case.data)

        resp=HttpRequests().Wshttps(case.url,data,case.method)
        print(resp)

        # 断言
        try:
            self.assertEqual(case.expected, resp)

            if case.case_id == 1:
                # 将短信验证码保存到Context中
                code = CheckSql(self.mysql).query_mvcode(eval(data)['mobile'])
                print(code)
                setattr(Context, 'code', code)

            if case.case_id == 2:
                # 判断注册成功后，数据库是否有新增数据
                uuid =CheckSql(self.mysql).query_uuid(eval(data)['user_id'])
                self.assertIsNotNone(uuid)

            self.excel.writeResult(case.case_id + 1, str(resp), 'PASS')

        except AssertionError as e:
            self.excel.writeResult(case.case_id + 1, str(resp), 'FAIL')
        logger.info("结束执行：{0}".format(case.title))

    @classmethod
    def teardownclass(cls):
        cls.mysql.close_mysql()


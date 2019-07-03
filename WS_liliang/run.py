#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py.py
# @Author: LILIANG
# @Date  : 2019/6/17
# @Desc  :  test

import unittest
from common import HTMLTestRunnerNew
from common.constants import *

discover=unittest.defaultTestLoader.discover(testcases_files,'test_*.py')
with open(report_files+'/report.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner( stream=file,
                                             verbosity=2,
                                             title='WS',
                                             description='test webservice',
                                             tester='liliang')
    runner.run(discover)
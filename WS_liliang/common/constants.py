#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : constants.py
# @Author: LILIANG
# @Date  : 2019/6/18
# @Desc  :  test

import os

# base_dir=os.path.abspath(__file__)
# print(base_dir)


base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

global_file=os.path.join(base_dir,'conf','global.cfg')

online_file=os.path.join(base_dir,'conf','online.cfg')

test_file=os.path.join(base_dir,'conf','global.cfg')

log_file=os.path.join(base_dir,'logs')

case_files=os.path.join(base_dir,'data','case1.xlsx')

report_files=os.path.join(base_dir,'report')

testcases_files=os.path.join(base_dir,'test_cases')
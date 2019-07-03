#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : logger.py
# @Author: LILIANG
# @Date  : 2019/6/17
# @Desc  :  test


import logging
from common import constants
from common.config import config
def mylogger(name):

    #新建日志收集器
    logger=logging.getLogger(name)
    #设置日志的输出级别
    logger.setLevel('DEBUG')

    # fmt = ('%(asctime)s-%(name)s-%(levelname)s-日志信息:%(message)s- [%(filename)s:%(lineno)d ]')
    # formatter = logging.Formatter(fmt=fmt)

    formatter = logging.Formatter(config.get('logger','fmt'))




    #新建日志输出器
    #指定日志输出到控制台
    sh=logging.StreamHandler()
    sh.setLevel('DEBUG')
    sh.setFormatter(formatter)



    #指定日志输出到文件中
    fh=logging.FileHandler(constants.log_file+'/case.log',encoding='utf-8',mode='w')
    fh.setLevel('DEBUG')
    fh.setFormatter(formatter)

    #将日志输出器和日志输出器配合使用
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger





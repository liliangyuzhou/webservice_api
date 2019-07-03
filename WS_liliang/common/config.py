#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: LILIANG
# @Date  : 2019/6/18
# @Desc  :  test


"""
这里读取配置文件错误，将configparser.ConfigParser换成configparser.RawConfigParser
这个类里面的方法,解决了从.cfg配置文件中读取fmt日志输出格式错误的问题：
configparser.InterpolationMissingOptionError: Bad value substitution
"""
import configparser
from common import constants
# from common import logger
# logger=logger.my_logger(__name__)
#这里因为read方法encoding='utf-8'，没有写，并且logger以及config相互使用，一直报错导包错误，自己要谨记
class ReadConfig:

    def __init__(self):
       self.config=configparser.RawConfigParser()
       self.config.read(constants.global_file)
       switch=self.config.getboolean('switch','on')
       if switch:
           self.config.read(constants.online_file,encoding='utf-8')
           # logger.info('读取现网测试环境配置文件')
       else:
           self.config.read(constants.test_file,encoding='utf-8')
           # logger.info('读取测试环境配置文件')

    def get(self,section,option):
        return self.config.get(section,option)
config=ReadConfig()


if __name__ == '__main__':
    s=config.get('logger', 'fmt')
    print(s)

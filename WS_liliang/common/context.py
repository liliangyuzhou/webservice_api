#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : context.py
# @Author: LILIANG
# @Date  : 2019/6/21
# @Desc  :  test

import re
from common.config import config

class CheckSql:
    def __init__(self,mysql):
        self.mysql=mysql

    def query_mvcode(self,mobile):
        db_name=mobile[9:11]
        table_name=mobile[8]
        sql='select * from sms_db_{0}.t_mvcode_info_{1} where Fmobile_no="{2}"'.format(db_name,table_name,mobile)
        print(sql)
        row=self.mysql.fetch_one(sql)
        if row:
            return row["Fverify_code"]
        return

    def query_uuid(self, reg_name):
        sql = 'select * from user_db.t_user_info where fuser_id = "{0}"'.format(reg_name)
        row = self.mysql.fetch_one(sql)
        if row:
            return row["Fuid"]
        return


class Context:
    param=None
    register_ip='127.0.0.1'
    register_mobile='13172545378'
    register_name='张红红'
    auth_uid='610502199809217624'
    auth_id=1234567

def replace(data):
    """
    替换文中所有符合替换的字符串
    :param data: data
    :return:
    """
    p='#(.*?)#'    #正则表达式
    while re.search(p,data):
        match=re.search(p,data) #从任意位置开始查找，找到第一个就返回Match object，没有就返回None

        param=match.group(1) # 拿到参数化的key
        if hasattr(Context,param):
            v=getattr(Context,param)
        else:
            v=eval('get_{0}()'.format(param))
            setattr(Context,param,v)

        #替换后的内容，继续用data接收

        data=re.sub(p,v,data,count=1)  #替换查找出的符合p的字段，替换后继续用data接收，返回data，每执行一次，只替换一次，知道不满足while条件
    return data

import random

def get_mobile():
    """
    随机生成手机号
    :return:
    """
    suffix=config.get('db','table_name')+config.get('db','db_name')
    prefix=['158', '136', '130', '131', '132', '133', '149', '134', '150', '152', '153']
    middle=random.randint(10000,99999)
    mobile=random.choice(prefix)+str(middle)+suffix
    return mobile


def get_ip():
    """
    调用本地ip
    :return:
    """
    return '127.0.0.1'

from faker import Faker

def get_reg_name():
    """
    主要用来创建伪数据，使用Faker包，无需再
    手动生成或者手写随机数来生成数据，只需要调用Faker提供的方法，即可完成数据的生成。

    :return:  随机生成的姓名
    """
    f=Faker(locale='zh_CN')
    return f.name()

def get_cre_id():
    """
    生成随机的身份号
    :return: 随机身份证号
    """
    f=Faker(locale='zh_CN')
    return f.ssn()




#
#
# def get_cre_id():
#     f = Faker(locale='zh_CN')
#     return f.ssn()


if __name__ == '__main__':
    prefix = ['158', '136', '130', '131', '132', '133', '149', '134', '150', '152', '153']
    s=random.choice(prefix)
    print(s)


    s=get_mobile()
    print(s)


    s1=get_reg_name()
    print(s1)

    s2=get_cre_id()
    print(s2)

    s='13089076543'
    str=s[8]
    print(str)


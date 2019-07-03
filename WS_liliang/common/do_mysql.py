#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : do_mysql.py
# @Author: LILIANG
# @Date  : 2019/6/21
# @Desc  :  test

import pymysql
from common.config import config
from common.logger import mylogger

logger=mylogger(__name__)


class DoMysql:
    #完成与数据库的交互

   def __init__(self):
       # 把这些参数放到配置文件里面去做，然后在这里读取配置文件
       host =config.get("mysql","host")
       user =config.get("mysql","user")
       password =config.get("mysql","password")
       port = int(config.get("mysql","port"))
       # 创建连接
       logger.info("连接sql")
       self.mysql=pymysql.Connect(host=host,user=user,password=password,port=port,charset='utf8')
       # 创建游标，设置返回字典
       self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor) #创建此类浮标，查询结果返回的是一个字典
       # self.cursor = self.mysql.cursor()  #创建此类浮标，查询结果返回的是一个元组

   def fetch_one(self,sql):
        logger.info("执行sql")
        self.cursor.execute(sql)
        self.mysql.commit()
        logger.info(self.cursor.rowcount)
        return self.cursor.fetchone()
   #执行次函数会返回查询结果的第一条数据


   def fetch_all(self,sql):
       logger.info("执行sql")
       self.cursor.execute(sql)
       return self.cursor.fetchall()
    #初始化中浮标设置元组类型执行此语句返回的是元组套元组
    #初始化中浮标设置的是字典类型执行此语句返回的是列表套字典


   def close_mysql(self):
       logger.info("关闭查询页面（浮标）")
       self.cursor.close()
       logger.info("关闭数据库")
       self.mysql.close()


# if __name__ == '__main__':
#     mysql = DoMysql()
#     result1 = mysql.fetch_one('select max(mobilephone) from future.member')  # 返回一条数据，元组
#     print(type(result1), result1)
#     result2 = mysql.fetch_all('select * from future.member limit 10')  # 返回多条数据的时候，元组里面套元组
#     print(type(result2), result2)
#     mysql.close_mysql()

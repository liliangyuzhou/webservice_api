#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ws_https.py
# @Author: LILIANG
# @Date  : 2019/6/17
# @Desc  :  test

import suds
from suds.client import Client
from common import logger
logger=logger.mylogger(__name__)
from common.config import config

"""
注：这里日志输出只能用format格式输出，不然 Logging error
正确：logger.info("返回信息：{}".format(resp.retInfo))
错误：logger.info("返回信息：{}",resp.retInfo)
"""
class HttpRequests:

    def Wshttps(self,url,data,method):
        logger.info("实例化一个client对象")
        # 拼接URL
        self.url =config.get('api', 'pre_url') + url
        self.method = method
        self.data = eval(data)
        logger.info('请求URL：{0}'.format(self.url))
        logger.info('请求METHOD：{0}'.format(self.method))
        logger.info('请求DATA：{0}'.format(self.data))

        client=Client(self.url)
        try:
            logger.info("发送一个webservice请求")
            resp=eval("client.service.{0}({1})".format(self.method,self.data))

            msg=resp.retInfo
            logger.info("返回信息：{}".format(resp.retInfo))
            logger.info("返回码：{}".format(resp.retCode))

        except suds.WebFault as e:
            logger.info(e.fault.faultstring)
            msg=e.fault.faultstring
        return msg


if __name__ == '__main__':

    # url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
    # data = {"uid": 100010710, "true_name": "张三", "cre_id": "43041219900729002Z"}
    # method='verifyUserAuth'
    # http_request = HttpRequests()
    # resp=http_request.Wshttps(url,data,method)
    # print(resp)


    url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
    data = {'verify_code': '198191', 'user_id': 'register_name', 'channel_id': '2', 'pwd': '1234567', 'mobile': '15239416848', 'ip': '127.0.0.1'}
    method='userRegister'
    http_request = HttpRequests()
    resp=http_request.Wshttps(url,data,method)
    print(resp)
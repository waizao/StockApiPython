#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/1/1 18:11
Desc: 歪枣网，财经数据库
http://www.waizaowang.com/
"""

import requests


def getDayKLine(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, token: str,
                filter: str, export: int, method: str = "post") -> str:
    """
    巨潮资讯-数据中心-评级预测-投资评级
    :param method:
    :param export:
    :param filter:
    :param date: 查询日期
    :type date: str
    :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getDayKLine"
    params = {"type": type, "code": code, "ktype": ktype, "fq": fq, "startDate": startDate, "endDate": endDate,
              "fields": fields, "token": token, "filter": filter, "export": export}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text


if __name__ == "__main__":
    print("http://www.waizaowang.com")

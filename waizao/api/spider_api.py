#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/1/1 18:11
Desc: 歪枣网，财经数据库
http://www.waizaowang.com/
"""
import re
import time

import requests


def get_pankou(codes="sz000001,sh600000,bj833171"):
    """
    买卖五档，盘口数据
    纯爬虫接口，完全免费使用，歪枣网不校验权限也不存储任何数据，若用于商业，请合规使用。
    :param codes      : 传入股票代码
    """

    root_url = "https://hq.sinajs.cn/rn=%s&list=%s" % (str(int(time.time() * 1000)), codes)
    response = requests.get(root_url,
                            headers={
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
                                'host': 'hq.sinajs.cn',
                                'referer': 'https://finance.sina.com.cn/'
                            })
    text = response.content.decode('GBK')
    reg = re.compile(r'\="(.*?)\";')
    data = reg.findall(text)
    data_list = []
    for index, row in enumerate(data):
        if len(row) > 1:
            data_list.append([astr for astr in row.split(',')[:33]])
    return data_list

if __name__ == "__main__":
    print("sz000001,sh600000,bj833171")

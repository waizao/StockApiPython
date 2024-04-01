"""
歪枣网终于和大家见面了，非常感谢有大家的一路支持！
歪枣网提供的财经数据下载接口，主要用于财经研究，解决大家在财经研究中数据获取的问题。
通过歪枣网，能快速获取沪深股票、港股、大盘指数、基金净值、基金排行等财经数据，财经接口将提供Txt、Gson、Csv文件等多种数据形式，方便分析人员快速分析数据。
力求给大家提供更高效、全面、稳定的财经数据服务，让大家不用再担心财经数据源，专心进行策略研究，提升投资收益。
希望歪枣网提供的财经数据接口能给大家在投资上带来些许方便，在探索财富奥秘、追求财富自由的道路上，也希望有大家相伴。
"""

__version__ = "1.1.2"
__author__ = "waizaowang"

import sys
import warnings

import pandas as pd

pd_main_version = int(pd.__version__.split('.')[0])

if pd_main_version < 2:
    warnings.warn(
        "为了支持更多特性，请将 Pandas 升级到 2.1.0 及以上版本！"
    )

if sys.version_info < (3, 9):
    warnings.warn(
        "为了支持更多特性，请将 Python 升级到 3.9.0 及以上版本！"
    )

del sys

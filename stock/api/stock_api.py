#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/1/1 18:11
Desc: 歪枣网，财经数据库
http://www.waizaowang.com/
"""

import requests


def getBaseInfo(type: int, code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股、沪深京B股、港股、美股、黄金、汇率、Reits、沪深指数、香港指数、全球指数、债券指数、场内基金、沪深债券、行业板块、概念板块、地域板块等范围列表。其中行业数据包括行业板块、概念板块、地域板块；场内基金包括ETF基金和LOF基金。可根据股票代码，调用通用接口中的每日行情、分线数据、时线数据、日线数据等接口。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBaseInfo"
    params = {"type": type,"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockType(flags: int, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    将沪深京股票分类，方便大家根据股票类别获取对应的股票集。包括上证A股、深证A股、北证A股、沪深京B股、新股、创业板、科创板、沪股通(港>沪)、深股通(港>深)、风险警示股票、港股通(沪>港)、港股通(深>港)等类型。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param flags     : 分类标记，取值范围：1|上证A股；2|深证A股；3|北证A股；4|沪深京B股；5|新股；6|创业板；7|科创板；8|沪股通(港>沪)；9|深股通(港>深)；10|st股票；11|港股通(沪>港)；12|港股通(深>港)；13|注册制上证A股；14|核准制上证A股；15|注册制深证A股；16|核准制深证A股；17|主板港股；18|创业板港股；19|知名港股；20|蓝筹港股；21|红筹港股；22|国企港股；23|知名美股；24|中概美股；25|粉单市场
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockType"
    params = {"flags": flags,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getTradeDate(mtype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    股票市场交易日历，包括沪深京股票、港股通、沪股通(港>沪)、港股。沪深港通-北向，包括沪股通(港>沪)、深股通(港>深)；沪深港通-南向，包括港股通(沪>港)、港股通(深>港)。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param mtype     : 市场类型，取值范围：1|沪深京A股；2|港股；3|沪深港通-北向；4|沪深港通-南向
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getTradeDate"
    params = {"mtype": mtype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorMoney(type: int, code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    资金情况，数据范围包括沪深京A股、港股、美股、沪深指数、场内基金、行业板块、概念板块、地域板块。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；3|港股；4|美股；10|沪深指数；20|场内基金；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorMoney"
    params = {"type": type,"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorBaseInfo(type: int, code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    基本指标，数据范围包括沪深京A股、港股、美股、场内基金。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；3|港股；4|美股；20|场内基金
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorBaseInfo"
    params = {"type": type,"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getDailyMarket(type: int, code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。每日行情数据，数据范围包括沪深京A股、沪深京B股、港股、美股、黄金、汇率、Reits、沪深指数、香港指数、全球指数、债券指数、场内基金、沪深债券、行业板块、概念板块、地域板块。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getDailyMarket"
    params = {"type": type,"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getMinuteKLine(type: int, code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    分线数据，数据以分钟为粒度。数据均为不复权数据。数据范围包括沪深京A股、沪深京B股、港股、美股、场内基金、沪深债券，提供开盘竞价数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getMinuteKLine"
    params = {"type": type,"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHourKLine(type: int, code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    时线数据，提供5分钟、15分钟、30分钟、60分钟数据。数据均为不复权数据。数据范围包括沪深京A股、沪深京B股、港股、美股、沪深指数、香港指数、全球指数、债券指数、场内基金、沪深债券。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHourKLine"
    params = {"type": type,"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getDayKLine(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。日线、周线、月线数据，数据范围包括沪深京A股、沪深京B股、港股、美股、黄金、汇率、Reits、沪深指数、香港指数、全球指数、债券指数、场内基金、沪深债券、行业板块、概念板块、地域板块。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getDayKLine"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getLevel2TimeDeal(type: int, code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    分时成交数据是指在一定时间内的成交和，如3秒内所有成交手数算在一起。数据均为不复权数据。数据范围包括沪深京A股、沪深京B股、场内基金、沪深债券。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；20|场内基金；30|沪深债券
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getLevel2TimeDeal"
    params = {"type": type,"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHangyeCfg(bkcode: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    查询行业板块、概念板块、地域板块下的成分股。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param bkcode    : 板块代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHangyeCfg"
    params = {"bkcode": bkcode,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getZhiShuChengFenGuZhongZhen(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    主要包含沪深京主要指数和香港主要指数的成分股数据。特别说明：指数成分股接口中指数只有沪深指数、香港指数中的一部分，大约有700只指数的成分股数据，也就是说沪深指数、香港指数中有部分指数是查不到成分股数据的。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 指数代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getZhiShuChengFenGuZhongZhen"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getZhiShuChengFenGu(mtype: int, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    只包含沪深300、上证50、中证500、科创50四个指数的成分股数据。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param mtype     : 指数类别，取值范围：1|沪深300；2|上证50；3|中证500；4|科创50
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getZhiShuChengFenGu"
    params = {"mtype": mtype,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getWatchStockTimeKLine(type: int, code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。提供沪深京A股、沪深京B股、港股、美股、黄金、汇率、Reits、沪深指数、香港指数、全球指数、债券指数、场内基金（ETF）、沪深债券实时数据获取接口。接口提供交易日当天实时交易数据，数据更新周期1分钟。沪深京股票交易时间：上午9：15--11：30，下午：13：00--15：00。港股交易时间：（1）正常交易时段：9:30至12:00；13:00至16:00。（2）早盘竞价时段：09:00至09:20；收市竞价交易：16:00至16:10。备注：每次请求实时接口只会返回当前最新一条数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getWatchStockTimeKLine"
    params = {"type": type,"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAcos(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    反余弦函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAcos"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAd(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    AD指标（Accumulation/Distribution）是一种用于量化分析股票、期货或其他金融资产的技术指标。它主要用于判断资金流向以及市场买卖压力的变化，进而辅助投资者做出买卖决策。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAd"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAdOsc(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ADOSC指标是一种技术分析指标，全称为累积/派发指标（Accumulation/Distribution Oscillator）。它用于衡量市场买卖压力的强度和方向。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 快速移动平均线周期
     :param input2    : 慢速移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAdOsc"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAdd(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    向量加法运算。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAdd"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAdx(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ADX指标（Average Directional Movement Index）是一种技术分析指标，用于衡量市场趋势的强弱程度。它由J. Welles Wilder于1978年提出，并广泛应用于股票、期货和外汇市场等。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAdx"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAdxr(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ADXR指标（Average Directional Movement Index Rating）是根据ADX指标（Average Directional Index）计算得出的一个指标，用于衡量市场趋势的强度。它是J. Welles Wilder开发的技术分析工具之一。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAdxr"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaApo(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    APO（Absolute Price Oscillator）指标是一种技术分析指标，用于衡量股票价格的变动幅度。它计算了两个不同时间周期的移动平均线之间的差异，从而提供了价格变动的绝对数值。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 快速移动平均线周期
     :param input3    : 慢速移动平均线周期
     :param input4    : 移动平均线类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaApo"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAroon(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    AROON指标的中文名称是“阿隆指标”，该指标是一种技术分析指标，用于衡量价格趋势的强度和趋势的方向。阿隆指标由两条线组成：上升线（Aroon Up）和下降线（Aroon Down）。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAroon"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAroonOsc(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    AroonOsc指标的名称是Aroon Oscillator（阿隆振荡器），它是Aroon指标的衍生指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAroonOsc"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAsin(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    反正弦函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAsin"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAtan(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    反正切函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAtan"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAtr(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ATR称为真实波动幅度指标，英文名称为Average True Range。ATR指标是一种衡量市场波动性的技术指标，它通过计算一定时间内的价格波动幅度，来评估市场的波动性程度。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAtr"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaAvgPrice(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    称为平均价格，Average Price (AVGPRICE) 。指标计算公式：AVGPRICE = (开盘价 + 最高价 + 最低价 + 收盘价) / 4 。它可以帮助分析师确定资产价格的趋势和波动性。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaAvgPrice"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaBbands(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, input5: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    BBANDS称为布林带，英文名称为Bollinger Bands。布林带是一种基于统计学原理的技术分析指标，由约翰·布林格（John Bollinger）于20世纪80年代提出。它通过计算价格的标准差来确定价格的高低波动区间，并以此构建出上下两条通道线，从而帮助判断价格的超买和超卖情况。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param input3    : 上轨道线的标准偏差倍数
     :param input4    : 下轨道线的标准偏差倍数
     :param input5    : 移动平均线类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaBbands"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"input5": input5,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaBeta(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    Beta指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input3    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaBeta"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaBop(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    BOP指标的名称是Balance of Power，也称为能量平衡指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaBop"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCci(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    CCI指标的全称是“商品通道指数”（Commodity Channel Index），它是一种技术分析指标，用于评估商品（或其他金融资产）的价格波动情况和超买超卖状态。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCci"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdl2Crows(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-Cdl2Crows指标。Two Crows 两只乌鸦，三日K线模式，第一天长阳，第二天高开收阴，第三天再次高开继续收阴，收盘比前一日收盘价低，预示股价下跌。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdl2Crows"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdl3BlackCrows(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-Cdl3BlackCrows指标。Three Black Crows 三只乌鸦，三日K线模式，连续三根阴线，每日收盘价都下跌且接近最低价，每日开盘价都在上根K线实体内，预示股价下跌。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdl3BlackCrows"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdl3Inside(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-Cdl3Inside指标。Three Inside Up/Down 三内部上涨和下跌，三日K线模式，母子信号+长K线，以三内部上涨为例，K线为阴阳阳，第三天收盘价高于第一天开盘价，第二天K线在第一天K线内部，预示着股价上涨。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdl3Inside"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdl3LineStrike(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-Cdl3LineStrike指标。Three-Line Strike 三线打击，四日K线模式，前三根阳线，每日收盘价都比前一日高，开盘价在前一日实体内，第四日市场高开，收盘价低于第一日开盘价，预示股价下跌。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdl3LineStrike"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdl3Outside(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-Cdl3Outside指标。Three Outside Up/Down 三外部上涨和下跌,三日K线模式，与三内部上涨和下跌类似，K线为阴阳阳，但第一日与第二日的K线形态相反，以三外部上涨为例，第一日K线在第二日K线内部，预示着股价上涨。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdl3Outside"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdl3StarsInSouth(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-Cdl3StarsInSouth指标。Three Stars In The South 南方三星，三日K线模式，与大敌当前相反，三日K线皆阴，第一日有长下影线，第二日与第一日类似，K线整体小于第一日，第三日无下影线实体信号，成交价格都在第一日振幅之内，预示下跌趋势反转，股价上升。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdl3StarsInSouth"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdl3WhiteSoldiers(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-Cdl3WhiteSoldiers指标。Three Advancing White Soldiers 三个白兵，三日K线模式，三日K线皆阳，每日收盘价变高且接近最高价，开盘价在前一日实体上半部，预示股价上升。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdl3WhiteSoldiers"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlAbandonedBaby(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlAbandonedBaby指标。Abandoned Baby 弃婴，三日K线模式，第二日价格跳空且收十字星（开盘价与收盘价接近，最高价最低价相差不大），预示趋势反转，发生在顶部下跌，底部上涨。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 穿透率
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlAbandonedBaby"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlAdvanceBlock(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlAdvanceBlock指标。Advance Block 大敌当前，三日K线模式，三日都收阳，每日收盘价都比前一日高，开盘价都在前一日实体以内，实体变短，上影线变长。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlAdvanceBlock"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlBeltHold(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlBeltHold指标。Belt-hold CDLBELTHOLD 捉腰带线，两日K线模式，下跌趋势中，第一日阴线，第二日开盘价为最低价，阳线，收盘价接近最高价，预示价格上涨。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlBeltHold"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlBreakaway(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlBreakaway。指标Breakaway 脱离，五日K线模式，以看涨脱离为例，下跌趋势中，第一日长阴线，第二日跳空阴线，延续趋势开始震荡，第五日长阳线，收盘价在第一天收盘价与第二天开盘价之间，预示价格上涨。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlBreakaway"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlClosingMarubozu(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlClosingMarubozu指标。Closing Marubozu 收盘缺影线，一日K线模式，以阳线为例，最低价低于开盘价，收盘价等于最高价，预示着趋势持续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlClosingMarubozu"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlConcealBabysWall(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlConcealBabysWall指标。Concealing Baby Swallow 藏婴吞没，四日K线模式，下跌趋势中，前两日阴线无影线，第二日开盘、收盘价皆低于第二日，第三日倒锤头，第四日开盘价高于前一日最高价，收盘价低于前一日最低价，预示着底部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlConcealBabysWall"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlCounterAttack(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlCounterAttack指标。Counterattack 反击线，二日K线模式，与分离线类似。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlCounterAttack"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlDarkCloudCover(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlDarkCloudCover指标。Dark Cloud Cover 乌云盖顶，二日K线模式，第一日长阳，第二日开盘价高于前一日最高价，收盘价处于前一日实体中部以下，预示着股价下跌。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 穿透率
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlDarkCloudCover"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlDoji(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlDoji指标。Doji 十字，一日K线模式，开盘价与收盘价基本相同。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlDoji"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlDojiStar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlDojiStar指标。Doji Star 十字星，一日K线模式，开盘价与收盘价基本相同，上下影线不会很长，预示着当前趋势反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlDojiStar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlDragonflyDoji(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlDragonflyDoji指标。Dragonfly Doji 蜻蜓十字/T形十字，一日K线模式，开盘后价格一路走低，之后收复，收盘价与开盘价相同，预示趋势反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlDragonflyDoji"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlEngulfing(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlEngulfing指标。Dragonfly 蜻蜓十字/T形十字指标，一日K线模式，开盘后价格一路走低，之后收复，收盘价与开盘价相同，预示趋势反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlEngulfing"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlEveningDojiStar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlEveningDojiStar指标。Evening Doji Star 十字暮星指标，三日K线模式，基本模式为暮星，第二日收盘价和开盘价相同，预示顶部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 穿透率
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlEveningDojiStar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlEveningStar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlEveningStar指标。Evening Star 暮星指标，三日K线模式，与晨星相反，上升趋势中,第一日阳线，第二日价格振幅较小，第三日阴线，预示顶部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 穿透率
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlEveningStar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlGapSideSideWhite(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlGapSideSideWhite指标。Up/Down-gap side-by-side white lines 向上/下跳空并列阳线指标，二日K线模式，上升趋势向上跳空，下跌趋势向下跳空,第一日与第二日有相同开盘价，实体长度差不多，则趋势持续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlGapSideSideWhite"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlGravestoneDoji(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlGravestoneDoji指标。Gravestone Doji 墓碑十字/倒T十字指标。一日K线模式，开盘价与收盘价相同，上影线长，无下影线，预示底部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlGravestoneDoji"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHammer(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHammer指标。Hammer 锤头指标。一日K线模式，实体较短，无上影线，下影线大于实体长度两倍，处于下跌趋势底部，预示反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHammer"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHangingMan(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHangingMan指标。Hanging Man 上吊线指标。一日K线模式，形状与锤子类似，处于上升趋势的顶部，预示着趋势反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHangingMan"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHarami(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHarami指标。Harami Pattern 母子线指标。二日K线模式，分多头母子与空头母子，两者相反，以多头母子为例，在下跌趋势中，第一日K线长阴，第二日开盘价收盘价在第一日价格振幅之内，为阳线，预示趋势反转，股价上升。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHarami"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHaramiCross(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHaramiCross指标。Harami Cross Pattern 十字孕线指标。二日K线模式，与母子县类似，若第二日K线是十字线，便称为十字孕线，预示着趋势反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHaramiCross"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHignWave(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHignWave指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHignWave"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHikkake(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHikkake指标。Hikkake Pattern 陷阱，三日K线模式，与母子类似，第二日价格在前一日实体范围内,第三日收盘价高于前两日，反转失败，趋势继续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHikkake"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHikkakeMod(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHikkakeMod指标。Modified Hikkake Pattern 修正陷阱，三日K线模式，与陷阱类似，上升趋势中，第三日跳空高开；下跌趋势中，第三日跳空低开，反转失败，趋势继续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHikkakeMod"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlHomingPigeon(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlHomingPigeon指标。Homing Pigeon 家鸽，二日K线模式，与母子线类似，不同的的是二日K线颜色相同，第二日最高价、最低价都在第一日实体之内，预示着趋势反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlHomingPigeon"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlIdentical3Crows(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlIdentical3Crows指标。Identical Three Crows 三胞胎乌鸦，三日K线模式，上涨趋势中，三日都为阴线，长度大致相等，每日开盘价等于前一日收盘价，收盘价接近当日最低价，预示价格下跌。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlIdentical3Crows"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlInNeck(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlInNeck指标。In-Neck Pattern 颈内线，二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低，收盘价略高于第一日收盘价，阳线，实体较短，预示着下跌继续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlInNeck"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlInvertedHammer(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlInvertedHammer指标。Inverted Hammer 倒锤头，一日K线模式，上影线较长，长度为实体2倍以上，无下影线，在下跌趋势底部，预示着趋势反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlInvertedHammer"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlKicking(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlKicking指标。Kicking 反冲形态，二日K线模式，与分离线类似，两日K线为秃线，颜色相反，存在跳空缺口。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlKicking"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlKickingByLength(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlKickingByLength指标。Kicking - bull/bear determined by the longer marubozu 由较长缺影线决定的反冲形态，二日K线模式，与反冲形态类似，较长缺影线决定价格的涨跌。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlKickingByLength"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlLadderBottom(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlLadderBottom指标。Ladder Bottom 梯底，五日K线模式，下跌趋势中，前三日阴线，开盘价与收盘价皆低于前一日开盘、收盘价，第四日倒锤头，第五日开盘价高于前一日开盘价，阳线，收盘价高于前几日价格振幅，预示着底部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlLadderBottom"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlLongLeggedDoji(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlLongLeggedDoji指标。Long Legged Doji 长脚十字，一日K线模式，开盘价与收盘价相同居当日价格中部，上下影线长，表达市场不确定性。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlLongLeggedDoji"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlLongLine(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlLongLine指标。Long Line Candle 长蜡烛，一日K线模式，K线实体长，无上下影线。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlLongLine"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlMarubozu(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlMarubozu指标。Marubozu 光头光脚/缺影线，一日K线模式，上下两头都没有影线的实体，阴线预示着熊市持续或者牛市反转，阳线相反。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlMarubozu"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlMatHold(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlMatHold指标。Mat Hold 铺垫，五日K线模式，上涨趋势中，第一日阳线，第二日跳空高开影线，第三、四日短实体影线，第五日阳线，收盘价高于前四日，预示趋势持续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 穿透率
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlMatHold"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlMatchingLow(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlMatchingLow指标。Matching Low 相同低价，二日K线模式，下跌趋势中，第一日长阴线，第二日阴线，收盘价与前一日相同，预示底部确认，该价格为支撑位。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlMatchingLow"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlMorningDojiStar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlMorningDojiStar指标。Morning Doji Star 十字晨星,三日K线模式，基本模式为晨星，第二日K线为十字星，预示底部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 穿透率
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlMorningDojiStar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlMorningStar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlMorningStar指标。Morning Star 晨星，三日K线模式，下跌趋势，第一日阴线，第二日价格振幅较小，第三天阳线，预示底部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 穿透率
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlMorningStar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlOnNeck(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlOnNeck指标。On-Neck Pattern 颈上线,二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低，收盘价与前一日最低价相同，阳线，实体较短，预示着延续下跌趋势。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlOnNeck"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlPiercing(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlPiercing指标。Piercing Pattern 刺透形态，两日K线模式，下跌趋势中，第一日阴线，第二日收盘价低于前一日最低价，收盘价处在第一日实体上部，预示着底部反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlPiercing"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlRickshawMan(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlRickshawMan指标。Rickshaw Man 黄包车夫,一日K线模式，与长腿十字线类似，若实体正好处于价格振幅中点，称为黄包车夫。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlRickshawMan"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlRiseFall3Methods(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlRiseFall3Methods指标。Rising/Falling Three Methods 上升/下降三法，五日K线模式，以上升三法为例，上涨趋势中，第一日长阳线，中间三日价格在第一日范围内小幅震荡，第五日长阳线，收盘价高于第一日收盘价，预示股价上升。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlRiseFall3Methods"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlSeperatingLines(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlSeperatingLines指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlSeperatingLines"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlShootingStar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlShootingStar指标。Shooting Star 射击之星，一日K线模式，上影线至少为实体长度两倍，没有下影线，预示着股价下跌。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlShootingStar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlShortLine(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlShortLine指标。Short Line Candle 短蜡烛，一日K线模式，实体短，无上下影线。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlShortLine"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlSpinningTop(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlSpinningTop指标。Spinning Top 纺锤，一日K线，实体小。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlSpinningTop"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlStalledPattern(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlStalledPattern指标。Stalled Pattern 停顿形态，三日K线模式，上涨趋势中，第二日长阳线，第三日开盘于前一日收盘价附近，短阳线，预示着上涨结束。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlStalledPattern"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlStickSandwhich(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlStickSandwhich指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlStickSandwhich"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlTakuri(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlTakuri指标。Takuri (Dragonfly Doji with very long lower shadow) 探水竿，一日K线模式，大致与蜻蜓十字相同，下影线长度长。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlTakuri"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlTasukiGap(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlTasukiGap指标。Tasuki Gap 跳空并列阴阳线，三日K线模式，分上涨和下跌，以上升为例，前两日阳线，第二日跳空，第三日阴线，收盘价于缺口中，上升趋势持续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlTasukiGap"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlThrusting(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlThrusting指标。Thrusting Pattern 插入，二日K线模式，与颈上线类似，下跌趋势中，第一日长阴线，第二日开盘价跳空，收盘价略低于前一日实体中部，与颈上线相比实体较长，预示着趋势持续。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlThrusting"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlTristar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlTristar指标。Tristar Pattern 三星，三日K线模式，由三个十字组成，第二日十字必须高于或者低于第一日和第三日，预示着反转。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlTristar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlUnique3River(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlUnique3River指标。Unique 3 River 奇特三河床，三日K线模式，下跌趋势中，第一日长阴线，第二日为锤头，最低价创新低，第三日开盘价低于第二日收盘价，收阳线，收盘价不高于第二日收盘价，预示着反转，第二日下影线越长可能性越大。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlUnique3River"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlUpsideGap2Crows(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlUpsideGap2Crows指标。Upside Gap Two Crows 向上跳空的两只乌鸦，三日K线模式，第一日阳线，第二日跳空以高于第一日最高价开盘，收阴线，第三日开盘价高于第二日，收阴线，与第一日比仍有缺口。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlUpsideGap2Crows"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCdlXSideGap3Methods(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    形态识别-CdlXSideGap3Methods指标。Upside/Downside Gap Three Methods 上升/下降跳空三法，五日K线模式，以上升跳空三法为例，上涨趋势中，第一日长阳线，第二日短阳线，第三日跳空阳线，第四日阴线，开盘价与收盘价于前两日实体内，第五日长阳线，收盘价高于第一日收盘价，预示股价上升。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCdlXSideGap3Methods"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCeil(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    向上取整数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCeil"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCmo(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    CMO指标的名称：Chande Momentum Oscillator（CMO，钱德动量振荡器）。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCmo"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCorrel(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    Correl指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input3    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCorrel"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCos(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    余弦函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCos"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaCosh(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    双曲正弦函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaCosh"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaDema(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    DEMA指标是一种双指数移动平均线，全称为Double Exponential Moving Average。DEMA指标用于平滑价格数据，以便更好地识别价格趋势。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaDema"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaDiv(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    向量减法运算。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaDiv"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaDx(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    动向指标(DMI)，英文名称是Directional Movement Index。动向指标（Dx）是一种技术分析指标，用于衡量市场趋势的强度和方向。它由综合指标（+DI和-DI）计算得出，可以帮助交易者判断市场是上涨趋势、下跌趋势还是盘整。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaDx"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaEma(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    EMA指标是指数移动平均线，全称为Exponential Moving Average。它是一种常用的技术分析工具，用于平滑价格数据并识别趋势。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaEma"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaExp(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    指数曲线。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaExp"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaFloor(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    向下取整数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaFloor"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaHtDcPeriod(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    Dominant Cycle Period 希尔伯特变换-主导周期。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaHtDcPeriod"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaHtDcPhase(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    Dominant Cycle Phase 希尔伯特变换-主导循环阶段。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaHtDcPhase"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaHtPhasor(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    Phasor Components 希尔伯特变换-希尔伯特变换相量分量。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaHtPhasor"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaHtSine(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    SineWave 希尔伯特变换-正弦波。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaHtSine"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaHtTrendMode(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    Trend vs Cycle Mode 希尔伯特变换-趋势与周期模式。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaHtTrendMode"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaHtTrendline(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    HTTRENDLINE称为趋势线，英文名称为HTTRENDLINE。该指标是一种基于趋势线的技术分析工具。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaHtTrendline"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaKama(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    KAMA是考夫曼自适应移动平均线，全称为Kaufman Adaptive Moving Average。是由Perry J. Kaufman开发的一种技术分析工具，用于平滑股价走势并提供趋势信号。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaKama"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaLinearReg(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    LinearReg指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaLinearReg"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaLinearRegAngle(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    LinearRegAngle指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaLinearRegAngle"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaLinearRegIntercept(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    LinearRegIntercept指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaLinearRegIntercept"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaLinearRegSlope(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    LinearRegSlope指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaLinearRegSlope"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaLn(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    自然对数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaLn"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaLog10(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    对数函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaLog10"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMacd(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MACD指标的中文名称为移动平均线收敛/发散指标，英文名称为Moving Average Convergence Divergence。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 快速移动平均线周期
     :param input3    : 慢速移动平均线周期
     :param input4    : 信号移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMacd"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMacdExt(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, input5: str, input6: str, input7: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MACDEXT指标的中文名称是MACD扩展，英文名称是MACD Extended。MACD扩展是基于移动平均线收敛背离（MACD）指标的一种变种指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 快速移动平均线周期
     :param input3    : 快速移动平均线类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param input4    : 慢速移动平均线周期
     :param input5    : 慢速移动平均线类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param input6    : 信号移动平均线周期
     :param input7    : 信号移动平均线类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMacdExt"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"input5": input5,"input6": input6,"input7": input7,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMacdFix(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MACDFIX指标的中文名称为移动平均收敛/背离指标，英文名称为Moving Average Convergence Divergence Fix。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 信号移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMacdFix"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMama(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MAMA是MESA自适应移动平均线，全称为MESA Adaptive Moving Average。它是根据价格的移动平均线和自适应移动平均线来计算的，它的设计初衷是能够更好地适应不同市场的变化。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 输入参数
     :param input3    : 输入参数
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMama"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMax(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    周期内最大值。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMax"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMaxIndex(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    周期内最大值的索引。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMaxIndex"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMedPrice(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    称为中位数价格指标，Median Price Indicator。指标计算公式：MEDPRICE = (最高价 + 最低价) / 2。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMedPrice"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMfi(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MFI指标的中文名称是资金流量指标，英文名称是Money Flow Index。MFI指标是一种衡量资金流入和流出的指标。它通过计算一定时期内的典型价格和成交量的买卖压力来衡量市场的超买和超卖情况。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMfi"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMidPoint(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MIDPOINT是一种基于价格的技术指标，用于衡量价格趋势的中点。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMidPoint"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMidPrice(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MIDPRICE指标是一种技术分析工具，用于计算一段时间内的市场中间价。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMidPrice"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMin(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    周期内最小值。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMin"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMinIndex(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    周期内最小值的索引。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMinIndex"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMinMax(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    周期内最小值和最大值。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMinMax"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMinMaxIndex(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    周期内最小值和最大值索引。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMinMaxIndex"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMinusDI(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MINUSDI指标中文名称为负向动向指标，英文名称为Negative Directional Indicator。它是技术分析中的一个指标，用于衡量市场下跌趋势的强度。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMinusDI"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMinusDM(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MINUSDM指标的中文名称为负方向运动指标，英文名称为Minus Directional Movement Indicator。该指标用于衡量股价下跌的动力和趋势强度。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMinusDM"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMom(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MOM金融指标的中文名称为动量指标，英文名称为Momentum Indicator。该指标是通过比较当前价格与一定期间前的价格变动情况来衡量市场的趋势力量。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMom"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMovingAverage(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    MOVINGAVERAGE金融指标的中文名称为移动平均线，英文名称为Moving Average。该指标通过计算一段时间内收盘价的平均值来观察价格变动的趋势。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param input3    : 移动平均线类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMovingAverage"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaMult(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    向量乘法运算。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaMult"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaNatr(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    NATR称为归一化真实波动幅度，英文名称为Normalized Average True Range。该指标用于衡量市场的波动性。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaNatr"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaObv(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    OBV指标（On-Balance Volume）是一种量能指标，用于衡量成交量的变化趋势和预测价格趋势的强弱。OBV指标通过统计成交量的正负值来判断市场的买卖力量，从而预测价格的上涨或下跌趋势。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaObv"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaPlusDI(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    正向移动方向指标，英文名称是Positive Directional Indicator。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaPlusDI"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaPlusDM(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    正向动向变动指标，英文名称是Positive Directional Movement。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaPlusDM"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaPpo(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    价格振荡百分比指标，英文名称为Percentage Price Oscillator。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 快速移动平均线周期
     :param input3    : 慢速移动平均线周期
     :param input4    : 移动平均线类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaPpo"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaRoc(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ROC金融指标的中文名称是变动率，英文名称是Rate of Change，ROC指标是一种衡量价格变动速度的技。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaRoc"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaRocP(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ROCP指标的中文名称为变化率指标，英文名称为Rate of Change Percentage。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaRocP"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaRocR(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ROCR金融指标是指Rate of Change Ratio，其中文名称是变动率比率，英文名称是Rate of Change Ratio。该指标用于衡量价格的变动率，并通过计算价格的百分比变化来表示。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaRocR"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaRocR100(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ROCR100金融指标的中文名称为价格变动率，英文名称为Rate of Change Ratio 100，指标介绍为衡量价格在一定时间内的变动幅度，以百分比表示。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaRocR100"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaRsi(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    RSI指标是相对强弱指标，全称为Relative Strength Index。它是一种用于衡量市场超买超卖状态的技术指标，由J. Welles Wilder于1978年提出。RSI指标的计算基于一定时期内的价格变动幅度，通过将一定时期内的上涨幅度和下跌幅度进行比较，以确定市场的强弱程度。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaRsi"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSar(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    SAR称为抛物线指标，英文名称为Parabolic SAR (Stop and Reverse)。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 加速因子
     :param input2    : 最大值
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSar"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSarExt(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, input5: str, input6: str, input7: str, input8: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    SAREXT称为拓展停损点指标，英文名称为SAREXT (Extended Stop and Reverse Indicator)。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 起始值
     :param input2    : 反转偏移量
     :param input3    : 多头初始加速因子
     :param input4    : 多头加速因子
     :param input5    : 多头最大加速因子
     :param input6    : 空头初始加速因子
     :param input7    : 空头加速因子
     :param input8    : 空头最大加速因子
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSarExt"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"input5": input5,"input6": input6,"input7": input7,"input8": input8,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSin(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    正弦函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSin"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSinh(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    双曲正弦函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSinh"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSma(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    SMA指标是简单移动平均线，全称为Simple Moving Average。它是一种常用的技术分析指标，用于平滑价格数据并显示价格趋势。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSma"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSqrt(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    非负实数的平方根。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSqrt"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaStdDev(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    StdDev指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param input3    : 标准差倍数
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaStdDev"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaStoch(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, input5: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    STOCH是随机指标（KDJ指标），英文名称是Stochastic Oscillator。该指标是一种用来测量价格相对于其价格范围的位置的技术指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 快速移动平均线K周期
     :param input2    : 慢速移动平均线K周期
     :param input3    : 慢速移动平均线K类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param input4    : 慢速移动平均线D周期
     :param input5    : 慢速移动平均线D类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaStoch"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"input5": input5,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaStochF(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    STOCHF是随机振荡指标（Stochastic Fast）。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 快速移动平均线K周期
     :param input2    : 慢速移动平均线D周期
     :param input3    : 慢速移动平均线D类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaStochF"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaStochRsi(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, input4: str, input5: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    随机相对强弱指标，Stochastic Relative Strength Index (STOCHRSI)。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param input3    : 快速移动平均线K周期
     :param input4    : 慢速移动平均线D周期
     :param input5    : 慢速移动平均线D类型，取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaStochRsi"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"input4": input4,"input5": input5,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSub(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    向量除法运算。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSub"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaSum(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    周期内求和。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaSum"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaT3(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    T3是三重移动平均线，全称是Triple Exponential Moving Average。它是指数移动平均线（EMA）的一种改进版本。T3指标通过使用三次平滑来减少EMA的滞后性，并提供更快的响应速度。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param input3    : va系数
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaT3"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTan(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    正切函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTan"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTanh(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    双曲正切函数。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTanh"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTema(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    TEMA是三重指数移动平均线，全程为Triple Exponential Moving Average。它是一种技术分析指标，用于平滑价格数据并识别趋势的变化。TEMA通过多次平滑价格数据来减少价格波动的影响，从而更准确地识别趋势的变化。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTema"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTrima(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    TRIMA是三重指数平均线，全称为Triangular Moving Average。它是一种平滑的移动平均线，通过将价格数据进行多次平均处理来消除噪音和波动。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTrima"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTrix(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    TRIX金融指标的中文名称是三重指数平滑平均线，英文名称是Triple Exponential Moving Average (TRIX)。TRIX是一种技术分析指标，用于衡量资产价格的趋势强度。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTrix"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTrueRange(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    称为真实波幅，英文名称为True Range。它是一种衡量价格波动性的指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTrueRange"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTsf(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    Tsf指标。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTsf"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaTypPrice(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    TYPPRICE是一种计算股票或其他金融资产的典型价格的方法。指标计算公式：Typical Price = (High + Low + Close) / 3。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaTypPrice"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaUltOsc(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    ULTOSC称为综合摆动指标，英文名称：Ultimate Oscillator (ULTOSC)。综合摆动指标是一种多周期的技术指标，用于衡量市场买卖力量的强弱。它通过将短期、中期和长期的价格波动进行加权平均，以提供更全面的市场信号。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 移动平均线周期1
     :param input2    : 移动平均线周期2
     :param input3    : 移动平均线周期3
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaUltOsc"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaVariance(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, input3: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    方差。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param input3    : 标准差倍数
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaVariance"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"input3": input3,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaWclPrice(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    WCLPRICE指标称为加权收盘价，英文名称为Weighted Close Price。指标计算公式：WCLPRICE = (最高价 + 最低价 + 2 * 收盘价) / 4 。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaWclPrice"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaWillR(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    WILLR指标的中文名称为威廉指标(WR)，英文名称为Williams' %R(W%R)。该指标通过测量价格在给定时间周期内的相对变动程度，来判断市场的超买和超卖情况。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input     : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaWillR"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input": input,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndicatorTaWma(type: int, code: str, ktype: int, fq: int, startDate: str, endDate: str, input1: str, input2: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    WMA指标是一种移动平均线指标，全称为Weighted Moving Average。它是一种加权平均线指标，与简单移动平均线（SMA）不同，WMA在计算平均值时给予较近期的数据更高的权重。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股；4|美股；5|黄金；6|汇率；7|Reits；10|沪深指数；11|香港指数；12|全球指数；13|债券指数；20|场内基金；30|沪深债券；40|行业板块；41|概念板块；42|地域板块
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：1|1分钟；5|5分钟；15|15分钟；30|30分钟；60|60分钟；101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param input1    : 数据标签，取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|cjl-成交量；6|cje-成交额
     :param input2    : 移动平均线周期
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndicatorTaWma"
    params = {"type": type,"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"input1": input1,"input2": input2,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSABaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSABaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSADailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。沪深京A股每日行情数据。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSADailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSAMinuteKLine(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股分线数据，数据以分钟为粒度。数据均为不复权数据，提供开盘竞价数据。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSAMinuteKLine"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSAHourKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股时线数据，数据均为不复权数据。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSAHourKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSADayKLine(code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。沪深京A股日线、周线、月线数据。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSADayKLine"
    params = {"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSBBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京B股基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSBBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSBDailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。沪深京B股每日行情数据。温馨提示：code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSBDailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSBMinuteKLine(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京B股分线数据，数据以分钟为粒度，提供开盘竞价数据。温馨提示：code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSBMinuteKLine"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSBHourKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京B股分时数据。提供5分钟、15分钟、30分钟、60分钟数据。温馨提示：code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSBHourKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHSBDayKLine(code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。沪深京B股日线、周线、月线数据。温馨提示：code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->B股->B股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHSBDayKLine"
    params = {"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockReName(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深A股股票曾用名。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockReName"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCompanyInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深A股公司信息。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCompanyInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockAccount(fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    股票账户统计详细数据。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockAccount"
    params = {"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockTradeDate(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深股票市场交易日历。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockTradeDate"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getChuQuanChuXi(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深A股除权除息数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getChuQuanChuXi"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getFuQuanYinZi(code: str, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深A股复权因子。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param fq        : 复权类别，取值范围：1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getFuQuanYinZi"
    params = {"code": code,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getJiGouDiaoYanTongJi(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    机构调研统计。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getJiGouDiaoYanTongJi"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getJiGouDiaoYanXiangXi(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    机构调研详细。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getJiGouDiaoYanXiangXi"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getJiGouDiaoYanJiLv(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    机构调研记录，记录机构调查详细内容，评估公司经营情况。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getJiGouDiaoYanJiLv"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getLonghbDetail(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股龙虎榜详情数据。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getLonghbDetail"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getLonghbActive(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股龙虎榜每日活跃营业部。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getLonghbActive"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getLonghbJigou(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股龙虎榜机构每日买卖统计。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getLonghbJigou"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getRzRjMarket(mtype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪市、深市融资融券交易信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param mtype     : 市场类型，取值范围：1|沪深两市；2|沪市；3|深市；3|京市
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getRzRjMarket"
    params = {"mtype": mtype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getRzRjHangye(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深A股板块融资融券。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 板块代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getRzRjHangye"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockRzRj(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股融资融券交易信息。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockRzRj"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getRzRjAccount(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股融资融券账户信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getRzRjAccount"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockXQHSADayKLine(code: str, ktype: int, fq: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    备用沪深京A股股票日线、周线、月线数据。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param fq        : 复权信息，取值范围：0|不复权；1|前复权；2|后复权
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockXQHSADayKLine"
    params = {"code": code,"ktype": ktype,"fq": fq,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getYanBaoStock(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    个股研报。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getYanBaoStock"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getYanBaoXinGu(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    新股研报。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getYanBaoXinGu"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getYanBaoHangYe(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    行业研报。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getYanBaoHangYe"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getYanbaoCelue(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    策略报告。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getYanbaoCelue"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getYanBaoChenBao(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    券商晨报。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getYanBaoChenBao"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getYanBaoHongGuan(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    宏观研究。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getYanBaoHongGuan"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getYanBaoYingLi(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    盈利预测。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getYanBaoYingLi"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportNianBao(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司业绩报表。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportNianBao"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportKuaiBao(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司业绩快报。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportKuaiBao"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportYugao(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司业绩预告。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportYugao"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportYuyueTime(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司预约披露时间。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportYuyueTime"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportFuzhai(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司资产负债表。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportFuzhai"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportLirun(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司利润表。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportLirun"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportXianjin(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司现金流量表。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportXianjin"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReportFenhong(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京上市公司分红送配。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReportFenhong"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHSGTMoney(mtype: int, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    南向资金、北向资金流向数据，包括净流入、资金余额、累计净流入。香港投资者交易内地股票，称为北向资金，内地投资者交易香港股票，称为南向资金。当日资金流入额=当日限额-当日余额。当日资金流入额包含两部分：当日成交净买额，当日申报但未成交的买单金额。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param mtype     : 沪深港通资金类型，取值范围：1|沪股通(港>沪)资金-北向；2|深股通(港>深)资金-北向；3|北向资金；4|港股通(沪>港)资金-南向；5|港股通(深>港)资金-南向；6|南向资金
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线；104|季线；106|年线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHSGTMoney"
    params = {"mtype": mtype,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHSGTBlockRank(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    北向板块排行数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 板块代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHSGTBlockRank"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHSGTStockRank(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    北向个股排行数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHSGTStockRank"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHSGTHistory(mtype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深港通历史数据。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param mtype     : 市场类别，取值范围：1|沪股通(港>沪)；2|深股通(港>深)；3|港股通(沪>港)；4|港股通(深>港)
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHSGTHistory"
    params = {"mtype": mtype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHsgtStockTop10(code: str, mtype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深港通十大成交股。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param mtype     : 市场类别，取值范围：1|沪股通(港>沪)；2|港股通(沪>港)；3|深股通(港>深)；4|港股通(深>港)
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHsgtStockTop10"
    params = {"code": code,"mtype": mtype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCaiWuZYZBReportHSA(code: str, mtype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深股市财务数据主要指标，按报告期、年度数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param mtype     : 报告类型，取值范围：0|按报告期；1|按年度
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCaiWuZYZBReportHSA"
    params = {"code": code,"mtype": mtype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCaiWuZYZBQuarterHSA(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深股市财务数据主要指标，按季度数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCaiWuZYZBQuarterHSA"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getFinanceHSDebt(code: str, mtype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深股市财务数据企业负债表，同比字段单位为百分比（%）。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param mtype     : 报告类型，取值范围：0|按报告期；1|按年度
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getFinanceHSDebt"
    params = {"code": code,"mtype": mtype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getPoolZT(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    包含当日当前涨停的所有A股股票(不含未中断连续一字涨停板的新股)。注：涨停板行情专题统计不包含ST股票及科创板股票。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getPoolZT"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getPoolQS(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    包含创下60日新高或近期多次涨停的A股股票。注：涨停板行情专题统计不包含ST股票及科创板股票。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getPoolQS"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getPoolCX(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    包含上市一年以内且中断了连续一字涨停板的A股股票。注：涨停板行情专题统计不包含ST股票及科创板股票。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getPoolCX"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getPoolZB(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    包含当日触及过涨停板且当前未封板的A股股票。注：涨停板行情专题统计不包含ST股票及科创板股票。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getPoolZB"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getPoolDT(startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    包含当日当前跌停的所有A股股票。注：涨停板行情专题统计不包含ST股票及科创板股票。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getPoolDT"
    params = {"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCnFundBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    场内基金（ETF、LOF）基本信息。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCnFundBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCnFundDailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。场内基金（ETF、LOF）每日行情数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCnFundDailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCnFundMinuteKLine(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    场内基金（ETF、LOF）分线数据，数据以分钟为粒度，提供开盘竞价数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCnFundMinuteKLine"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCnFundHourKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    场内基金（ETF、LOF）分时数据，提供5分钟、15分钟、30分钟、60分钟数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCnFundHourKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getCnFundADayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。场内基金日线、周线、月线数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getCnFundADayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getFundBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    所有基金基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 基金代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getFundBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getFundRank(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。基金每日行情数据。温馨提示：code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 基金代码，code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getFundRank"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getFundNav(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    基金净值数据。温馨提示：code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 基金代码，code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getFundNav"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getFundMaxBack(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    获取基金历史最大回撤率。最大回撤率是指在选定周期内任一历史时点往后推，产品净值走到最低点时的收益率回撤幅度的最大值。最大回撤用来描述买入产品后可能出现的最糟糕的情况。历史最大回撤率=（最高点累计净值-最低点累计净值）/最高点累计净值。温馨提示：code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 基金代码，code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getFundMaxBack"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getFundPosition(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    基金持仓数据。温馨提示：code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 基金代码，code参数可以从【基金->基金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getFundPosition"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockPosition(scode: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    提供个股每个季度被各大基金机构持有数据。可通过股票代码，查询出该股票被基金公司持有的数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param scode     : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockPosition"
    params = {"scode": scode,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHyBKBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股行业板块基本信息，备注：可根据返回的成分股,在其它接口里作为入参（code字段）查询详细数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHyBKBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockGnBKBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股概念板块基本信息，备注：可根据返回的成分股,在其它接口里作为入参（code字段）查询详细数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockGnBKBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockDyBKBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深京A股地域板块基本信息，备注：可根据返回的成分股,在其它接口里作为入参（code字段）查询详细数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockDyBKBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHYADailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。沪深京A股行业板块每日行情数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 板块代码（行业板块、地域板块、概念板块），code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHYADailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockBKDayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。沪深京A股板块日线、周线、月线数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 板块代码（行业板块、地域板块、概念板块），code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockBKDayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getGZMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    市场估值概况。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 市场代码，取值范围：000300|沪深两市；000001|沪市主板；000688|科创板；399001|深市主板；399006|创业板
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getGZMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getGZHangYe(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    行业估值概况。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 板块代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getGZHangYe"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHSGZStock(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    个股估值概况。温馨提示：code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【沪深京->A股->A股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHSGZStock"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getBaseInfoPlatB(type: int, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    行业数据包括行业板块、概念板块、地域板块、证监会行业板块。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：40|行业板块；41|概念板块；42|地域板块；43|证监会行业板块
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBaseInfoPlatB"
    params = {"type": type,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getHangyeCfgPlatB(bkcode: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    查询行业板块、概念板块、地域板块、证监会行业板块下的成分股。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param bkcode    : 板块代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getHangyeCfgPlatB"
    params = {"bkcode": bkcode,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHKBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    港股股票基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHKBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHKDailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。港股行情数据。温馨提示：code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHKDailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHKMinuteKLine(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    港股分线数据，数据以分钟为粒度，提供开盘竞价数据，提供开盘竞价数据。温馨提示：code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHKMinuteKLine"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHKHourKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    港股分时数据，提供5分钟、15分钟、30分钟、60分钟数据。温馨提示：code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHKHourKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockHKDayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。港股日线、周线、月线数据。温馨提示：code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【港股->港股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockHKDayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockUSABaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    美股股票基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockUSABaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockUSADailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。美股行情数据。温馨提示：code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockUSADailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockUSAMinuteKLine(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    美股分线数据，数据以分钟为粒度，提供开盘竞价数据。温馨提示：code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockUSAMinuteKLine"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockUSAHourKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    美股分时数据，提供5分钟、15分钟、30分钟、60分钟数据。温馨提示：code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockUSAHourKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getStockUSADayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。美股日线、周线、月线数据。温馨提示：code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【美股->美股列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getStockUSADayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndexHSBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深指数基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndexHSBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndexHKBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    香港指数基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndexHKBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndexQQBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    全球指数基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndexQQBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndexBondBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    债券指数基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndexBondBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndexDailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。所有指数行情数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndexDailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndexHourKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    所有指数5分钟、15分钟、30分钟、60分钟数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndexHourKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getIndexDayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。所有指数日线、周线、月线数据。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getIndexDayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getBondHSBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深可转债基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 债券代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBondHSBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getBondHSDetailInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    沪深可转债基本信息。温馨提示：code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 债券代码，code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBondHSDetailInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getBondHSDailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。可转债行情数据。温馨提示：code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBondHSDailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getBondMinuteKLine(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    可转债分线数据，数据以分钟为粒度，提供开盘竞价数据。温馨提示：code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBondMinuteKLine"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getBondHSHourKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    可转债分时数据。温馨提示：code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；不支持all参数查询。
     :param ktype     : K线类别，取值范围：5|5分钟；15|15分钟；30|30分钟；60|60分钟
     :param startDate : 开始日期，yyyy-MM-dd HH:mm:ss格式，例如：2020-01-01 01:00:00
     :param endDate   : 结束日期，yyyy-MM-dd HH:mm:ss格式，例如：2050-01-01 01:00:00
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBondHSHourKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getBondHSDayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。可转债日线、周线、月线数据。温馨提示：code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【债券->可转债列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getBondHSDayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getGoldBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    黄金基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getGoldBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getGoldDayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。黄金日线、周线、月线数据。温馨提示：code参数可以从【其它->黄金->黄金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【其它->黄金->黄金列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getGoldDayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getWaihuiBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    外汇基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getWaihuiBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getWaihuiDayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。外汇日线、周线、月线数据。温馨提示：code参数可以从【其它->外汇->外汇列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【其它->外汇->外汇列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getWaihuiDayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReitsBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    黄金基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReitsBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getReitsDayKLine(code: str, ktype: int, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想收盘后立即获取当日的收盘数据，可通过【实时行情】或者【每日行情】接口获取收盘后的日K线数据。Reits日线、周线、月线数据。温馨提示：code参数可以从【其它->REITS->REITS列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【其它->REITS->REITS列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param ktype     : K线类别，取值范围：101|日线；102|周线；103|月线
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getReitsDayKLine"
    params = {"code": code,"ktype": ktype,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getQihuoBaseInfo(code: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    期货基本信息。温馨提示：建议选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getQihuoBaseInfo"
    params = {"code": code,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getQihuoDailyMarket(code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    如果想立即获取当天的收盘数据，收盘后可通过本接口采集当天日K线数据。期货每日行情数据。温馨提示：code参数可以从【其它->期货->期货列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param code      : 股票代码，code参数可以从【其它->期货->期货列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getQihuoDailyMarket"
    params = {"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text

def getTSStockPosition(type: int, code: str, startDate: str, endDate: str, fields: str, export: int, token: str, filter: str,  method: str = "post") -> str:
    """
    提供各大机构持有沪深京A股、沪深京B股、港股数据。主要用于分析个股每个季度被各大基金机构持有情况。温馨提示：code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据。
    :param type      : 资产类型，取值范围：1|沪深京A股；2|沪深京B股；3|港股
     :param code      : 股票代码，code参数可以从【通用接口->股票列表】接口中批量获取，也可以选择左上角菜单栏【浏览模式】查询数据；支持批量查询，用逗号分隔，每次最多50个；若为all，则表示全部，即可获取任意一天内的所有数据。
     :param startDate : 开始日期，yyyy-MM-dd格式，例如：2020-01-01
     :param endDate   : 结束日期，yyyy-MM-dd格式，例如：2050-01-01
     :param fields    : 数据字段，多个字段之间使用逗号分隔，若获取所有字段，则取值为all。
     :param export    : 数据导出类型，取值范围：0|Txt字符串；1|Json字符串；2|Txt文件；3|Json文件；4|Csv文件；5|DataFrame格式
     :param token     : 令牌，登录后可获取
     :param filter    : 过滤参数，例如filter=open>=15。建议选择左上角菜单栏【浏览模式】操作数据
     :return: pandas.DataFrame
    """
    url = "http://api.waizaowang.com/doc/getTSStockPosition"
    params = {"type": type,"code": code,"startDate": startDate,"endDate": endDate,"fields": fields,"export": export,"token": token,"filter": filter}
    if method == 'post':
        response = requests.post(url, params=params)
        return response.text
    else:
        response = requests.get(url, params=params)
        return response.text


if __name__ == "__main__":
    print("http://www.waizaowang.com")


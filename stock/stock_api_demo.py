import os

from stock import export_tool
from stock.api import stock_api

if __name__ == '__main__':
    print("StockApiDemo")
    token: str = "e80da5d374d50461fd52080d43a0f591"  # 歪枣网（www.waizaowang.com）上登录后获取Token

    # 请求日线数据，返回JSON格式
    data: str = stock_api.getDayKLine(
        1,
        "all",  # 请求A股所有股票
        101,
        1,
        "2024-02-01",  # code选择all的场景下，开始日期和结束日期必须相同，表示返回市场上当天所有股票的数据
        "2024-02-01",
        "all",  # 返回全部字段，也可以定制字段
        1,  # 返回Json数据类型
        token,
        "",
        "get")  # get请求

    # 生成Json文件
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "waizaowang_export.json")
    export_tool.toFile(file, data)

    # 将Json格式数据转换为DataFrame格式数据
    result = export_tool.toDataFrame(data)

    # 请求日线数据，返回JSON格式
    data: str = stock_api.getDayKLine(
        1,
        "000001,000002",  # 请求部分股票
        101,
        1,
        "2024-01-01",
        "2025-01-01",
        "all",  # 返回全部字段，也可以定制字段
        5,  # 返回DataFrame格式数据类型
        token,
        "",
        "post")  # post请求
    result = export_tool.dataFrame(data)

    # 请求日线数据，返回csv格式文件
    data: str = stock_api.getDayKLine(
        1,
        "000001,000002",  # 请求部分股票
        101,
        1,
        "2024-01-01",
        "2025-01-01",
        "all",  # 返回全部字段，也可以定制字段
        4,  # 返回Csv格式文件
        token,
        "",
        "post")  # post请求
    result = export_tool.dataFrame(data)
    # 生成Csv文件
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "waizaowang_export.csv")
    export_tool.toFile(file, data)

    # 请求日线数据，返回txt格式数据
    data: str = stock_api.getDayKLine(
        1,
        "000001,000002",  # 请求部分股票
        101,
        1,
        "2024-01-01",
        "2025-01-01",
        "all",  # 返回全部字段，也可以定制字段
        0,  # 返回Csv格式文件
        token,
        "",
        "post")  # post请求

    print(data)

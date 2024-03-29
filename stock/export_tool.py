import json

import pandas as pd


def toFile(file: str, data: str):
    """
    将请求返回的字符串数据写到文件中，包括Csv、Json、Txt文件
    :param file: 文件路径
    :param data: 字符串
    """
    with open(file, "w") as file:
        file.write(data)


def toDataFrame(data: str) -> pd.DataFrame:
    """
    将请求返回的Json格式数据转换为DataFrame格式
    :param data: Json格式数据
    """
    return pd.DataFrame(json.loads(data)["data"])


def dataFrame(data: str) -> pd.DataFrame:
    """
    将请求返回的DataFrame格式数据重新转换为DataFrame格式
    :param data: DataFrame格式数据（数据中zh为中文标题，en为英文标题）
    """
    json_data = json.loads(data)
    temp_df = pd.DataFrame(json_data["data"])
    temp_df.columns = json_data["zh"]  # 请求数据对应的字段名称
    return temp_df


if __name__ == '__main__':
    print("StockApiDemo")

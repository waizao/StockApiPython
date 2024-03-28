import os

from stock import export_tool
from stock.api import stock_api

if __name__ == '__main__':
    print("StockApiDemo")
    token: str = ""
    data: str = stock_api.getDayKLine(1, "000001,000002", 101, 1, "2023-01-01", "2024-01-01", "all", 1,
                                      token,
                                      "", "get")
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.json")
    print(file)
    export_tool.toFile(file, data)
    result = export_tool.toDataFrame(data)

    data: str = stock_api.getDayKLine(1, "000001,000002", 101, 1, "2023-01-01", "2024-01-01", "all", 5,
                                      token,
                                      "", "get")
    result = export_tool.dataFrame(data)
    print(result)

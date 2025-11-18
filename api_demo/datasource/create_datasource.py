#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.api.datasource_api import DatasourceAPI
from common.exceptions import APIException

def main():
    try:
        # 初始化API客户端
        api = DatasourceAPI()
        
        # 创建数据源
        result = api.create_datasource(
            datasource_type="MYSQL",
            name="txx",
            host="localhost",
            port=3306,
            username="root",
            password="xxx",
            database="ds",
            note="",
            other={"serverTimezone": "GMT-8"}
        )
        print(result)
        
    except APIException as e:
        print(f"Error creating datasource: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.api.datasource_api import DatasourceAPI
from common.exceptions import APIException

def main():
    if len(sys.argv) < 3:
        print("Usage: {} <datasource-id> <database-name>".format(sys.argv[0]))
        sys.exit(1)
    
    datasource_id = sys.argv[1]
    database_name = sys.argv[2]
        
    try:
        # 初始化API客户端
        api = DatasourceAPI()
        
        # 获取数据库表列表
        tables = api.list_tables(datasource_id, database_name)
        
        for table in tables:
            print(table)
        
    except APIException as e:
        print(f"Error getting tables: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
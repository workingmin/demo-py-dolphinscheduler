#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.api.datasource_api import DatasourceAPI
from common.exceptions import APIException

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <database-type>".format(sys.argv[0]))
        print("Available values : MYSQL, POSTGRESQL, HIVE, SPARK, " \
            "CLICKHOUSE, ORACLE, SQLSERVER, DB2, PRESTO, H2, REDSHIFT, " \
            "ATHENA, TRINO, STARROCKS, AZURESQL, DAMENG, OCEANBASE, SSH, " \
            "KYUUBI, DATABEND, SNOWFLAKE, VERTICA, HANA, DORIS")
        sys.exit(1)
            
    database_type = sys.argv[1]
    
    try:
        # 初始化API客户端
        api = DatasourceAPI()
        
        # 按数据库类型查询数据源列表
        datasources = api.list_datasources_by_type(database_type)
        
        for datasource in datasources:
            print(datasource)
        
    except APIException as e:
        print(f"Error querying datasource list: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
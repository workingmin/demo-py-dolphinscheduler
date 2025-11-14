#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.api.project_api import ProjectAPI
from common.exceptions import APIException

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <project-code>".format(sys.argv[0]))
        sys.exit(1)
    
    project_code = sys.argv[1]
    
    # 初始化API客户端
    api = ProjectAPI()
    
    # 查询项目 (v2)
    project = api.get_project(project_code, version="v2")
    print(project)
    
    try:
        # 初始化API客户端
        api = ProjectAPI()
        
        # 查询项目 (v2)
        project = api.get_project(project_code, version="v2")
        print(project)
        
    except APIException as e:
        print(f"Error querying project: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
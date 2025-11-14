#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.api.project_api import ProjectAPI
from common.exceptions import APIException

def format_project(project: dict) -> str:
    return "{:<10} {:<20} {:<30}".format(project['id'], project['code'], project['name'])

def main():
    try:
        # 初始化API客户端
        api = ProjectAPI()
        
        # 查询所有项目 (v2)
        projects = api.list_all_projects(version="v2")
        
        print("\nProjects List:")
        print("{:<10} {:<20} {:<30}".format("ID", "Code", "Project Name"))
        print("-" * 60)
        for project in projects:
            print(format_project(project))
            
    except APIException as e:
        print(f"API Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
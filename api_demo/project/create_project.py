#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.api.project_api import ProjectAPI
from common.exceptions import APIException

def main():
    try:
        # 初始化API客户端
        api = ProjectAPI()

        # 创建项目 (v1)
        v1_project = api.create_project(
            "v1_project",
            "v1 description",
            version="v1"
        )
        
        if v1_project:
            print("Project created successfully:")
            print(v1_project)
        else:
            print("Failed to create project.")
            
    except APIException as e:
        print(f"Error creating project: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

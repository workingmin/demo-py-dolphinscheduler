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
        
        # 创建项目 (v2)
        v2_project = api.create_project("v2_project", "v2 description", version="v2")
        print("Project created successfully:")
        print(v2_project)
        
    except APIException as e:
        print(f"Failed to create project: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()

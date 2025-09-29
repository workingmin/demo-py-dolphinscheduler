#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
from common.api.project_api import ProjectAPI
from common.utils.config_util import load_config

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <project-code>".format(sys.argv[0]))
        sys.exit(1)
    
    project_code = sys.argv[1]
    
    # 加载配置
    server_url, user_token = load_config()

    # 初始化API客户端
    api = ProjectAPI(server_url, user_token)

    # 删除项目 (v1)
    api.delete_project(project_code, version="v1")
    
    print("Project deleted successfully.")


if __name__ == '__main__':
    main()
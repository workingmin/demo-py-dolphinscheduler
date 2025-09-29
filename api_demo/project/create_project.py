#!/bin/env python3
# -*- coding: utf-8 -*-

from common.api.project_api import ProjectAPI
from common.utils.config_util import load_config

def main():
    # 加载配置
    server_url, user_token = load_config()

    # 初始化API客户端
    api = ProjectAPI(server_url, user_token)

    # 创建项目 (v1)
    v1_project = api.create_project("pro123", "this is a project", version="v1")
        
    print("Project created successfully:")
    print(v1_project)


if __name__ == '__main__':
    main()

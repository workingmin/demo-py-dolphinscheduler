#!/bin/env python3
# -*- coding: utf-8 -*-

from common.api.project_api import ProjectAPI
from common.utils.config_util import load_config

def main():
    # 加载配置
    server_url, user_token = load_config()

    # 初始化API客户端
    api = ProjectAPI(server_url, user_token)

    # 创建项目 (v2)
    v2_project = api.create_project("v2_project", "v2 description", version="v2")
        
    print("Project created successfully:")
    print(v2_project)


if __name__ == '__main__':
    main()

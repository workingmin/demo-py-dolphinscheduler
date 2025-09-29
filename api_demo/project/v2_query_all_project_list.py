#!/bin/env python3
# -*- coding: utf-8 -*-

from common.api.project_api import ProjectAPI
from common.utils.config_util import load_config

def main():
    # 加载配置
    server_url, user_token = load_config()

    # 初始化API客户端
    api = ProjectAPI(server_url, user_token)

    # 查询所有项目 (v2)
    all_projects = api.list_all_projects(version="v2")
        
    print("All projects:")
    for project in all_projects:
        print(f"- {project['id']}: {project['name']}")


if __name__ == '__main__':
    main()
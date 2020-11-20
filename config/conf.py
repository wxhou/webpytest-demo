#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from config import *
from common.readconfig import ReadConfig

# 测试项目应用管理
apps = {
    'apps': os.path.join(BASE_DIR, 'apps'),
    'baidu': os.path.join(BASE_DIR, 'apps', 'baidu'),
}

# 测试项目配置文件应用管理
ini = {
    "baidu": ReadConfig(apps['baidu'])
}

# 测试项目元素文件应用管理
element = {
    "baidu": os.path.join(apps['baidu'], 'page', 'elements')
}

# airimages图片管理
airimages = {
    'baidu': os.path.join(apps['baidu'], 'page', 'images')
}

if __name__ == '__main__':
    print(ini['baidu'].url)

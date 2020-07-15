#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from common.readconfig import ReadConfig
from selenium.webdriver.common.by import By

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 截图目录
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screen_capture')

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}

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

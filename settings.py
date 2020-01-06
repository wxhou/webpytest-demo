#!/usr/bin/env python3
# coding=utf-8
import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置文件
CONFIG_PATH = os.path.join(BASE_DIR, 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'PageElements')

# SQLite数据库
SQLITE_PATH = os.path.join(BASE_DIR, 'TestData', 'sqlite3.sqlite')

# 截图目录
SCREENSHOT_PATH = os.path.join(BASE_DIR, 'screenshot')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')


if __name__ == '__main__':
    print(BASE_DIR)

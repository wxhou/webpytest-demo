#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'PageElements')

# airtest图像目录
AIRTEST_PATH = os.path.join(BASE_DIR, 'airtest_image')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 用例目录
TEST_SUITES = os.path.join(BASE_DIR, 'TestData')

if __name__ == '__main__':
    print(BASE_DIR)

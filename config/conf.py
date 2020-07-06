#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os
from selenium.webdriver.common.by import By

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

# airtest图像目录
PAGE_IMAGE = os.path.join(BASE_DIR, 'page_images')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 截图目录
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screen_capture')

# 用例目录
TEST_SUITES = os.path.join(BASE_DIR, 'TestCase')

# allure结果目录
ALLURE_RESULTS = os.path.join(BASE_DIR, 'allure-results')

# allure报告目录
ALLURE_REPORT = os.path.join(BASE_DIR, 'allure-report')

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}

if __name__ == '__main__':
    print(BASE_DIR)

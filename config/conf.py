#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By
from utils.times import datetime_strftime
from common.readconfig import ReadConfig


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # 日志目录
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

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
    tests = {
        'tests': os.path.join(BASE_DIR, 'tests'),
        'baidu': os.path.join(BASE_DIR, 'tests', 'test_baidu')
    }

    # 测试项目配置文件应用管理
    ini = {
        "baidu": ReadConfig(tests['baidu'])
    }

    # 测试项目元素文件应用管理
    element = {
        "baidu": os.path.join(tests['baidu'], 'page', 'elements')
    }

    # airimages图片管理
    airimages = {
        'baidu': os.path.join(tests['baidu'], 'page', 'images')
    }

    @property
    def screen_path(self):
        """截图目录"""
        if not os.path.exists(self.SCREENSHOT_DIR):
            os.makedirs(self.SCREENSHOT_DIR)
        _now = datetime_strftime("%Y%m%d%H%M%S")
        screen_file = os.path.join(self.SCREENSHOT_DIR, "{}.png".format(_now))
        return _now, screen_file

    @property
    def log_path(self):
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)
        return os.path.join(self.LOG_DIR, '{}.log'.format(datetime_strftime()))


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)

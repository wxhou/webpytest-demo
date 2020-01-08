#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   basepage.py
@Time    :   2020-01-07 15:14:28
@Author  :   wxhou 
@Version :   1.0
@Contact :   1084502012@qq.com
'''
import sys
sys.path.append('.')
from .webpage import WebPage, sleep, log
from common.readelement import Element
import time
from selenium.common.exceptions import TimeoutException

base = Element('base')


class BasePage(WebPage):
    """管理平台基类"""
    def get_exist_text(self, value):
        """DOM中存在的文本"""
        return self.Exists(base.找页面文本 % value)

    def get_visible_text(self, value):
        """可见的文本"""
        return self.isElementVisible(base.找页面文本 % value)

if __name__ == '__main__':
    pass

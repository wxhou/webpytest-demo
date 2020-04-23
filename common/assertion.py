# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
from Page.webpage import WebPage, base

"""
断言文件
"""


def assert_text_is_dom(driver, text):
    """验证文字在DOM中"""
    assert WebPage(driver).element_exists(base['模糊匹配文字'] % text), "文字{}未在DOM中加载".format(text)


def assert_text_visible(driver, text):
    """验证文字是否可见"""
    assert WebPage(driver).element_visible(base['模糊匹配文字'] % text), "文字{}不可见".format(text)


if __name__ == '__main__':
    pass

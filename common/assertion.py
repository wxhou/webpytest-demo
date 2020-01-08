#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   assertion.py
@Time    :   2020-01-07 15:13:03
@Author  :   wxhou 
@Version :   1.0
@Contact :   1084502012@qq.com
'''
import sys
sys.path.append('.')
from Page.basepage import BasePage

def assert_visible_text(driver, value):
    """断言页面文字"""
    ast = BasePage(driver)
    assert ast.get_visible_text(value), "名称%s 在页面不存在，添加失败"



def assert_exists_text(driver, value):
    """断言文字在DOM存在"""
    ast = BasePage(driver)
    assert ast.get_exist_text(value), "名称 %s 在DOM中不存在" % value

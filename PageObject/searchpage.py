#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   searchpage.py
@Time    :   2019/09/28 11:54:22
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys

sys.path.append('.')
from Page.webpage import WebPage, sleep
from common.readyaml import Element

login = Element('login')
search = Element('search')


class SearchPage(WebPage):
    def input_search(self, content):
        """输入搜索"""
        self.input_text(search.搜索框, text=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        result_number = range(1, self.isElementNum(search.候选) + 1)
        return map(lambda x: self.isElementText(search.搜索候选, number=x),
                   result_number)

    def click_search(self):
        """点击搜索"""
        self.is_click(search.搜索按钮)

    def login(self, user, pwd):
        """登录"""
        self.is_click(login.登录)
        if not self.textInElement(login.登录方式, text="用户名密码登录"):
            self.is_click(login.用户名登录)
        self.input_text(login.用户名, text=user)
        self.input_text(login.密码, text=pwd)
        self.is_click(login.记住登录)
        self.is_click(login.点击登录)
        sleep(2)


if __name__ == '__main__':
    pass

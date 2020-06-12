#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')
search = Element('search')


class SearchPage(WebPage):
    def input_search(self, content):
        """输入搜索"""
        self.input_text(search['搜索框'], text=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        result_number = range(1, self.elements_num(search['候选']) + 1)
        return map(lambda x: self.get_text(search['搜索候选'], number=x),
                   result_number)

    def click_search(self):
        """点击搜索"""
        self.is_click(search['搜索按钮'])

    def login(self, user, pwd):
        """登录"""
        self.is_click(login['登录'])
        if not self.text_in_element(login['登录方式'], text="用户名密码登录"):
            self.is_click(login['用户名登录'])
        self.input_text(login['用户名'], text=user)
        self.input_text(login['密码'], text=pwd)
        self.is_click(login['记住登录'])
        self.is_click(login['点击登录'])
        sleep(2)


if __name__ == '__main__':
    pass

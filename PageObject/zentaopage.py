#!/usr/bin/env python3
# coding=utf-8
import sys

sys.path.append('.')
from Page.webpage import WebPage, sleep
from common.readyaml import element


class ZenTao(WebPage):
    def login(self, usr, pwd):
        self.input_text(element.账号, text=usr)
        self.input_text(element.密码, text=pwd)
        self.is_click(element.提交)

    def keeplogin(self):
        self.is_click(element.保持登录)

    def quit_login(self):
        self.is_click(element.用户名)
        self.is_click(element.退出)

    def add_product(self, name, code):
        self.is_click(element.产品)
        self.is_click(element.添加产品)
        self.input_text(element.产品名称, text=name)
        self.input_text(element.产品代号, text=code)
        self.focus(element.保存)
        self.is_click(element.保存)
        sleep(5)


if __name__ == '__main__':
    pass

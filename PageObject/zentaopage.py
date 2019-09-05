#!/usr/bin/env python3
# coding=utf-8
import sys

sys.path.append('.')
from Page.webpage import WebPage, sleep
from common.readconfig import element


class ZenTao(WebPage):
    def login(self, usr, pwd):
        self.input_text(element('zentao', '账号'), text=usr)
        self.input_text(element('zentao', '密码'), text=pwd)
        self.is_click(element('zentao', '提交'))

    def keeplogin(self):
        self.is_click(element('zentao', '保持登录'))

    def quit_login(self):
        self.is_click(element('zentao', '用户名'))
        self.is_click(element('zentao', '退出'))

    def add_product(self, name, code):
        self.is_click(element('zentao', '产品'))
        self.is_click(element('zentao', '添加产品'))
        self.input_text(element('zentao', '产品名称'), text=name)
        self.input_text(element('zentao', '产品代号'), text=code)
        self.focus(element('zentao', '保存'))
        self.is_click(element('zentao', '保存'))
        sleep(5)


if __name__ == '__main__':
    pass

#!/usr/bin/env python3
# coding=utf-8
from Page.webpage import WebPage, sleep
from utils.readconfig import Element

element = Element()


class ZenTao(WebPage):
    def login(self, usr, pwd):
        self.input_text(element('zentao', '账号'), text=usr)
        self.input_text(element('zentao', '密码'), text=pwd)
        self.is_click(element('zentao', '登录'))

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

    def add_bug(self):
        self.is_click(element('zentao', '测试'))
        self.is_click(element('zentao', 'bug'))
        self.is_click(element('zentao', '提bug'))
        self.click_drop_down(selectlocator=element('zentao', '当前指派'),
                             optionlocator=element('zentao', '选项'),
                             optionnumber=2)
        self.click_drop_down(selectlocator=element('zentao','影响版本'),optionlocator=element('zentao','选项'),
                             optionnumber=1)

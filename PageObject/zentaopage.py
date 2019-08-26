#!/usr/bin/env python3
# coding=utf-8
from Page.webpage import WebPage,sleep
from utils.readconfig import Element

element = Element()


class ZenTao(WebPage):
    def add_product(self, name, code):
        self.is_click(element('zentao', '产品'))
        self.is_click(element('zentao', '添加产品'))
        self.input_text(element('zentao', '产品名称'), text=name)
        self.input_text(element('zentao', '产品代号'), text=code)
        self.is_click(element('zentao', '保存'))
        sleep(5)
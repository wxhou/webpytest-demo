#!/usr/bin/env python3
# coding=utf-8
from Page.webpage import WebPage
from utils.readconfig import Element

element = Element()


class FastLogin(WebPage):
    def login(self, usr, pwd):
        self.input_text(element('fastadmin', '账户'), text=usr)
        self.input_text(element('fastadmin', '密码'), text=pwd)
        self.is_click(element('fastadmin', '登录'))

    def keeplogin(self):
        self.is_click(element('fastadmin', '保持会话'))

    def quit_login(self):
        self.is_click(element('fastadmin', '用户头像'))
        self.is_click(element('fastadmin', '注销'))

    def logo(self, shot_name):
        '''截取logo'''
        return self.screenshots_of_element(element('fastadmin', 'logo'),
                                           screenshot_path=shot_name)


class ZenTaoLogin(WebPage):
    def login(self, usr, pwd):
        self.input_text(element('zentao', '账号'), text=usr)
        self.input_text(element('zentao', '密码'), text=pwd)
        self.is_click(element('zentao', '登录'))

    def keeplogin(self):
        self.is_click(element('zentao', '保持登录'))

    def quit_login(self):
        self.is_click(element('zentao', '用户名'))
        self.is_click(element('zentao', '退出'))



if __name__ == '__main__':
    pass

#!/usr/bin/env python3
# coding=utf-8
from Page.webpage import WebPage
from utils.readconfig import Element

element = Element()


class LoginPage(WebPage):
    def login(self, usr, pwd):
        self.input_text(element('login', '账户'), text=usr)
        self.input_text(element('login', '密码'), text=pwd)
        self.is_click(element('login', '登录'))

    def keeplogin(self):
        self.is_click(element('login', '保持会话'))

    def quit_login(self):
        self.is_click(element('login', '用户头像'))
        self.is_click(element('login', '注销'))

    def logo(self, shot_name):
        '''截取logo'''
        return self.screenshots_of_element(element('home', 'logo'),
                                           screenshot_path=shot_name)


if __name__ == '__main__':
    pass

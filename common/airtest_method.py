#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
from airtest_selenium.proxy import WebChrome
from tools.images import get_airtest_image
from airtest.core.cv import Template
from tools.times import sleep


class AirtestMethod:
    """airtest-selenium方法"""

    def __init__(self, driver):
        self.driver = driver
        self.size = self.driver.get_window_size()
        self.width = self.size['width']
        self.height = self.size['height']

    def template(self, name):
        """被识别的图片Template对象"""
        return Template(name, record_pos=(self.width / 2, self.height / 2), resolution=(self.width, self.height))

    def touch_image(self, name):
        """
        点击网页中的图片
        :param name: 图片名称
        """
        v = self.template(get_airtest_image(name))
        self.driver.airtest_touch(v)
        sleep(3)

    def assert_template(self, name, msg=None):
        """验证网页中图片存在
        :param name: 图片的名称
        :param msg:
        """
        v = self.template(get_airtest_image(name))
        self.driver.assert_template(v, msg)


if __name__ == '__main__':
    pass

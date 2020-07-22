#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config import apps
from utils.times import *
from utils.logger import log
from common.readelement import Element
from core.webpage import WebPage, getElement
from utils.images import area_screenshot, get_image_name
from selenium.common.exceptions import TimeoutException

base = Element(apps['apps'], 'base')


class NovaPage(WebPage):
    """WebPage的延伸方法"""

    def assert_text_dom(self, text):
        """验证文字在DOM中"""
        assert self.is_exists(base['模糊匹配文字'] % text), f"文字{text}未在DOM中加载"

    def assert_text_visible(self, text):
        """验证文字是否可见"""
        assert self.is_visible(base['模糊匹配文字'] % text), f"文字{text}不可见"

    def upload_file(self, locator, file_path, exists=None, number=None):
        """上传文件
        :param locator: 上传文件的元素 input[type=file]
        :param file_path: 文件的路径
        :param exists: 上传后要验证的元素
        :param number: 元素index
        """
        file_name = get_image_name(file_path)[0]
        values = getElement(locator, number)
        ele = self.find_element(values)
        self.focus(ele)
        ele.send_keys(file_path)
        log.info("正在上传文件：%s" % file_path)
        start_time = timestamp()
        if file_path.endswith(('.jpg', '.png')):
            exists = base['模糊匹配文字'] % file_name
        while not self.is_exists(exists):
            sleep(0.5)
            if (timestamp() - start_time) > self.timeout:
                raise TimeoutException("在元素【】上传文件【】失败" % ())
        sleep(3)
        log.info("上传文件【%s】成功！" % file_path)

    def element_screenshot(self, locator, path, number=None):
        """对某个元素进行截图,并返回截图路径"""
        values = getElement(locator, number)
        ele = self.find_element(values)
        self.focus(ele)  # 元素不可见则聚焦
        self.driver.save_screenshot(path)
        area_screenshot(ele, path)
        self.driver.implicitly_wait(1)
        log.info("截图的路径是：%s" % path)


if __name__ == '__main__':
    print(base['模糊匹配文字'])

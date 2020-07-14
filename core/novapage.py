#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config import element
from utils.times import *
from utils.logger import log
from core.webpage import WebPage
from common.readelement import Element
from utils.images import area_screenshot, get_image_name
from selenium.common.exceptions import TimeoutException

base = Element(element['baidu'], 'base')


class NovaPage(WebPage):
    """WebPage的延伸方法"""

    def upload_file(self, locator, file_path, exists=None, number=None):
        """上传文件
        :param locator: 上传文件的元素 input[type=file]
        :param file_path: 文件的路径
        :param exists: 上传后要验证的元素
        :param number: 元素index
        """
        file_name = get_image_name(file_path)[0]
        ele = self.find_element(locator, number)
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
        ele = self.find_element(locator, number)
        self.focus(ele)  # 元素不可见则聚焦
        self.driver.save_screenshot(path)
        area_screenshot(ele, path)
        self.driver.implicitly_wait(1)
        log.info("截图的路径是：%s" % path)

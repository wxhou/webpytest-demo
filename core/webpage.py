#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# selenium基类
# 本文件存放了selenium基类的深度封装方法
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *

from common.readelement import getElement
from utils.logger import logger
from utils.times import *


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = WebChrome()
        self.driver = driver
        self.timeout = 20
        self.visible = 3
        self.visible_obj = WebDriverWait(self.driver, self.visible)
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.action = ActionChains(self.driver)
        self.touch = TouchActions(self.driver)

    @logger
    def get_url(self, url, title=None):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except TimeoutException:
            raise ("打开%s超时,请检查网络或网址服务器" % url)
        if title:
            title2 = self.driver.title
            assert EC.title_is(title)(
                self.driver), "网页title不正确，应为%s，实为%s" % (title, title2)

    """
    基础函数
    """

    def find_element(self, *args, **kwargs):
        """寻找单个元素"""
        values = getElement(*args, **kwargs)
        return self.wait.until(EC.presence_of_element_located(values),
                               message="查找单个元素失败！{}".format(values))

    def find_elements(self, *args, **kwargs):
        """查找多个相同的元素"""
        values = getElement(*args, **kwargs)
        return self.wait.until(EC.presence_of_all_elements_located(values),
                               message="查找多个元素失败！{}".format(values))

    """
    获取函数
    """

    @logger(msg="元素个数:{}")
    def get_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        return number

    @logger(msg="元素文本：{}")
    def get_text(self, locator, number=None):
        """获取当前的text"""
        text = self.find_element(locator, number).text
        return text

    @logger(msg="元素坐标：{}")
    def get_location(self, locator, number=None):
        """获取元素的坐标"""
        location = self.find_element(locator, number).location
        return location['x'], location['y']

    """判断函数"""

    @logger
    def is_exists(self, locator, number=None):
        """元素是否存在(DOM)"""
        try:
            values = getElement(locator, number)
            return EC.presence_of_element_located(values)(self.driver)
        except NoSuchElementException:
            return False

    @logger
    def is_visible(self, locator, number=None):
        """元素是否可见"""
        try:
            values = getElement(locator, number)
            self.visible_obj.until(EC.visibility_of_element_located(values))
            return True
        except TimeoutException:
            return False

    @logger
    def is_refresh(self, locator, number=None):
        """判断页面是否刷新"""
        ele = self.find_element(locator, number)
        return EC.staleness_of(ele)

    @logger(msg="是否选中：{}")
    def is_selected(self, locator, number=None):
        """判断是否选中"""
        values = getElement(locator, number)
        return self.wait.until(EC.element_located_selection_state_to_be(values, True))

    @logger(msg="文本<{}>在元素中：{}")
    def text_in_element(self, locator, text, number=None):
        """检查某段文本是否在元素中"""
        values = getElement(locator, number)
        return EC.text_to_be_present_in_element(values, text)(self.driver)

    @logger(msg="弹窗提示：{}")
    def alert_text_exists(self):
        """判断弹框是否出现，并返回弹框的文字"""
        alert = EC.alert_is_present()(self.driver)
        text = alert.text
        alert.accept()
        return text

    """操作函数"""

    def focus(self, element):
        """聚焦元素"""
        self.driver.execute_script("arguments[0].focus();", element)

    @logger
    def clear(self, locator, number=None):
        """清空输入框"""
        ele = self.find_element(locator, number)
        self.focus(ele)
        ele.clear()
        self.driver.implicitly_wait(1)

    @logger
    def input_text(self, locator, text, number=None):
        """输入(输入前先清空)"""
        sleep(0.5)
        values = getElement(locator, number)
        ele = self.wait.until(EC.element_to_be_clickable(values),
                              message="在元素%s中，输入<%s>失败！" % (values, text))
        self.focus(ele)
        ele.clear()
        ele.send_keys(text)
        return text

    @logger
    def is_click(self, locator, number=None):
        """点击"""
        values = getElement(locator, number)
        ele = self.wait.until(EC.element_to_be_clickable(values),
                              message="点击元素{}失败！".format(values))
        self.focus(ele)
        ele.click()
        sleep()

    @logger
    def action_click(self, locator, number=None):
        """使用鼠标点击"""
        element = self.find_element(locator, number)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).perform()
        self.driver.implicitly_wait(1)

    @logger
    def action_input(self, locator, text, number=None):
        """action的输入方法"""
        element = self.find_element(locator, number)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).send_keys(text)
        self.action.perform()
        self.action._actions.pop()  # 防止重复输入
        return text

    @logger
    def internal_scroll_bar(self, class_name, func='Left', number='10000'):
        """
        内部滚动条（默认为向右滚动）
        :param class_name: class_name
        :param func: ['Left','Top']
        :param number: ['10000','0']
        """
        js1 = 'document.getElementsByClassName("%s")[0].scroll%s=%s' % (
            class_name, func, number)
        self.driver.execute_script(js1)

    @logger
    def select_drop_down(self, locator, number=None):
        """选择下拉框"""
        ele = self.find_element(locator, number)
        self.focus(ele)
        sleep(2)
        # 这里一定要加等待时间，否则会引起如下报错
        # Element is not currently visible and may not be manipulated
        return Select(ele)

    @logger
    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)


if __name__ == "__main__":
    pass

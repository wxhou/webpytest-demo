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
from config import LOCATE_MODE
from utils.logger import log
from utils.times import *
from functools import wraps


def getElement(locator, number=None):
    """获取元素"""
    pattern, value = locator.split("==")
    element_value = value % number if number else value
    locate_mode = LOCATE_MODE[pattern]
    log.info("定位方式：{} 元素值：{}".format(locate_mode, element_value))
    return locate_mode, element_value


def logger(msg):
    """selenium日志"""

    def wrappers(func):
        @wraps(func)
        def deco(*args, **kwargs):
            result = func(*args, **kwargs)
            log.info(msg.format(result))
            return result

        return deco

    return wrappers


class WebPage:
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

    def get_url(self, url, title=None):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("\t打开网页：%s" % url)
        except TimeoutException:
            raise ("打开%s超时,请检查网络或网址服务器" % url)
        if title:
            title2 = self.driver.title
            assert EC.title_is(title)(self.driver), "网页title不正确，应为%s，实为%s" % (title, title2)

    """
    基础函数
    """

    def find_element(self, args: tuple):
        """寻找单个元素"""
        return self.wait.until(EC.presence_of_element_located(args),
                               message="查找单个元素{}失败！".format(args))

    def find_elements(self, args: tuple):
        """查找多个相同的元素"""
        return self.wait.until(EC.presence_of_all_elements_located(args),
                               message="查找多个元素{}失败！".format(args))

    """
    获取函数
    """

    @logger(msg="元素个数:{}")
    def elements_num(self, locator):
        """获取相同元素的个数"""
        values = getElement(locator)
        number = len(self.find_elements(values))
        return number

    @logger("元素文本：{}")
    def get_text(self, locator, number=None):
        """获取当前的text"""
        values = getElement(locator, number)
        text = self.find_element(values).text
        return text

    """判断函数"""

    def is_exists(self, locator, number=None):
        """元素是否存在(DOM)"""
        try:
            values = getElement(locator, number)
            return EC.presence_of_element_located(values)(self.driver)
        except NoSuchElementException:
            return False

    def is_visible(self, locator, number=None):
        """元素是否可见"""
        try:
            values = getElement(locator, number)
            WebDriverWait(self.driver, self.visible).until(EC.visibility_of_element_located(values))
            return True
        except TimeoutException:
            return False

    def is_page_refresh(self, locator, number=None):
        """判断页面是否刷新"""
        values = getElement(locator, number)
        ele = self.find_element(values)
        return EC.staleness_of(ele)

    @logger(msg="文本<{}>在元素中：{}")
    def text_in_element(self, locator, text, number=None):
        """检查某段文本是否在元素中"""
        values = getElement(locator, number)
        return EC.text_to_be_present_in_element(values, text)(self.driver)

    @logger(msg="是否选中：{}")
    def is_selected(self, locator, number=None):
        """判断是否选中"""
        values = getElement(locator, number)
        return self.wait.until(EC.element_located_selection_state_to_be(values, True))

    @logger("弹窗提示：{}")
    def alert_text_exists(self):
        """判断弹框是否出现，并返回弹框的文字"""
        alert = EC.alert_is_present()(self.driver)
        text = alert.text
        alert.accept()
        return text

    """操作函数"""

    def focus(self, element):  # 该函数的编写来源于robot-framework-selenium
        """聚焦元素"""
        self.driver.execute_script("arguments[0].focus();", element)

    @logger("清空输入框:{}")
    def clear(self, locator, number=None):
        """清空输入框"""
        values = getElement(locator, number)
        ele = self.find_element(values)
        self.focus(ele)
        ele.clear()
        self.driver.implicitly_wait(1)

    @logger("输入文本：{}")
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

    @logger("点击元素")
    def is_click(self, locator, number=None):
        """点击"""
        values = getElement(locator, number)
        ele = self.wait.until(EC.element_to_be_clickable(values),
                              message="点击元素{}失败！".format(values))
        self.focus(ele)
        ele.click()
        sleep()

    @logger(msg="鼠标点击")
    def action_click(self, locator, number=None):
        """使用鼠标点击"""
        values = getElement(locator, number)
        element = self.find_element(values)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).perform()
        self.driver.implicitly_wait(1)

    @logger("action输入:{}")
    def action_input(self, locator, text, number=None):
        """action的输入方法"""
        values = getElement(locator, number)
        element = self.find_element(values)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).send_keys(text)
        self.action.perform()
        log.info("使用：%s" % text)
        self.action._actions.pop()  # 防止重复输入
        return text

    def internal_scroll_bar(self, class_name, func='Left', number='10000'):
        """
        内部滚动条（默认为向右滚动）
        :param class_name: class_name
        :param func: ['Left','Top']
        :param number: ['10000','0']
        """
        js1 = 'document.getElementsByClassName("%s")[0].scroll%s=%s' % (class_name, func, number)
        self.driver.execute_script(js1)

    def select_drop_down(self, locator, number=None):
        """选择下拉框"""
        values = getElement(locator, number)
        ele = self.find_element(values)
        self.focus(ele)
        sleep(2)
        # 这里一定要加等待时间，否则会引起如下报错
        # Element is not currently visible and may not be manipulated
        return Select(ele)

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        log.info("刷新当前网页!")
        self.driver.implicitly_wait(30)


if __name__ == "__main__":
    pass

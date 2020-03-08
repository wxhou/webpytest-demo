#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from airtest_selenium import WebChrome
from common.airtest_method import airtest_assert_exists
from common.images import element_screenshot, get_image_name
from utils.logger import Logger
import time

"""
selenium基类
本文件存放了selenium基类的深度封装方法
"""
log = Logger('page').logger

LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}  # 元素定位的类型


def sleep(seconds=1.0):
    '''
    等待时间
    有些步骤不强制等待，只用显式等待会导致执行报错
    '''
    time.sleep(seconds)


def element_value(locator, number):
    """元素值"""
    return locator % number if number else locator


class WebPage:
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = WebChrome()
        self.driver = driver
        self.timeout = 10
        self.visible = 3
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.action = ActionChains(self.driver)
        self.touch = TouchActions(self.driver)

    @staticmethod
    def selector(func, locator, number=None):
        """选择器"""
        pattern, value = locator.split('==')
        return func(LOCATE_MODE[pattern], element_value(value, number))

    def get_url(self, url, title=None):
        '''打开网址并验证'''
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

    def findelement(self, locator, number=None):
        """寻找单个元素"""
        return WebPage.selector(
            lambda *args: self.wait.until(lambda x: x.find_element(*args),
                                          message="查找单个元素%s失败！" % element_value(locator, number)),
            locator, number)

    def findelements(self, locator, number=None):
        """查找多个相同的元素"""
        return WebPage.selector(
            lambda *args: self.wait.until(lambda x: x.find_elements(*args),
                                          message="查找单个元素%s失败！" % element_value(locator, number)),
            locator, number)

    def Exists(self, locator, number=None):  # 判断元素是否在DOM中
        '''元素是否存在(DOM)'''
        try:
            WebPage.selector(lambda *args: EC.presence_of_element_located(args)(self.driver),
                             locator, number=number)
            return True
        except:
            return False

    def isElementVisible(self, locator, number=None):
        '''元素是否可见'''
        try:
            WebPage.selector(lambda *args: WebDriverWait(self.driver, self.visible).until(
                EC.visibility_of_element_located(args)), locator, number)
            return True
        except:
            return False

    def focus(self, element):  # 该函数的编写来源于robot-framework-selenium
        """聚焦元素"""
        self.driver.execute_script("arguments[0].focus();", element)

    def inline_scroll_bar(self, element, func='Left', number='10000'):
        """
        内嵌滚动条（默认为向右滚动）
        :param func: ['Left','Top']
        :param number: ['10000','0']
        """
        js1 = 'document.getElementsByClassName("%s")[0].scroll%s=%s' % (element, func, number)
        self.driver.execute_script(js1)

    def isElementNum(self, locator):  # 获取相同元素的个数
        '''获取相同元素的个数'''
        number = len(self.findelements(locator))
        log.info("元素%s的个数是：%s" % (locator, number))
        return number

    def is_clear(self, locator, number=None):
        '''清空输入框'''
        ele = self.findelement(locator, number)
        self.focus(ele)
        ele.clear()
        log.info("清空输入框：%s" % element_value(locator, number))
        self.driver.implicitly_wait(1)

    def input_text(self, locator, text, number=None):
        '''输入(输入前先清空)'''
        sleep(0.5)
        msg = element_value(locator, number)
        ele = WebPage.selector(lambda *args: self.wait.until(
            EC.element_to_be_clickable(args), message="在元素%s中，输入【%s】失败！" % (msg, text)), locator, number)
        self.focus(ele)
        ele.clear()
        ele.send_keys(text)
        log.info("在元素%s中输入%s" % (element_value(locator, number), text))

    def is_click(self, locator, number=None):
        '''点击'''
        msg = element_value(locator, number)
        ele = WebPage.selector(lambda *args: self.wait.until(
            EC.element_to_be_clickable(args), message="点击元素%s失败！" % msg), locator, number)
        self.focus(ele)
        ele.click()
        log.info("点击元素%s" % msg)
        sleep()

    def isPagerefresh(self, locator, number=None):
        """判断页面是否刷新"""
        ele = self.findelement(locator, number)
        return EC.staleness_of(ele)

    def isElementText(self, locator, number=None):
        '''获取当前的text'''
        __text = self.findelement(locator, number).text
        log.info("获取元素%s文字：[%s]" % (element_value(locator, number), __text))
        return __text

    def textInElement(self, locator, text, number=None):
        '''检查某段文本在输入框中'''
        log.info("检查文本【%s】在输入框%s中" % (text, element_value(locator, number)))
        return WebPage.selector(lambda *args: EC.text_to_be_present_in_element(args, text)(
            self.driver), locator, number)

    def isSelected(self, locator, number=None):
        '''判断是否选中'''
        log.info("检查元素:%s 是否被选中" % element_value(locator, number))
        return WebPage.selector(lambda *args: self.wait.until(
            EC.element_located_selection_state_to_be(args, True)), locator, number)

    def action_click(self, locator, number=None):
        '''使用鼠标点击'''
        element = self.findelement(locator, number)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).perform()
        log.info("使用鼠标点击：%s" % element_value(locator, number))
        self.driver.implicitly_wait(1)

    def action_sendkeys(self, locator, text, number=None):
        '''action的输入方法'''
        element = self.findelement(locator, number)
        self.focus(element)
        self.action.pause(0.5).click(element).pause(0.5).send_keys(text)
        self.action.perform()
        log.info("使用鼠标方法输入：%s" % text)
        self.action._actions.pop()  # 防止重复输入

    def upload_File(self, locator, filepath, number=None):
        """上传文件"""
        name = get_image_name(filepath)[0]
        ele = self.findelement(locator, number)
        self.focus(ele)
        ele.send_keys(filepath)
        log.info("正在上传文件：%s" % filepath)
        start_time = time.time()
        while True:
            try:
                airtest_assert_exists(self.driver, locator % name)
                break
            except AssertionError:
                sleep(0.5)
            if (time.time() - start_time) > self.timeout:
                raise TimeoutException("在元素【】上传文件【】失败" % ())
        log.info("上传文件【%s】成功！" % filepath)

    def screenshots_of_element(self, locator, path, number=None):
        '''对某个元素进行截图,并返回截图路径'''
        ele = self.findelement(locator, number)
        self.focus(ele)  # 元素不可见则聚焦
        self.driver.save_screenshot(path)
        self.shot_file(path)
        element_screenshot(ele, path)
        self.driver.implicitly_wait(1)
        log.info("截图的路径是：%s" % path)
        return path

    def select_drop_down(self, locator, number=None):
        """选择下拉框"""
        ele = self.findelement(locator, number)
        self.focus(ele)
        sleep(2)
        # 这里一定要加等待时间，否则会引起如下报错
        # Element is not currently visible and may not be manipulated
        return Select(ele)

    def alertTextExists(self):
        """判断弹框是否出现，并返回弹框的文字"""
        alert = EC.alert_is_present()(self.driver)
        text = alert.text
        log.info("Alert弹窗提示为：%s" % text)
        alert.accept()
        return text

    def switchToFrame(self, locator, number=None):
        """切换iframe"""
        log.info("切换最新的iframe")
        return WebPage.selector(lambda *args: self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(args)), locator, number)

    def switchToDefaultFrame(self):
        """返回默认"""
        self.driver.switch_to.default_content()
        log.info("返回至默认的iframe")

    def switchWindowshandle(self):
        '''切换最新的标签'''
        now_handle1 = self.driver.current_window_handle
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[-1])
        now_handle2 = self.driver.current_window_handle
        for i in range(3, 0, -1):
            try:
                assert now_handle1 != now_handle2
                log.info('切换新标签成功！%s' % self.driver.title)
                break
            except AssertionError:
                log.exception("切换标签失败！正在重试，还有%d机会！" % i)
        else:
            log.error("切换标签失败!请检查！")

    @property
    def getSource(self):
        """获取页面源代码"""
        log.info("获取页面的源码！")
        return self.driver.page_source

    def shot_file(self, path):
        '''文件截图'''
        log.info("正在进行PNG截图！生成文件为：%s" % path)
        return self.driver.save_screenshot(path)

    def close(self):
        '''关闭当前标签'''
        log.info("关闭浏览器标签")
        self.driver.close()

    def refresh(self):
        '''刷新页面F5'''
        self.driver.refresh()
        log.info("刷新当前网页!")
        self.driver.implicitly_wait(30)


if __name__ == "__main__":
    pass

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import pytest
from config import conf
from py._xmlgen import html
from airtest_selenium import WebChrome
from utils.clear_data import clear_old_data
from common.inspect_element import inspect_element

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    inspect_element()
    if driver is None:
        driver = WebChrome()
        driver.maximize_window()

    def fn():
        print("当全部用例执行完之后：quit driver！")
        driver.quit()
        clear_old_data(conf.TEST_SUITES)
        clear_old_data(conf.BASE_DIR)

    request.addfinalizer(fn)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()  # base64截图
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        # report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
        # 最新版本的pytest-html报告，已经可以实现自动转码了
        # plugin.py文件中
        # class TestResult:
        #     def __init__(self, outcome, report, logfile, config):
        #         self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
        #         if getattr(report, "when", "call") != "call":
        #             self.test_id = "::".join([report.nodeid, report.when])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('未捕获日志输出.', class_='empty log'))


def _capture_screenshot():
    '''
    截图保存为base64
    :return: base64字符串
    '''
    return driver.get_screenshot_as_base64()

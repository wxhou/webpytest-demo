#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from utils.logger import log
from common.readimage import get_image
from core.aircore import AirtestMethod
from config import ini, apps, airimages
from apps.baidu.page.objects.searchpage import SearchPage


@allure.feature("测试百度模块")
class TestSearch:
    @pytest.fixture(scope='class', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        airtest = AirtestMethod(drivers)
        search.get_url(ini['baidu'].url)
        airtest.assert_template(get_image(airimages['baidu'], "百度首页logo"))

    @allure.story("搜索结果用例")
    @pytest.mark.parametrize("value", ["selenium", "你好"])
    def test_001(self, drivers, value):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search(value)
        search.click_search()
        result = re.search(value, drivers.page_source)
        log.info(result)
        assert result

    @allure.story("测试搜索候选用例")
    @pytest.mark.parametrize("value", ["selenium", "你好"])
    def test_002(self, drivers, value):
        """测试搜索候选"""
        search = SearchPage(drivers)
        search.input_search(value)
        results = list(search.imagine)
        log.info(results)
        assert all([value in i for i in results])


if __name__ == '__main__':
    pytest.main(['test_search.py'])

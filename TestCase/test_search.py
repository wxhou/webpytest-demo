#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import re
import pytest
from PageObject.searchpage import SearchPage
from common.airtest_method import AirTestMethod
from common.readconfig import ini
from utils.logger import log


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        airtest = AirTestMethod(drivers)
        search.get_url(ini.url)
        airtest.assert_template("百度首页logo")

    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
        assert 0
        result = re.search(r'selenium', drivers.page_source)
        log.info(result)
        assert result

    def test_002(self, drivers):
        """测试搜索候选"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        results = list(search.imagine)
        log.info(results)
        assert all(["selenium" in i for i in results])


if __name__ == '__main__':
    pytest.main(['test_search.py'])

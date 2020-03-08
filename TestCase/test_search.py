#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import re
import pytest
from PageObject.searchpage import SearchPage
from common.readconfig import ini
from utils.logger import Logger

log = Logger('testcase').logger


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        search.get_url(ini.url)

    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
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
    pytest.main(['-v', 'test_search.py'])

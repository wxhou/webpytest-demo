#!/usr/bin/env python3
# coding=utf-8
import sys

sys.path.append('.')
import pytest
from PageObject.zentaopage import ZenTao
from common.readconfig import conf


class TestZenTao:
    @pytest.fixture(scope='class', autouse=True)
    def login(self, drivers):
        login = ZenTao(drivers)
        login.get_url(conf.url)
        login.login('hoou', 'Hoou1993')

    def test_001(self, drivers):
        """添加产品"""
        zentao = ZenTao(drivers)
        zentao.add_product('你好', '123')


if __name__ == '__main__':
    pytest.main(['-v', 'test_zentao.py'])

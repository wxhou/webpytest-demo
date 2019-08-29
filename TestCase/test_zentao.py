#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import pytest
from PageObject.zentaopage import ZenTao


class TestZenTao:

    def test_001(self, drivers):
        """添加产品"""
        zentao = ZenTao(drivers)
        zentao.add_product('你好', '123')

    def test_002(self, drivers):
        """添加BUG"""
        zentao = ZenTao(drivers)
        zentao.add_bug()


if __name__ == '__main__':
    pytest.main(['-vv', 'test_zentao.py'])

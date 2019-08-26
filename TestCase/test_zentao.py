#!/usr/bin/env python3
# coding=utf-8
import pytest
from utils.readconfig import Config
from utils.generated import Generator
from utils.picture_processing import Picture
from utils.data_maintenance import Maintenance
from PageObject.loginpage import ZenTaoLogin
from PageObject.zentaopage import ZenTao

conf = Config()
pic = Picture()
gen = Generator()
mai = Maintenance()


class TestZenTao:
    @pytest.fixture(scope='class', autouse=True)
    def start_url(self, drivers):
        login = ZenTaoLogin(drivers)
        login.get_url(conf.url)
        login = ZenTaoLogin(drivers)
        login.login('hoou', 'Hoou1993')
        yield
        login.quit_login()

    def test_001(self, drivers):
        """添加产品"""
        zentao = ZenTao(drivers)
        zentao.add_product('你好','123')

if __name__ == '__main__':
    pytest.main(['-vv', 'test_zentao.py'])

#!/usr/bin/env python3
# coding=utf-8
import pytest
from utils.readconfig import Config
from utils.generated import Generator
from PageObject.loginpage import FastLogin
from utils.picture_processing import Picture
from utils.data_maintenance import Maintenance

conf = Config()
pic = Picture()
gen = Generator()
mai = Maintenance()


class TestLogin:
    @pytest.fixture(scope='class', autouse=True)
    def start_url(self,drivers):
        login = FastLogin(drivers)
        login.get_url(conf.url)

    def test_001(self, drivers):
        '''测试登录'''
        login = FastLogin(drivers)
        login.login('admin', '123456')
        picture1 = mai.last_screen
        picture2 = login.logo(gen.screen_name)
        if picture1:
            assert pic.ImageContrast(picture1, picture2)


if __name__ == '__main__':
    pytest.main(['-vv', 'test_fast.py'])

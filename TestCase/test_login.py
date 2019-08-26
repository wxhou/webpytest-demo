#!/usr/bin/env python3
# coding=utf-8
import pytest
from utils.readconfig import Config
from utils.generated import Generator
from PageObject.loginpage import LoginPage
from utils.picture_processing import Picture
from utils.data_maintenance import Maintenance

conf = Config()
pic = Picture()
gen = Generator()
mai = Maintenance()


class TestLogin:
    def test_001(self, drivers):
        login = LoginPage(drivers)
        login.login('admin', '123456')
        picture1 = mai.last_screen
        picture2 = login.logo(gen.screen_name)
        assert pic.ImageContrast(picture1, picture2)


if __name__ == '__main__':
    pytest.main(['-vv', 'test_login.py'])

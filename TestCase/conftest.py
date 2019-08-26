#!/usr/bin/env python3
# coding=utf-8
import pytest
from utils.readconfig import Config
from PageObject.loginpage import LoginPage

conf = Config()


@pytest.fixture(scope='function', autouse=True)
def start_url(drivers):
    login = LoginPage(drivers)
    login.get_url(conf.url)

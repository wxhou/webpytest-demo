#!/usr/bin/env python3
# coding=utf-8
import pytest
from PageObject.zentaopage import ZenTao
from utils.readconfig import Config

conf = Config()


@pytest.fixture(scope='class', autouse=True)
def login(drivers):
    login = ZenTao(drivers)
    login.get_url(conf.url)
    login.login('hoou', 'Hoou1993')
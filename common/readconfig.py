#!/usr/bin/env python3
# coding=utf-8
import os, sys

sys.path.append('.')
import configparser

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 如果可以，请不要在root_dir中使用os.getcwd()
config_path = os.path.join(root_dir, 'data', 'config.ini')


class Config:
    """配置文件"""
    BROWSER = 'browser'
    HOST = 'host'
    REMOTE = 'remote'

    def __init__(self):
        self.config = configparser.RawConfigParser()
        # 当有%的符号时请使用Raw读取
        self.config.read(config_path, encoding='utf-8')

    @property
    def browser(self):
        return self.config.get(self.BROWSER.upper(), self.BROWSER.lower()).title()

    @property
    def url(self):
        return self.config.get(self.HOST.upper(), self.HOST.lower())

    @url.setter
    def url(self, value):
        self.config.set(self.HOST.upper(), self.HOST.lower(), value)
        with open(config_path, 'w') as f:
            self.config.write(f)

    @property
    def remote(self):
        return self.config.get(self.REMOTE.upper(), self.REMOTE.lower())

    @remote.setter
    def remote(self, value):
        self.config.set(self.REMOTE.upper(), self.REMOTE.lower(), value)
        with open(config_path, 'w') as f:
            self.config.write(f)


conf = Config()

if __name__ == '__main__':
    conf = Config()
    print(conf.browser)

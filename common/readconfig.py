#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   readconfig.py
@Time    :   2019/09/28 11:52:32
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys

sys.path.append('.')
import settings
import configparser


class Config:
    """配置文件"""
    HOST = 'host'

    def __init__(self):
        self.config_path = settings.CONFIG_PATH
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(self.config_path, encoding='utf-8')

    @property
    def url(self):
        return self.config.get(self.HOST.upper(), self.HOST.lower())

    @url.setter
    def url(self, value):
        self.config.set(self.HOST.upper(), self.HOST.lower(), value)
        with open(self.config_path, 'w') as f:
            self.config.write(f)


conf = Config()

if __name__ == '__main__':
    conf = Config()
    print(conf.url)

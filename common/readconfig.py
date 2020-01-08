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
import configparser
import settings



HOST = 'HOST'


class Config:
    """配置文件"""

    def __init__(self):
        self.config_path = settings.CONFIG_PATH
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(self.config_path, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(self.config_path, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

    @url.setter
    def url(self, value):
        self._set(HOST, HOST, value)


conf = Config()

if __name__ == '__main__':
    conf = Config()
    print(conf.url)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import configparser
import settings

HOST = 'HOST'


class ReadConfig:
    """配置文件"""

    def __init__(self):
        self.config_path = settings.INI_PATH
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


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import configparser

HOST = 'HOST'


class ReadConfig(object):
    """配置文件"""

    def __init__(self, route):
        self.path = os.path.join(route, 'config.ini')
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(self.path, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(self.path, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


if __name__ == '__main__':
    pass

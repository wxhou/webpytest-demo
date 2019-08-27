#!/usr/bin/env python3
# coding=utf-8
import os
import configparser
from pprint import pprint

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 如果可以，请不要在root_dir中使用os.getcwd()
config_path = os.path.join(root_dir, 'config', 'config.ini')
element_path = os.path.join(root_dir, 'config', 'element.ini')


class Config:
    """配置文件"""

    def __init__(self):
        self.config = configparser.ConfigParser()
        # with open(config_path,'r') as f:
        self.config.read(config_path, encoding='utf-8')

    @property
    def url(self):
        return self.config.get('webserver', 'url')

    @url.setter
    def url(self, value):
        self.config.set('server', 'url', value)
        with open(config_path, 'w') as f:
            self.config.write(f)

    @property
    def remote_state(self):
        return self.config.get('remote', 'state')

    @remote_state.setter
    def remote_state(self, value):
        self.config.set('remote', 'state', value)
        with open(config_path, 'w') as f:
            self.config.write(f)

    @property
    def remote_url(self):
        return self.config.get('remote', 'state')

    @remote_url.setter
    def remote_url(self, value):
        self.config.set('remote', 'state', value)
        with open(config_path, 'w') as f:
            self.config.write(f)


class Element:
    """获取元素"""

    def __init__(self):
        self.element = configparser.ConfigParser()
        self.element.read(element_path, encoding='utf-8')

    def __call__(self, *args, **kwargs):
        return self.element.get(*args)

    def __getattr__(self, item):
        sections = self.element.items(item)
        return sections


if __name__ == '__main__':
    conf = Element()
    pprint(conf.zentao)

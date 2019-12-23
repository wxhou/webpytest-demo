#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   readyaml.py
@Time    :   2019/09/28 11:52:25
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys

sys.path.append('.')
import os
import yaml
import settings


class Element:
    """获取元素"""

    def __init__(self, name):
        self.element_path = settings.ELEMENT_PATH(name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        sections = self.data.get(item)
        if sections:
            return sections
        else:
            raise AttributeError("关键字 %s 获取元素结果为空" % item)


if __name__ == '__main__':
    login = Element('login')
    print(login.登录)

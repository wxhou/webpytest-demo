#!/usr/bin/env python3
# coding=utf-8
'''
@project : webpytest-demo
@author  : hoou
@file   : readyaml.py
@time   : 18:14
@Version : 1.0
@Contact : wxhou@yunjinginc.com
'''
import sys

sys.path.append('.')
import os
import yaml

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
element_path = os.path.join(root_dir, 'data', 'element.yaml')


class Element:
    """获取元素"""

    def __init__(self):
        with open(element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f.read())

    def __getattr__(self, item):
        sections = self.data.get(item)
        if sections:
            return sections
        else:
            raise ValueError("关键字 %s 获取元素结果为空" % item)


element = Element()

if __name__ == '__main__':
    print(element.账户)

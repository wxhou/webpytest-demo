#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from config.conf import LOCATE_MODE


class Element:
    """获取元素"""

    def __init__(self, route, name):
        self.path = os.path.join(route, '%s.yaml' % name)
        if not os.path.exists(self.path):
            raise FileNotFoundError("%s 文件不存在！" % self.path)
        with open(self.path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        return self.data[item]


def getElement(locator, number=None):
    """获取元素"""
    pattern, value = locator.split("==")
    element_value = value % number if number else value
    return LOCATE_MODE[pattern], element_value


if __name__ == '__main__':
    pass

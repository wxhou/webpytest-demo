#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   readelement.py
@Time    :   2020-01-08 19:07:32
@Author  :   wxhou 
@Version :   1.0
@Contact :   1084502012@qq.com
'''
import sys
sys.path.append('.')
import os
import yaml
import settings
from common.image import get_file_name


class Element:
    """获取元素"""
    def __init__(self, name):
        self.element_path = os.path.join(settings.ELEMENT_PATH,
                                         '%s.yaml' % name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        sections = self.data.get(item)
        if sections:
            return sections
        else:
            file_name = "%s.yaml" % get_file_name(self.element_path)[0]
            raise AttributeError("文件%s中的关键字 %s 获取元素结果为空" % (file_name, item))


if __name__ == '__main__':
    login = Element('login')
    print(login.登录)

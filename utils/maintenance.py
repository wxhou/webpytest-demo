#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   data_maintenance.py
@Time    :   2019/09/28 11:55:42
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import os
from utils.produce import produce

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Maintenance:
    """数据维护"""

    def __init__(self):
        self.screen = os.path.join(root_dir, 'screenshot')
        if not os.path.exists(self.screen):
            os.mkdir(self.screen)

    def last(self, path):
        data = os.listdir(path)
        if data:
            data.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
            return data[-1]

    @property
    def last_screen(self):
        """返回最后一个截图路径"""
        if self.last(self.screen):
            last_piture = os.path.join(self.screen, self.last(self.screen))
            return last_piture
        
    def __del__(self):
        for filename in os.listdir(self.screen):
            file = os.path.join(self.screen, filename)
            if os.path.getmtime(file) < produce.time_line:
                os.remove(file)
                print("删除文件%s成功！" % file)


if __name__ == '__main__':
    m = Maintenance()
    print(m.last_screen)
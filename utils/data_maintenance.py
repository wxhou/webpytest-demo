#!/usr/bin/env python3
# coding=utf-8
import os

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Maintenance:
    def __init__(self):
        self.screen = os.path.join(root_dir, 'screenshot')

    def last(self, path):
        data = os.listdir(path)
        data.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
        return data[-1]

    @property
    def last_screen(self):
        """返回最后一个截图"""
        return os.path.join(self.screen,self.last(self.screen))


if __name__ == '__main__':
    m = Maintenance()
    print(m.last_screen)

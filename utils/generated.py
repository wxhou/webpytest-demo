#!/usr/bin/env python3
# coding=utf-8
import os,sys
sys.path.append('.')
import time
from datetime import datetime
from faker import Factory

faker = Factory().create('zh_CN')
root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Generator:
    """数据生成"""

    @property
    def mobile_number(self):
        '''手机号'''
        return faker.phone_number()

    @property
    def ID_card(self):
        '''身份证'''
        return faker.ssn(min_age=1, max_age=90)

    @property
    def image(self):
        '''图片网址'''
        return faker.image_url()

    @property
    def word(self):
        '''随机单词'''
        return faker.word()

    @property
    def license_plate(self):
        '''车牌号'''
        return faker.license_plate()

    @property
    def address(self):
        ''' 随机地址'''
        return faker.address()

    @property
    def randomdate(self):
        '''随机日期（可自定义格式）'''
        return faker.date(pattern="%Y-%m-%d")

    @property
    def randomtime(self):
        '''随机时间（可自定义格式）'''
        return faker.time(pattern="%H:%M")

    @property
    def name(self):
        '''生成名字'''
        return faker.name()

    @property
    def screen_name(self):
        '''截图名称'''
        screen_name = os.path.join(root_dir, 'screenshot', '%s.png' % self.now_time)
        return screen_name

    @property
    def now_time(self):
        '''现在的时间'''
        return time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

    @property
    def time_line(self):
        '''删除的时间线'''
        return time.time() - 7 * 24 * 3600


if __name__ == '__main__':
    print(Generator().time_line)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
from faker import Faker

faker = Faker('zh_CN')


class Fakers:
    """假数据生成"""

    @property
    def mobile_number(self):
        """手机号"""
        return faker.phone_number()

    @property
    def ID_card(self):
        """身份证"""
        return faker.ssn(min_age=1, max_age=90)

    @property
    def image(self):
        """图片网址"""
        return faker.image_url()

    @property
    def word(self):
        """随机单词"""
        return faker.word()

    @property
    def license_plate(self):
        """车牌号"""
        return faker.license_plate()

    @property
    def address(self):
        """ 随机地址"""
        return faker.address()

    @property
    def randomdate(self):
        """随机日期（可自定义格式）"""
        return faker.date(pattern="%Y-%m-%d")

    @property
    def randomtime(self):
        """随机时间（可自定义格式）"""
        return faker.time(pattern="%H:%M")

    @property
    def name(self):
        """生成名字"""
        return faker.name()


fakers = Fakers()

if __name__ == '__main__':
    print(fakers.name)

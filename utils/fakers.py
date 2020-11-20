#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from faker import Faker


class Fakers(object):
    """假数据生成"""

    def __init__(self):
        super(Fakers, self).__init__()
        self.faker = Faker('zh_CN')

    def __getattr__(self, item):
        handler = getattr(self.faker, item)
        return handler()

    @property
    def mobile_number(self):
        """手机号"""
        return self.faker.phone_number()

    @property
    def ID_card(self):
        """身份证"""
        return self.faker.ssn(min_age=1, max_age=90)

    @property
    def image(self):
        """图片网址"""
        return self.faker.image_url()

    @property
    def word(self):
        """随机单词"""
        return self.faker.word()

    @property
    def license_plate(self):
        """车牌号"""
        return self.faker.license_plate()

    @property
    def address(self):
        """ 随机地址"""
        return self.faker.address()

    @property
    def randomdate(self):
        """随机日期（可自定义格式）"""
        return self.faker.date(pattern="%Y-%m-%d")

    @property
    def randomtime(self):
        """随机时间（可自定义格式）"""
        return self.faker.time(pattern="%H:%M")

    @property
    def name(self):
        """生成名字"""
        return self.faker.name()


fakers = Fakers()

if __name__ == '__main__':
    print(fakers.name)

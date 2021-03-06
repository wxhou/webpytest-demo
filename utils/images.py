#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import math
import operator
from PIL import Image
from functools import reduce
from utils.logger import log
from utils.times import sleep


def get_image_name(string):
    """获取文件名称"""
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    return pattern.findall(string)


def area_screenshot(locator, path):
    """区域截图"""
    log.warning("需要截图的元素坐标%s" % locator.location)
    log.warning("需要截图的元素大小%s" % locator.size)
    shot = (locator.location['x'], locator.location['y'],
            locator.location['x'] + locator.size['width'],
            locator.location['y'] + locator.size['height'])
    im = Image.open(path)
    im = im.crop(shot)
    im.save(path)
    sleep()


def image_contrast(img1, img2, threshold=7):
    """图像对比算法"""
    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add, list(
        map(lambda x, y: (x - y) ** 2, h1, h2))) / len(h1))
    log.info("对比结果为%s" % result)
    return result <= threshold


if __name__ == '__main__':
    b = image_contrast('/Users/hoou/Desktop/4510.png',
                       '/Users/hoou/Desktop/144223.png')
    print(b)

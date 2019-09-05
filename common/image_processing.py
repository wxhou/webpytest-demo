#!/usr/bin/env python3
# coding=utf-8
import sys

sys.path.append('.')
import math
import time
import operator
from PIL import Image
from functools import reduce
from utils.log import log


class Picture:
    """图像处理"""

    def picture_interception(self, locator, path):
        """图像裁剪"""
        log.warning("需要截图的元素坐标%s" % locator.location)
        log.warning("需要截图的元素大小%s" % locator.size)
        shot = (locator.location['x'],
                locator.location['y'],
                locator.location['x'] + locator.size['width'],
                locator.location['y'] + locator.size['height'])
        im = Image.open(path)
        im = im.crop(shot)
        im.save(path)
        time.sleep(1)

    def image_contrast(self, img1, img2):
        """图像对比算法"""
        image1 = Image.open(img1)
        image2 = Image.open(img2)

        h1 = image1.histogram()
        h2 = image2.histogram()

        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        log.info("对比结果为%s" % result)
        return result == 0.0


pic = Picture()

if __name__ == '__main__':
    pass

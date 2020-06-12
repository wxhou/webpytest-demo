#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import os
from PIL import Image
from config import conf
from tools.logger import log
from tools.times import sleep
from airtest_selenium.exceptions import IsNotTemplateError


def area_screenshot(locator, path):
    """元素截图"""
    log.warning("需要截图的元素坐标%s" % locator.location)
    log.warning("需要截图的元素大小%s" % locator.size)
    shot = (locator.location['x'], locator.location['y'],
            locator.location['x'] + locator.size['width'],
            locator.location['y'] + locator.size['height'])
    im = Image.open(path)
    im = im.crop(shot)
    im.save(path)
    sleep()


def get_image_name(string):
    """获取文件名称"""
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    return pattern.findall(string)


def get_airtest_image(name):
    """获取airtest图像"""
    path = os.path.join(conf.AIR_IMAGE, "{}.png".format(name))
    if os.path.exists(path):
        return path
    raise IsNotTemplateError("验证图片不存在：{}".format(path))


if __name__ == '__main__':
    pass

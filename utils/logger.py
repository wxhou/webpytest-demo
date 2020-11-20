#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import logging
import functools
from config.conf import LOG_PATH
from utils.times import datetime_strftime


class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:  # 防止日志重复输出
            self.logger.setLevel(logging.INFO)

            # 创建一个handle写入文件
            fh = logging.FileHandler(self.log_path, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def log_path(self):
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        return os.path.join(LOG_PATH, '{}.log'.format(datetime_strftime()))

    @property
    def fmt(self):
        return '%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] %(message)s'


log = Logger().logger


def logger(func=None, msg=None):
    """日志"""
    if not func:
        return functools.partial(logger, msg=msg)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log.info(func.__name__ + func.__doc__)
        log.info(f"参数：{args[1:]}{kwargs}")
        if msg:
            log.info(msg.format(result))
        return result

    return wrapper


if __name__ == '__main__':
    log.info("你好")

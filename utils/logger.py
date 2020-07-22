#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import logging
from functools import wraps
from config import LOG_PATH
from utils.times import datetime_strftime


class Logger:
    def __init__(self):
        log_path = self.log_path[:self.log_path.rfind('/')]
        if not os.path.exists(log_path):
            os.makedirs(log_path)
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
        return os.path.join(LOG_PATH, '{}.log'.format(datetime_strftime()))

    @property
    def fmt(self):
        return '%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] %(message)s'


log = Logger().logger

if __name__ == '__main__':
    log.info('你好', '12344')

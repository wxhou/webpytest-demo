#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   log.py
@Time    :   2019/09/28 11:57:16
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys

sys.path.append('.')
import os
import logging
from datetime import datetime
import settings


class Log:
    def __init__(self):
        log_path = self.log_path[:self.log_path.rfind('/')]
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

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
        timeline = datetime.now().strftime("%Y%m")
        return os.path.join(settings.LOG_PATH, '{}.log'.format(timeline))

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'


log = Log().logger

if __name__ == '__main__':
    log.info('你好')

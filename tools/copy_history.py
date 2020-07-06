#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import os
import shutil
from config.conf import ALLURE_RESULTS, ALLURE_REPORT


def copy_history():
    start_path = os.path.join(ALLURE_REPORT, 'history')
    end_path = os.path.join(ALLURE_RESULTS, 'history')
    if os.path.exists(end_path):
        shutil.rmtree(end_path)
        print("复制上一运行结果成功！")
    try:
        shutil.copytree(start_path, end_path)
    except FileNotFoundError:
        print("allure没有历史数据可复制！")


if __name__ == "__main__":
    copy_history()

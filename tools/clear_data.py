#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
import os
from tools.times import timestamp, time_strftime
from config.conf import ALLURE_RESULTS, SCREENSHOT_DIR


def clear_screen_capture():
    """清除过期的截图"""
    end_time = timestamp() - 1 * 24 * 3600
    timeline = time_strftime(end_time)  # strftime不支持中文
    print("当前清理过期截图的时间线是：%s" % timeline)
    ver = True
    for i in os.listdir(SCREENSHOT_DIR):
        delete_pic = os.path.join(SCREENSHOT_DIR, i)
        if os.path.isfile(delete_pic):
            start_time = os.path.getmtime(delete_pic)
            if start_time < end_time:
                os.remove(delete_pic)
                print("删除%s完毕！" % delete_pic)
                ver = False
    if ver:
        
        print("当前没有删除任何过期截图！")


def clear_allure_results():
    var = True
    for i in os.listdir(ALLURE_RESULTS):
        new_path = os.path.join(ALLURE_RESULTS, i)
        if os.path.isfile(new_path):
            os.remove(new_path)
            print("删除{}成功！".format(new_path))
            var = False
    if var:
        print("没有allure历史数据可清理！")


if __name__ == '__main__':
    clear_allure_results()
    clear_screen_capture()
#!/usr/bin/env python3
# coding=utf-8
'''
@File    :   runcase.py
@Time    :   2019/09/28 11:50:32
@Author  :   wxhou
@Version :   1.0
@Contact :   wxhou@yunjinginc.com
'''
import sys
sys.path.append('.')
import pytest

if __name__ == '__main__':
    pytest.main(['--html=report.html', '--self-contained-html'])

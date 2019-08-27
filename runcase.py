#!/usr/bin/env python3
# coding=utf-8
import os
import sys
import pytest

print(os.getcwd())
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

fastadmin = os.path.join(os.getcwd(), 'TestCase', 'test_fast.py')
zentao = os.path.join(os.getcwd(), 'TestCase', 'test_zentao.py')


def main(zentao):
    if zentao in 'zentao':
        pytest.main([zentao, '--html=report.html', '--self-contained-html'])
    else:
        pytest.main([fastadmin, '--html=report.html', '--self-contained-html'])


if __name__ == '__main__':
    main('zentao')

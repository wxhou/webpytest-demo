#!/usr/bin/env python3
# coding=utf-8
import os
import sys
import pytest

print(os.getcwd())
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

testcase = os.path.join(os.getcwd(), 'TestCase')

args = r'pytest {} --html=report.html --self-contained-html'.format(testcase)


def main():
    os.system(args)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import os

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


if __name__ == '__main__':
    print(root_dir)

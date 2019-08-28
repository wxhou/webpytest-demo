#!/usr/bin/env python3
# coding=utf-8
import os
import sys
import pytest

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

if __name__ == '__main__':
    pytest.main(['--html=report.html', '--self-contained-html'])

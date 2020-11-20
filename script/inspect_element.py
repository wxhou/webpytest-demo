#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from utils.times import runner_time
from config.conf import element, LOCATE_MODE


@runner_time
def inspect_element():
    """审查所有的元素是否正确"""
    for v in element.values():
        for i in os.listdir(v):
            ele_file = os.path.join(v, i)
            with open(ele_file, encoding='utf-8') as fp:
                data = yaml.safe_load(fp)
            for k in data:
                ele = data[k]
                if "==" in ele:
                    pattern, value = ele.split('==')
                    if pattern not in LOCATE_MODE:
                        raise AttributeError('【%s】路径中【%s]元素没有指定类型'
                                             % (i, k))
                    if pattern == 'xpath':
                        assert '//' in ele, \
                            '【%s】路径中【%s]元素xpath类型与值不配' % (i, k)
                    if pattern == 'css':
                        assert '//' not in ele, \
                            '【%s】路径中【%s]元素css类型与值不配' % (i, k)
                else:
                    raise AttributeError('【%s】路径中【%s]元素没有指定元素分隔符' % (i, k))


if __name__ == '__main__':
    inspect_element()

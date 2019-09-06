#!/usr/bin/env python3
# coding=utf-8

# a = [1, 2, 310, 34, 6, 8, 34234]
#
# for i in range(len(a)):
#     for j in range(len(a) - 1):
#         if a[i] > a[j]:
#             a[i], a[j] = a[i], a[j]
#
#
# print(a)


b = 'ab**cd**e*12'

# class string_handle:
#     def __init__(self, string):
#         self.string = string
#
#     def __len__(self):
#         return self.string.count('*')
#
#     def __str__(self):
#         new_str = ''
#         for i in self.string:
#             if i != '*':
#                 new_str += i
#         return '*' * len(self) + new_str


# hand = string_handle(b)
# print(len(hand))
# print(hand)

a = 'ab**cd**e*12'


def string_handle(string):
    new_str = ''
    str_count = string.count('*')
    for i in string:
        if i != '*':
            new_str += i
    return str_count, '*' * str_count + new_str


bb = "#u1>a[name=tj_login]"
print(bb.split('=='))
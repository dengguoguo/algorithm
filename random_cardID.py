# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 16:26
# @Author  : dengguo
# @File    : random_cardID.py
# @Software: PyCharm
import random

def shuffle(tar_list):
    res_list = []
    while tar_list:
        p = random.randrange(0, len(tar_list))
        res_list.append(str(tar_list[p]))
        tar_list.pop(p)
    result = ''.join(res_list)
    return result
res = shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(res)   #字符串



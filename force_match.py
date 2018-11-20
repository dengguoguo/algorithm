# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 10:16
# @Author  : dengguo
# @File    : force_match.py
# @Software: PyCharm


def force_match(s, p):
    m = len(s); n = len(p)
    for i in range(m-n+1):#起始指针i
        if s[i:i+n] == p:
            return True
    return False

if __name__ == '__main__':
    print(force_match('2131131113','111'))

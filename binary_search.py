# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 10:38
# @Author  : dengguo
# @File    : binary_search.py
# @Software: PyCharm
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。但是，
# 折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
def binary_search(target, num):
    low = 0
    high = len(target) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = target[mid]
        if guess == num:
            return mid
        elif guess > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    result = binary_search(test_list, 15)
    print(result)

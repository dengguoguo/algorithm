#!/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 18-11-17 下午4:56
# @Author  : dengguo
# @File    : quick_sort.py
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    testRes = quicksort([5, 11, 3, 5, 8, 2, 6, 7,5000,4, 326,200])
    print(testRes)

#!/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 18-11-17 下午5:40
# @Author  : dengguo
# @File    : lru.py
import collections


# 基于OrderedDict实现
class LRUCache(collections.OrderedDict):
    """
       function:利用collection.OrderedDict数据类型实现最近最少使用算法
                OrderedDict有个特殊方法popitem(Last=False)时则实现队列，弹出最先插入的元素，
                而当Last=True则实现堆栈方法，弹出的是最近插入的那个元素
                实现了两个方法：get(key）取出键中对应的值，若没有返回None
                 set(key, value) 根据LRU特性添加元素
    """

    def __init__(self, *args, **kwargs):
        super(LRUCache, self).__init__(*args, **kwargs)
        self.capacity = args
        self.queue = collections.OrderedDict()

    def get(self, key):
        if key not in self.queue:
            return -1
        value = self.queue.pop(key)
        self.queue[key] = value
        return self.queue[key]

    def put(self, key, value):
        if key in self.queue:
            self.queue.pop(key)

        elif len(self.queue.items()) == self.capacity:
            self.queue.popitem(last=False)
            self.queue[key] = value

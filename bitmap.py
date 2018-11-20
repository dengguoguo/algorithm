# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 10:24
# @Author  : dengguo
# @File    : bitmap.py
# @Software: PyCharm

# 初始化bitmap
class Bitmap(object):
    def __init__(self, max):
        self.size = int((max + 31 - 1) / 31)  # 向上取整


if __name__ == '__main__':
    bitmap = Bitmap(90)
    print('需要 %d 个元素。' % bitmap.size)


# 计算在数组中的索引
class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return num / 31


if __name__ == '__main__':
    bitmap = Bitmap(90)
    print('数组需要 %d 个元素。' % bitmap.size)
    print('47 应存储在第 %d 个数组元素上。' % bitmap.calcElemIndex(47))


# 计算在数组中的位索引
class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return num / 31

    def calcBitIndex(self, num):
        return num % 31


if __name__ == '__main__':
    bitmap = Bitmap(90)
    print('数组需要 %d 个元素。' % bitmap.size)
    print('47 应存储在第 %d 个数组元素上。' % bitmap.calcElemIndex(47))
    print('47 应存储在第 %d 个数组元素的第 %d 位上。' % (bitmap.calcElemIndex(47), bitmap.calcBitIndex(47),))


# 置1操作
class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return int(num / 31)

    def calcBitIndex(self, num):
        return int(num % 31)

    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)


if __name__ == '__main__':
    bitmap = Bitmap(90)
    bitmap.set(0)
    print(bitmap.array)


# 清0操作
class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return int(num / 31)

    def calcBitIndex(self, num):
        return int(num % 31)

    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << byteIndex))


if __name__ == '__main__':
    bitmap = Bitmap(87)
    bitmap.set(0)
    bitmap.set(34)
    print(bitmap.array)
    bitmap.clean(0)
    print(bitmap.array)
    bitmap.clean(34)
    print(bitmap.array)


# 测试某位是否为1
class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return int(num / 31)

    def calcBitIndex(self, num):
        return int(num % 31)

    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << byteIndex))

    def test(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False


if __name__ == '__main__':
    bitmap = Bitmap(90)
    bitmap.set(0)
    print(bitmap.array)
    print(bitmap.test(0))
    bitmap.set(1)
    print(bitmap.test(1))
    print(bitmap.test(2))
    bitmap.clean(1)
    print(bitmap.test(1))


# 不重复数组得排序
class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return int(num / 31)

    def calcBitIndex(self, num):
        return int(num % 31)

    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << byteIndex))

    def test(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False


if __name__ == '__main__':
    MAX = 879
    suffle_array = [45, 2, 78, 35, 67, 90, 879, 0, 340, 123, 46]
    result = []
    bitmap = Bitmap(MAX)
    for num in suffle_array:
        bitmap.set(num)
    for i in range(MAX + 1):
        if bitmap.test(i):
            result.append(i)
    print('原始数组为:    %s' % suffle_array)
    print('排序后的数组为: %s' % result)

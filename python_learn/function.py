# -*- coding: utf-8 -*

import numpy as np
import re
from fnmatch import fnmatch, fnmatchcase

'''
#仅仅查看b是否有值传进来
_no_value_ = object()
def spam(a, b=_no_value_):
    if b is _no_value_:
        print("no")

spam(1)
'''
'''
是完全通配的意思，\s是指空白，包括空格、换行、tab缩进等所有的空白，而\S刚好相反,这样一正一反下来，就表示所有的字符，完全的，一字不漏的。
另外，[]这个符号，表示在它里面包含的单个字符不限顺序的出现，比如下面的正则：
[ace]*这表示，只要出现a/c/e这三个任意的字母，都会被匹配
'''
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

# addresses = [
#     '5412 N CLARK ST',
#     '1060 W ADDISON ST',
#     '1039 W GRANVILLE AVE',
#     '2122 N CLARK ST',
#     '4802 N BROADWAY',
# ]
#
# print([addr for addr in addresses if fnmatchcase(addr, "*ST")])

# names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
# print(sorted(names, key = lambda name:name.split()[-1].lower()))
# print(sorted(names, key = lambda name:name.split()[-1]))
# print(names.sort(key = lambda x:x.split()[-1]))

# funcs = [lambda x, n=n: x+n for n in range(5)]
# for f in funcs:
#     print(f(0))

# class Pair:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# def __repr__(self):
#     return 'Pair({0.x!r}, {0.y!r})'.format(self)
# def __str__(self):
#     return '({0.x!s}, {0.y!s})'.format(self)
#
# p = Pair(3, 4)
# print(p)

'''
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def SetNewAge(self, newage):
        if newage > 0 and newage <= 100:
            self.__age = newage

    def getage(self):
        return self.__age

    def __test(self):
        print("私有函数")

    def test2(self):
        self.__test()
        print("调用定义的私有函数")

    def printage(self):
        print(self.__age)

zhangsan = Person("zhangsan", 30)
# zhangsan.age = 31
# zhangsan.printage()

zhangsan.SetNewAge(31)
# print(zhangsan.printage())
age = zhangsan.getage()
print(age)
'''


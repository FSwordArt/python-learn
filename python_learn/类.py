# -*- coding: utf-8 -*

import numpy as np

class Test():

    num = 0

    def __init__(self, age):
        self.age = age

    def setage(self, n_num):
        self.age = n_num

    def getage(self):
        return self.age

    @classmethod
    def setNum(cls, NewNum):
        cls.num = NewNum

    @staticmethod
    def printTest():
        print("验证")

a = Test(1)
print(a.num)

#要用类名修改值
Test.setNum(100)
print(a.num)

#super可以直接获取当前类的父类，不需要传递self
super().__init__(属性名)



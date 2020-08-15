from collections.abc import Iterable
from collections.abc import Iterator
import time

class Classmate(object):

    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        #要实现for功能，必须实现__iter__功能，函数必须返回一个迭代器的对象
        return classmateiterator(self)

class classmateiterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.index = 0

    #只要类中有下面两个方法，就称这个类为迭代器
    def __iter__(self):
        pass

    def __next__(self):

        if self.index < len(self.obj.names):
            set = self.obj.names[self.index]
            self.index += 1
            return set

        else:
            raise StopIteration

classmate = Classmate()
classmate.add("11")
classmate.add("22")
classmate.add("33")

print("是否为迭代对象：", isinstance(classmate, Iterable))
classmate_iterator = iter(classmate)
print("判断是否为迭代器：", isinstance(classmate_iterator, Iterator))

for name in classmate:
    print(name)
    time.sleep(1)





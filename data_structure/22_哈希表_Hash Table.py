# -*- coding: utf-8 -*
'''
哈希表由一个直接寻址表和一个哈希函数组成
解决哈希冲突：
    1.开放寻址法：如果哈希函数返回的位置已经有值，则可向后探查新的位置来存储这个值
    2.线性探查：如果位置i被占用，则探查i+1, i+2
    3.二次探查：如果位置i被占用，则探查i+1**2, i-1**2, i+2**2, i-2**2
    4.二度哈希：有n个哈希函数，当使用第1个哈希函数h1发生冲突时，使用第二个，第三个

时间复杂度：O(kn) k:while循环的次数，也是最大数的位数
空间复杂度O(k+n)
'''

class LinkList(object):

    class Node(object):

        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator(object):

        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):

        self.head = None
        self.tail = None #尾结点
        if iterable:
            self.extend(iterable)

    def append(self, obj):

        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s #尾结点
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, item):
        for n in self:
            if n == item:
                return True
            else:
                return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+", ".join(map(str, self)) + ">>"

class HashTable:

    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for _ in range(self.size)]

    #创建哈希函数
    def h(self, k):
        return k % self.size

    def insert(self, item):
        i = self.h(item)
        if self.find(item):
            print("Duplicate Insert")
        else:
            self.T[i].append(item)

    def find(self, item):
        i = self.h(item)
        return self.T[i].find(item)

ht = HashTable()
ht.insert(0)















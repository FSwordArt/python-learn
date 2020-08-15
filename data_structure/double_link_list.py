#coding = utf-8
from single_link_list import *
'''双向链表'''

class Node(object):
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None

class DoubleLinkList(object):
    # def __init__(self):
    #     super(DoubleLinkList, self).__init__()
    #     SingleLinkList.__init__(self)
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素, 头插法"""
        node = Node(item)
        node.next = self.__head
        # self.__head = node
        # node.next.prev = node
        #也可以
        self.__head.prev = node
        self.__head = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = Node(item)
        count = 0
        cur = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            while count < (pos-1) and cur != None:
                cur = cur.next
                count += 1
            #当循环退出后，pre指向count-1位置
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node
            '''也可以
            while count < pos:
                cur = cur.next
                count += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            '''

    def remove(self, item):
        """删除结点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #判断是不是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    #判断链表是否只有一个结点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找结点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.insert(-1, 9)
    dll.travel()
    dll.insert(3, 100)
    dll.travel()
    dll.insert(10, 200)
    dll.travel()
    dll.remove(100)
    dll.travel()
    dll.remove(9)
    dll.travel()
#coding = utf-8
'''单向链表'''

class Node(object):
    """结点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
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

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = Node(item)
        count = 0
        pre = self.__head

        if pos <= 0:
            self.add(item)

        elif pos > (self.length()-1):
            self.append(item)

        else:
            while count < (pos-1) and pre != None:
                pre = pre.next
                count += 1
            #当循环退出后，pre指向count-1位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除结点"""
        pre = None
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #判断是不是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(1)
    print(sll.is_empty())
    print(sll.length())

    sll.append(2)
    sll.add(8)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.insert(-1, 9)
    sll.travel()
    sll.insert(3, 100)
    sll.travel()
    sll.insert(10, 200)
    sll.travel()
    sll.remove(100)
    sll.travel()
    sll.remove(9)
    sll.travel()
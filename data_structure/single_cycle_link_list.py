#coding = utf-8
'''单向循环链表'''

class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None

class SingleCycleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self.__head
            while cur.next != self.__head:
                count += 1
                cur = cur.next

        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return print("have no ele")
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem, end=" ")
                cur = cur.next
            #退出循环时，cur指向尾结点，打印最后一个结点的值
            print(cur.elem)

    def add(self, item):
        """链表头部添加元素, 头插法"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            #退出循环时，cur指向尾结点
            node.next = self.__head
            self.__head = node
            #cur.next = node
            cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            # cur.next = self.__head
            # cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = Node(item)
        count = 0
        pre = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            while count < (pos - 1) and pre != None:
                pre = pre.next
                count += 1
            # 当循环退出后，pre指向count-1位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除结点"""
        if self.is_empty():
            return
        else:
            pre = None
            cur = self.__head
            while cur.next != self.__head:
                if cur.elem == item:
                    # 判断是不是头节点
                    if cur == self.__head:
                        #头结点
                        #找尾结点
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                    else:
                        #中间结点
                        pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # 退出循环时，cur指向最后一个结点
            if cur.elem == item:
                if cur == self.__head:
                    #只有一个结点
                    self.__head = None
                else:
                    pre.next = cur.next

    def search(self, item):
        """查找结点是否存在"""
        cur = self.__head
        if self.is_empty():
            return False
        else:
            while cur.next != self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            #退出循环时，cur指向最后一个结点
            if cur.elem == item:
                return True
            return False

if __name__ == "__main__":
    sll = SingleCycleLinkList()
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



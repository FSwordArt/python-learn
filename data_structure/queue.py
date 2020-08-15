#coding=utf-8

class Queue(object):
    def __init__(self):
        self.__item = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__item.append(item)#尾部加  O(1)
        #self.__item.insert(0, item)#O(n)

    def dequeue(self):
        """从队列头部删除一个元素"""
        self.__item.pop(0)#头部弹， O(n)
        #self.__item.pop()#尾部弹 O(1)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__item ==[]

    def size(self):
        """返回队列的大小"""
        return len(self.__item)

if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

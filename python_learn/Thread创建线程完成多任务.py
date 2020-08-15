# -*- coding: utf-8 -*
'''
创建多线程
'''
import numpy as np
import threading
import time

def test1():   #子线程
    for i in range(5):
        print("-----%d-----" % i)
        time.sleep(1)

def test2():
    for i in range(10):
        print("-----%d-----" % i)
        time.sleep(1)

if __name__ == "__main__":

    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start() #启动线程，让线程开始运作，主线程
    t2.start()

    while True:
        print(threading.enumerate())

        if(len(threading.enumerate()) <= 1):
            break
        time.sleep(1)

# class A(object):
#     def a(self):
#         print("-----a-----")
#
# class B(A):
#     def b(self):
#          print("-----b-----")
#
# c = B()
# c.a()


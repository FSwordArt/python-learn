import time
from greenlet import greenlet

# def test1():
#
#     while True:
#         print("-----1-----")
#         time.sleep(0.1)
#         yield
#
# def test2():
#
#     while True:
#         print("-----2-----")
#         time.sleep(0.1)
#         yield
#
# def main():
#
#     t1 = test1()
#     t2 = test2()
#
#     while True:
#         next(t1)
#         next(t2)

def task_1():
    while True:
        print("--1--")
        gr2.switch()
        time.sleep(0.1)

def task_2():
    while True:
        print("--2--")
        gr1.switch()
        time.sleep(0.1)


gr1 = greenlet(task_1)
gr2 = greenlet(task_2)

gr1.switch()



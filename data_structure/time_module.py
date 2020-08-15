#coding=utf-8

#timeit 模块
#class timeit.Timer(stmt = 'pass', setup = 'pass', timer = <timer function>)
from timeit import Timer

def t1():
    list1 = list(range(10000))

def t2():
    list2 = [i for i in range(10000)]#列表生成器

def t3():
    list3 = []
    for i in range(10000):
        list3.append(i)

def t4():
    list4 = []
    for i in range(10000):
        list4 += [i]    #列表相加

def t5():
    list5 = []
    for i in range(10000):
        list5.extend([i])

def t6():
    list6 = []
    for i in range(10000):
        list6.insert(0, i)#往头部添加新的元素

def t7():
    list7 = []
    #
    for i in range(10000):

        list7.insert(-1, i)#往尾部添加新的元素

timer1 = Timer("t1()", "from __main__ import t1")
print("list(range):", timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("[i for i in range]:", timer2.timeit(1000))

timer3 = Timer("t4()", "from __main__ import t4")
print("+:", timer3.timeit(1000))

timer4 = Timer("t5()", "from __main__ import t5")
print("extend:", timer4.timeit(1000))

timer5 = Timer("t3()", "from __main__ import t3")
print("list.append:", timer5.timeit(1000))

timer6 = Timer("t6()", "from __main__ import t6")
print("list.insert(0):", timer6.timeit(1000))

timer7 = Timer("t7()", "from __main__ import t7")
print("list.insert(-1):", timer7.timeit(1000))

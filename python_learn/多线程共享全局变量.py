# -*- coding: utf-8 -*

import threading
import time

'''
对全局变量进行修改时，是否运用global进行说明，要看是否对全局变量的指向发生了变化
变化加
'''

# num = 100
# num1 = [11, 22]
# num2 = [1]
#
# def test1():
#     global num
#     num += 100
#
# def test2():
#     num1.append(33)
#
# def test3():
#     global num2
#     num2 += [100,200]
#
# print(num)
# print(num1)
# print(num2)
# test1()
# test2()
# test3()
# print(num)
# print(num1)
# print(num2)



def test1(tmp):
    tmp.append(33)
    print("------in test1 tmp=%s------" % str(tmp))

def test2(tmp):
    print("------in test2 tmp=%s------" % str(tmp))

tmp = [100, 200]
def main():
    #args指定在调用函数时，传什么参数进去
    t1 = threading.Thread(target=test1, args=(tmp, ))
    t2 = threading.Thread(target=test2, args=(tmp, ))

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("------in main tmp=%s------" % tmp)

if __name__ == "__main__":
    main()
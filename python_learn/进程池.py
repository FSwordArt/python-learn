# -*- coding:utf-8 -*
'''
任务数不确定，用进程池来创建进程
multiprocessing 可以等子进程全部结束，主进程才结束，Pool创建的进程池等到代码结束后会自动结束主进程，而此时子进程不一定结束
通过调用multiprocessing 中的 Pool()函数来实现
Pool().apply_async(要调用的目标, (传递给目标的参数元组, ))
Pool.close()关闭进程池
Pool.join()等到子进程全部完成后程序才往下进行，一定要放在Pool.close()之后
'''

import os
import time
import random
import threading
import multiprocessing
from multiprocessing import Pool

def worker(msg):

    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))

    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))

def main():

    po = Pool(3)

    for i in range(10):
        po.apply_async(worker, (i, ))

    print("-----start-----")
    po.close()
    po.join()
    print("------finish-----")

if __name__ == '__main__':

    main()





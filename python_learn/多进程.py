# -*- coding:utf-8 -*

import time
import multiprocessing
import os
def test1():
    current_process = multiprocessing.current_process()
    test1_id = os.getpid()
    print("test1_id:", test1_id)
    test1_parent_id = os.getppid()
    print("test1_parent_id", test1_parent_id)
    print("test1:", current_process)
    for i in range(3):
        print("-----test1-----")
        time.sleep(1)

def test2():
    current_process = multiprocessing.current_process()
    print("test2:", current_process)
    test2_id = os.getpid()
    print("test2_id:", test2_id)
    test1_parent_id = os.getppid()
    print("test1_parent_id", test1_parent_id)
    for i in range(3):
        print("-----test2-----")
        time.sleep(1)

def main():

    # t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)
    #
    # t1.start()
    # t2.start()

    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    main_id = os.getpid()
    print("main_id:", main_id)
    # p1.daemon = True#主进程退出，子进程销毁
    # p2.daemon = True

    p1.start()
    #p1.join()#主进程等待p1结束后，再进行p2的执行
    p2.start()

if __name__ == "__main__":
    main()






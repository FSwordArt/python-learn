import threading
import time
'''
创建锁
mutex = threading.Lock()
上锁
mutex.acquire()
解锁
mutex.release()
'''
num = 0
mutex = threading.Lock()

def test1(tmp):
    global num
    mutex.acquire()
    for i in range(tmp):
        num += 1
    mutex.release()
    print("-----in test1 num=%d-----" % num)

def test2(tmp):
    global num
    for i in range(tmp):
        mutex.acquire()
        num += 1
        mutex.release()
    print("-----in test2 num=%d-----" % num)

def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()
    print(threading.enumerate())

    time.sleep(2)
    print("-----test2 num=%d-----" % num)

if __name__ == "__main__":
    main()
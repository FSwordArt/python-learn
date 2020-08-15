import time
import threading

class MyThread(threading.Thread):
    def run(self): #必须定义run
        for i in range(5):
            print(i, end = " ")

if __name__ == "__main__":
    t = MyThread()
    t.start()
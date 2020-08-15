# -*- coding:utf-8 -*
'''
Queue只能实现同一个电脑上的数据共享
'''

import multiprocessing

def download_from_web(q):

    data = [11, 22, 33]
    for temp in data:
        q.put(temp)

    print("已经加载好数据")

def analysis_data(q):
    
    ana_data = list()

    while True:
        data = q.get()
        ana_data.append(data)

        if q.empty():
            break

    print(ana_data)

def main():

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=download_from_web, args = (q, ))
    p2 = multiprocessing.Process(target=analysis_data, args = (q, ))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()









































# -*- coding: utf-8 -*

import random

def sift(alist, low, high):

    i = low
    j = 2*i + 1
    temp = alist[low]

    while j <= high:
        if j+1 <= high and alist[j] > alist[j+1]:
            j = j + 1

        if temp > alist[j]:
            alist[i] = alist[j]
            i = j
            j = 2*j + 1

        else:
            alist[i] = temp
            break
    else:
        alist[i] = temp

def topk(alist, k):

    #1.建堆
    heap = alist[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)

    #2.遍历k到最后，找到其中的最大值
    for i in range(k, len(alist)-1):
        if alist[i] > heap[0]:
            heap[0] = alist[i]
            sift(heap, 0, k-1)

    #3.出数
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)

    return heap

if __name__ == '__main__':

    list = [i for i in range(100)]
    random.shuffle(list)
    print(list)

    print(topk(list, 3))

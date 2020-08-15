# -*- coding: utf-8 -*
'''
堆排序过程：
1.建立堆
2.得到堆顶元素，为最大元素
3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
4.堆顶元素为第二大元素
5。重复步骤3，直到堆变空
'''

import random
import heapq #内置堆排序
def sift(alist, low, high):
    '''
    建堆,这是个调整过程，已经保证有大根堆
    heap_sort
    :param alist:列表
    :param low:堆的根节点位置
    :param high:堆的最后一个元素的位置
    lchild : 2i+1
    rchild ：2i+2
    时间复杂度：nlog(n)
    '''

    i = low #i指向最开始的根节点
    j = 2*i + 1 #j起始是左孩子
    temp = alist[low]#把堆顶存起来

    while j <= high:
        #如果有右孩子，且大于左孩子，指向右孩子
        if j+1 <= high and alist[j] < alist[j+1]:
            j += 1
        #下一层比根节点大，将下一层赋给根节点，i下移寻找下一级的孩子
        if alist[j] > temp:
            alist[i] = alist[j]
            i = j
            j = 2*j + 1

        else:
            alist[i] = temp #调整过程
            break
    else:
        alist[i] = temp


def heap_sort(alist):

    n = len(alist)

    #根据孩子找节点 root = (child - 1) // 2
    for i in range((n-2)//2, -1, -1):
        #i表示建堆的时候调整的部分的根的下标
        sift(alist, i, n-1)
        #完成建堆操作

    for i in range(n-1, -1, -1):
        #i始终指向堆的最后一个位置
        alist[0], alist[i] = alist[i], alist[0]
        sift(alist, 0, i-1) #i-1是新的high

if __name__ == '__main__':

    list = [i for i in range(100)]
    random.shuffle(list)
    print(list)

    #手写大根堆
    heap_sort(list)
    print(list)

    # #内置函数小分堆
    # heapq.heapify(list)
    #
    # for i in range(len(list)):
    #     print(heapq.heappop(list), end=',')





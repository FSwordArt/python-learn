# -*- coding: utf-8 -*

'''
希尔排序是插入排序的一个特例
最优时间复杂度：O(n**1.3)
最坏时间复杂度:O(n**2)
不稳定
'''

def shell_sort(alist):
    n = len(alist)
    gap = n // 2  #gap可以随便调，会有不同的时间复杂度
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2 #缩短gap步长

if __name__ == '__main__':
    list = [11, 22, 66, 44, 33, 77, 55]
    print(list)
    shell_sort(list)
    print(list)









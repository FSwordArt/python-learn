# -*- coding: utf-8 -*

'''
最优时间复杂度：O(n**2)
最坏时间复杂度:O(n**2)
不稳定
'''

def select_sort_min2max(alist):

    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

def select_sort_max2min(alist):

    n = len(alist)
    for j in range(n-1):
        max_index = j
        for i in range(j+1, n):
            if alist[max_index] < alist[i]:
                max_index = i
        alist[j], alist[max_index] = alist[max_index], alist[j]


if __name__ == '__main__':

    list = [11,22,66,44,33,77,55]
    print(list)
    # select_sort_min2max(list)
    select_sort_max2min(list)
    print(list)



# -*- coding: utf-8 -*
'''
最优时间复杂度：O(n)
最坏时间复杂度:O(n**2)
稳定
'''
def bubble_sort_min2max(alist):

    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n-j-1):

            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1

        if count == 0: #O(n)
            break

def bubble_sort_max2min(alist):

    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n-j-1):

            if alist[i] < alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1

        if count == 0: #O(n)
            break

if __name__ == '__main__':
    list = [11,22,33,55,77,66,22]
    print(list)
    # bubble_sort_min2max(list)
    bubble_sort_max2min(list)
    print(list)

'''
从后往前取，上面从前往后取
for j in range(n-1, 0, -1):
    for i in range(j):
'''








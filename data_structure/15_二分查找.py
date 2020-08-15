# -*- coding: utf-8 -*

'''
binary_search
必须是个顺序表,二分查找也叫作折半查找
最优时间复杂度：O(1)
最坏时间复杂度:O(logn)
不稳定
'''

def binary_sort_1(alist, item):
    '''递归版本'''
    n = len(alist)
    if n > 0:
        mid = n // 2

        if alist[mid] == item:
            return mid
        elif item < alist[mid]:
            return binary_sort_1(alist[:mid], item)
        else:
            return binary_sort_1(alist[mid+1:], item)

    else:
        return False

def binary_sort_1_plus(alist, item, start=None, end=None):
    '''递归版本,找位置'''
    start = start if start else 0
    end = end if end is not None else len(alist)-1

    mid = (end + start) // 2

    if start > end:
        return False

    elif alist[mid] == item:
        return mid

    elif item < alist[mid]:
        return binary_sort_1_plus(alist, item, start, mid-1)

    else:
        return binary_sort_1_plus(alist, item, mid+1, end)




def binary_sort_2(alist, item):
    '''非递归版本'''
    n = len(alist)

    first = 0
    last = n-1

    while first <= last:

        mid = (first+last) // 2

        if alist[mid] == item:
            return mid

        elif item < alist[mid]:
            last = mid -1

        else:
            first = mid + 1

    return False

if __name__ == '__main__':

    list = [17, 20, 26, 61, 44, 54, 55, 77, 93]
    print(binary_sort_1(list, 55))
    print(binary_sort_1(list, 100))

    print(binary_sort_1_plus(list, 55))
    print(binary_sort_1_plus(list, 100))

    print(binary_sort_2(list, 55))
    print(binary_sort_2(list, 100))
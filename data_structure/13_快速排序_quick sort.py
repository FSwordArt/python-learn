# -*- coding: utf-8 -*

'''
快速排序面试必须掌握！！！！！
最优时间复杂度：O(nlogn)
最坏时间复杂度:O(n**2)
不稳定
'''

def quick_sort(alist, first, last):

    if first >= last:
        return

    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)

if __name__ == '__main__':

    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list)

    quick_sort(list, 0, len(list)-1)
    print(list)













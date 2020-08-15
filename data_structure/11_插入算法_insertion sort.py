# -*- coding: utf-8 -*

'''
最优时间复杂度：O(n)
最坏时间复杂度:O(n**2)
稳定
'''
def insertion_sort(alist):

    n = len(alist)
    for j in range(1, n):

        i = j
        #执行从右边的无序序列中取出一个元素，即i的位置，然后将其插入到前面的正确位置中

        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            # i -= 1 O(n)
            else:
                break

# for i in range(i, 0, -1):
#     if alist[i] < alist[i-1]:
#         alist[i], alist[i - 1] = alist[i-1], alist[i]

if __name__ == '__main__':
    list = [11, 22, 66, 44, 33, 77, 55]
    print(list)
    insertion_sort(list)
    print(list)

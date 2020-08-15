# -*- coding: utf-8 -*
import random

'''
平均时间复杂度：O(n+k)
最坏时间复杂度：O(n2k)
空间复杂度O(nk)
'''

def bucket_sort(alist, n=10):
    '''
    @param n:桶的个数
    @param max_num:最大的元素
    '''
    max_num = max(alist)
    buckets = [[] for _ in range(n)]

    for value in alist:
        #将list列表中的元素放到对应的桶中
        i = min(value // (max_num//n), n-1)
        buckets[i].append(value)

        for j in range(len(buckets[i])-1, 0, -1):

            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]

            else:
                break

    sort_list = []

    for buc in buckets:
        sort_list.extend(buc)

    return sort_list

if __name__ == '__main__':
    list = [random.randint(0, 100) for _ in range(1000)]
    print(list)

    list = bucket_sort(list)
    print(list)






# -*- coding: utf-8 -*
'''
时间复杂度：O(kn) k:while循环的次数，也是最大数的位数
空间复杂度O(k+n)
'''

import random

def radix_sort(alist):

    max_num = max(alist)
    it = 0
    sort_list = alist

    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]

        for value in sort_list:
            digit = (value // (10**it)) % 10
            buckets[digit].append(value)

        sort_list = []
        for buc in buckets:
            sort_list.extend(buc)

        it += 1

    return sort_list






if __name__ == '__main__':
    list = list(range(1000))
    random.shuffle(list)

    print(radix_sort(list))







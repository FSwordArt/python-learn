# -*- coding: utf-8 -*
import random

def count_sort(alist, max_count):

    count = [0 for _ in range(max_count+1)]
    for value in alist:
        count[value] += 1

    alist.clear()

    for index, value in enumerate(count):
        for i in range(value):
            alist.append(index)

    return alist

if __name__ == '__main__':
    list = [random.randint(0, 100) for _ in range(1000)]
    print(list)
    count_sort(list, 100)
    print(list)

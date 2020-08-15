# -*- coding: utf-8 -*

from functools import cmp_to_key

'''
分数背包
'''
def fractional_backage(goods, w):#w总的重量
    m = [0 for _ in range(len(goods))]
    total_prize = 0
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
            total_prize += prize
        else:
            m[i] = w / weight
            total_prize += m[i] * prize
            w = 0
            break
    return total_prize, m

'''
数字拼接
'''
def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_join(alist):

    li = list(map(str, alist))
    li.sort(key=cmp_to_key(xy_cmp))

    return "".join(li)

'''
活动选择问题
'''
def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:
            res.append(a[i])

    return res

if __name__ == '__main__':
    '''1'''
    # goods = [(60, 10), (120, 30), (100, 20)]
    # goods.sort(key=lambda x: x[0] / x[1], reverse=True)
    # print(fractional_backage(goods, 50))

    '''2'''
    # alist = [32, 94, 128, 1286, 6, 71]
    # print(number_join(alist))

    '''3'''
    activities = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
    #活动是按照最早结束时间排好序
    activities.sort(key=lambda x:x[1])
    print(activity_selection(activities))



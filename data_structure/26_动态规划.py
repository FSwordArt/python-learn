# -*- coding:utf-8 -*

# def fabonacci(n):
#
#     if n <= 1:
#         return (n, 0)
#     else:
#         (a, b) = fabonacci(n-1)
#         return (a+b, a)
#
# def fabonacci_no_rec(n):
#
#     f = [0,1,1]
#     if n >=2:
#         for i in range(n-2):
#             num = f[-1] + f[-2]
#             f.append(num)
#     return f[n]
#
#
# import time
#
# '''时间装饰器'''
# def cal_time(func):
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = func(*args, **kwargs)
#         t2 = time.time()
#         print("%s running time: %s secs." % (func.__name__, t2-t1))
#         return result
#     return wrapper
#
# '''------------------------------------------------------------------------------------------------------------------'''
# '''钢条切割问题'''
#
# def cut_rod_rec_1(p, n):
#     '''自顶向下实现递归，时间复杂度O(2**n)'''
#     if n == 0:
#         return 0
#     else:
#         res = p[n]
#         for i in range(1, n):
#             res = max(res, cut_rod_rec_1(p, i) + cut_rod_rec_1(p, n-i))
#
#         return res
#
# @cal_time
# def c1(p, n):
#     return cut_rod_rec_1(p, n)
#
# def cut_rod_rec_2(p, n):
#
#     if n == 0:
#         return 0
#     else:
#         res = 0
#         for i in range(1, n+1):
#             res = max(res, p[i] + cut_rod_rec_2(p, n-i))
#
#         return res
#
# @cal_time
# def c2(p, n):
#     return cut_rod_rec_2(p, n)
#
# @cal_time
# def cut_rod_db(p, n):
#     '''
#     自底向上实现
#     时间复杂度O(n**2)
#     '''
#     r = [0]
#     for i in range(1, n+1):
#         res = 0
#         for j in range(1, i+1):
#             res = max(res, p[j] + r[i-j])
#         r.append(res)
#
#     return r[n]
#
# def cut_rod_extend(p, n):
#
#     r = [0]
#     s = [0]
#     for i in range(1, n+1):
#         res_r = 0
#         res_s = 0
#         for j in range(1, i+1):
#             if p[j] + r[i-j] > res_r:
#                 res_r = p[j] + r[i-j]
#                 res_s = j
#
#         r.append(res_r)
#         s.append(res_s)
#
#     return r[n], s
#
# def cut_rod_solution(p, n):
#
#     r, s = cut_rod_extend(p, n)
#     ans = []
#     while n > 0:
#         ans.append(s[n])
#         n -= s[n]
#
#     return ans
# '''------------------------------------------------------------------------------------------------------------------'''
# '''
# 最长公共子序列(LCS：Longest Commont Sequence)
# 应用场景：字符串相似度比对
# '''
#
# def lcs(x, y):
#     m = len(x)
#     n = len(y)
#     c = [[0 for _ in range(n+1)] for _ in range(m+1)]
#     b = [[0 for _ in range(n + 1)] for _ in range(m + 1)] #1左上方 2上方 3左方
#
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#
#             if x[i-1] == y[j-1]:
#                 c[i][j] = c[i-1][j-1] + 1
#                 b[i][j] = 1
#             elif c[i-1][j] > c[i][j-1]:
#                 c[i][j] = c[i-1][j]
#                 b[i][j] = 2
#             else:
#                 c[i][j] = c[i][j-1]
#                 b[i][j] = 3
#
#
#     return c[m][n], b
#
# def lcs_trackback(x, y):
#
#     c, b = lcs(x, y)
#     i = len(x)
#     j = len(y)
#     res = []
#     while i > 0 and j > 0:
#         if b[i][j] == 1:
#             res.append(x[i-1])
#             i -= 1
#             j -= 1
#         elif b[i][j] == 2: #不匹配，来自上方
#             i -= 1
#         else:
#             j -= 1
#
#     return "".join(reversed(res))
#
# '''------------------------------------------------------------------------------------------------------------------'''
# '''欧几里得算法'''
# def GCD_1(a, b): #greatest common divisor
#     if b == 0:
#         return a
#     else:
#         return GCD_1(b, a % b)
#
# def GCD_2(a, b):
#     while b>0:
#         a, b = b, a%b
#     return a
#
# '''实现分数计算'''
# class Fraction(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         x = self.GCD(a, b)
#         self.a /= x
#         self.b /= x
#
#     def GCD(self, a, b):
#         while b > 0:
#             a, b = b, a % b
#         return a
#
#     def zxgbs(self, a, b):#求a,b的最小公倍数
#         x = self.GCD(a, b)
#         return x*(a/x)*(b/x)
#
#     def __add__(self, other):
#         a = self.a
#         b = self.b
#         c = other.a
#         d = other.b
#
#         fenmu = self.zxgbs(b, d)
#         fenzi = a*(fenmu/b) + c*(fenmu/d)
#
#         return Fraction(fenzi, fenmu)
#
#     def __str__(self):
#         return "%d/%d" % (self.a, self.b)
#
# if __name__ == '__main__':
#
#     '''钢条切割问题'''
#     '''-------------------------------------------------------------------'''
#     #print(fabonacci(5)[0])
#     #print(fabonacci_no_rec(5))
#
#     p1 = [0,1,5,8,9,10,17,17,20,21,23,24,26,27,27,28,30,33,36,39,40]
#     p2 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
#     # print(cut_rod_rec_1(p1, 9))
#     #print(cut_rod_rec_2(p2, 9))
#     # print(c1(p1, 10))
#     # print(c2(p1, 10))
#     #print(cut_rod_db(p2, 9))
#     #print(cut_rod_extend(p2, 9))
#     #print(cut_rod_solution(p2, 9))
#     '''-------------------------------------------------------------------'''
#     list_a = "ABCBDAB"
#     list_b = "BDCABA"
#
#     # c, b = lcs(list_a, list_b)
#     # for _ in b:
#     #     print(_)
#     #print(lcs_trackback(list_a, list_b))
#     '''-------------------------------------------------------------------'''
#     '''欧几里得算法'''
#     p = Fraction(1, 3)
#     q = Fraction(1, 2)
#     print(p+q)







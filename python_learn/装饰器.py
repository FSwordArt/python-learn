# -*- coding:utf-8 -*

import time
'''
目的：对已有函数进行额外的功能扩展，本质上是一个闭包函数
特点：
1.不修改已有函数的源代码
2.不修改已有函数的调用方式
3.给以后函数添加新的功能
'''

# def caltime(func):
#
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print("运行的时间为：", end_time - start_time)
#
#     return inner
#
# @caltime
# def work():
#     for i in range(10000):
#         print(i)
#
# '''
# 通用装饰器：可以装饰任意类型的函数
# '''
# #带有参数和返回值的装饰器，带有不定长参数
#
# def decorator1(func):
#     def inner(*args, **kwargs):
#         print("正在努力计算中")
#         # *args：把元组里的每个元素按照位置参数进行传参
#         # **kwargs：把字典里的每个键值对按照关键字进行传参
#         # 这里对元组和字典进行拆包，仅针对于结合不定长参数的函数使用
#         num = func(*args, **kwargs)
#         return num
#     return inner
#
# @decorator1
# def add(*args, **kwargs):
#     result = 0
#
#     for val in args:
#         result += val
#
#     for value in kwargs.values():
#         result += value
#
#     return result
#
# # result = add(1, 2)
# # print(result)
#
#
# def make_p(func):
#     print("make_p执行了")
#     def inner():
#         result = "<p>" + func() + "</p>"
#         return result
#
#     return inner
#
# def make_div(func):
#     print("make_div执行了")
#     def inner():
#         result = "<div>" + func() + "</div>"
#         return result
#
#     return inner
#
# @make_div
# @make_p
# def content():
#     return "我用python"
#
# # res = content()
# # print(res)

'''
带有参数的装饰器
'''
def return_decorator(flag):
    def decorator(func):
        def inner(num1, num2):
            if flag == "+":
                print("加法计算")
            elif flag == "-":
                print("减法计算")
            num = func(num1, num2)
            return num
        return inner
    return decorator

@return_decorator("+")
def add1(num1, num2):
    result = num1 + num2
    return result

@return_decorator("-")
def sub(num1, num2):
    result = num1 - num2
    return result

a = add1(1, 2)
print(a)

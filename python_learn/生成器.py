'''
简单的生成器 yield
'''
#
# def Fibonacci(re_num):
#
#     a, b = 0, 1
#     index = 0
#
#     while index < re_num:
#
#         #没有yield是函数，有了是个生成器模板
#         yield a
#         a, b = b, a+b
#         index += 1
#
#     return "-----ok-----"
#
# obj = Fibonacci(2) #创建生成器对象
#
# while True:
#
#     try:
#         ret = next(obj)
#         print(ret)
#
#     except Exception as ret:
#         print(ret.value)
#         break


'''
通过send启动生成器
'''
def Fibonacci(re_num):

    a, b = 0, 1
    index = 0

    while index < re_num:

        #没有yield是函数，有了是个生成器模板
        ret = yield a
        print(">>>>>ret:", ret)
        a, b = b, a+b
        index += 1

    return "-----ok-----"

obj = Fibonacci(2) #创建生成器对象

ret = next(obj)
print(ret)

ret = obj.send("test")
print(ret)





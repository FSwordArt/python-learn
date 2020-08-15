# -*-coding: utf-8 -*
'''
闭包的作用：可以保存外部函数的变量
闭包形成的条件
1.函数嵌套
2.内部函数使用了外部函数的变量或参数
3.外部函数返回内部函数
这个使用了外部函数变量或参数的内部函数成为闭包
'''

def func_out():
    num1 = 10

    def func_inner():

        #要修改外部变量必须使用nonlocal关键字
        nonlocal num1
        num1 = 20
        
        result = num1 + 10
        print("结果：", result)

    print("before:", num1)
    func_inner()
    print("after:", num1)


    return func_inner

#获取闭包对象
#这个new_func就是闭包
new_func = func_out()
#执行闭包
new_func()


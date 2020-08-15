# -*-coding: utf-8 -*

import re
'''re.match'''
'''
* 匹配前一个字符出现0次或者无数次
[A-Z], [a-z]可以匹配下划线
'''
# str = '_PYTHONisTHEbest LAngUAge'
# rule = '[a-z\w]*'
# print(re.match(rule, str).group())

# res = re.match("[\w]{4,8}", "pYThonIstHE")
# print(res.group())
#
#
# print(re.match(r"c:\\a.txt", "c:\\a.txt").group())
# print(re.match("[\w]{4,20}@163\.com", "python@163.comsddadwda").group())

'''
^:匹配字符串开头,也有取反的意思
'''
# print(re.match("^p.*", "python is language").group())
# print(re.match("^p\w{5}", "python is language").group())

'''
$:匹配字符串末尾
'''
# print(re.match("[\w]{4,20}@[\w]*\.com$", "python@5989448.com").group())
# print(re.match("[\w]?", "wqeqw").group())

'''
|:匹配左右表达式任意一个,是一个或的关系，前面条件满足就停止
'''
# print(re.match("[1-9]?\d$|100", "100").group())
# print(re.match("(waddwr888|waddwr)", "waddwr888").group())

'''
(ab)分组
'''
# res = re.match("([0-9]*)-(\d*)", "05689-156491321")
# # res = re.match("[0-9]*-\d*", "05689-156491321")
# print(res.group())
# print(res.group(1))
# print(res.group(2))

'''
\num的使用
'''
# htmlTag = "<html><h1>测试数据</h1></html>"
# res = re.match(r"<(.+)><(.+)>(.+)</(\2)></(\1)>", htmlTag)
# print(res.group(4))

'''
(?P)
(?P=name)
别名的使用(?p<name>)
如何使用别名(?P=引用的名字)
'''
# data = "<div><h1>www.baidu.com</h1></div>"
# res = re.match(r"<(?P<div>\w*)><(?P<h1>\w*)>.*</(?P=h1)></(?P=div)>", data)
# print(res.group())



'''re.compile'''
'''
compile模块中的编译方法，可以吧一个字符串编译成字节码
优点：在使用正则表达式进行match操作时，python会把字符串转为正则表达式对象
    而如果使用compile只需要完成一次转换即可，以后再使用模式对象的话，无需重复转换
'''
# reobj = re.compile("\d{4}")
# print(reobj.match("123456").group())

'''re.findall'''
'''
使用频率高 findall(string[, pos[, endpos]]) 查询字符串中某个正则表达式全部的非重复出现的情况
'''
# reobj = re.compile("华.")
# str = "华人的后代是华裔"
# res = reobj.findall(str)
# print(res)
print(re.match(".*?", "abc123").group())

'''
re.sub  替换
re.subn 返回被替换的数量，以元组的形式
'''
# reobj = re.compile("h")
# res = reobj.sub("H", "hello worhd")
# # res = re.sub("h", "H", "hello worhd")
# print(res)







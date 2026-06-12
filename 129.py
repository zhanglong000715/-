"""
演示Python正则表达式re模块的3个基础匹配语法
"""
import re

# s = "python ithiema"
# # match 从头匹配
# result = re.match("python", s)
# print(result)
# print(result.span())
# print(result.group())
# search 搜索匹配
# s = "1python666itheima666python666"
# result = re.search("python", s)
# print(result)
# print(result.span())
# print(result.group())

# findall 搜索全部匹配
s = "1p2y3t4h5o6n"
result = re.findall(r"\w", s)
print(result)
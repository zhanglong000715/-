"""
演示对文件的读取
"""

# 打开文件
f=open('D:/word.txt','r',encoding='UTF-8')
# print(type(f))
# 读取文件-read()
# print(f'读取8个字节的结果是：{f.read(8)}')
# print(f'读取8个字节的结果是：\n{f.read()}')

# 读取文件-readlines()
# lines=f.readlines()    # 读取文件的全部行，封装到列表中
# print(f'lines对象的类型：{type(lines)}')
# print(f'lines对象的内容是：{lines}')

# 读取文件-readline()
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# print(f'第一行数据是：{line1}')
# print(f'第二行数据是：{line2}')
# print(f'第三行数据是：{line3}')

# for循环读取文件行
# for line in f.readlines():
#     print(f'每一行数据的内容是{line}')

# 文件的关闭
# f.close()
# import time
# time.sleep(500000)

# with open 语法操作文件
# with open('D:/word.txt','r',encoding='UTF-8') as f:
#     for line in f:
#         print(f'每一行数据是：{line}')

# import time
# time.sleep(500000)
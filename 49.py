"""
演示数据容器之：list列表
"""

# 定义一个列表
my_list=['itheima','itcast','python']
print(my_list)
print(type(my_list))

my_list=['itheima',666,True]
print(my_list)
print(type(my_list))
# 定义一个嵌套的列表
my_list=[[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))
# 通过下标索引取出数据（倒序取出）
my_list=['tom','lily','rose']
# 通过列表[下标索引],从前向后从0开始，每次加1.   从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 错误示例，通过下标索引取数据，一定不要超出范围
# print(my_list[3])

# 通过下标索引取数据（倒序取出）
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


# 取出嵌套列表的元素
my_list=[[1,2,3],[4,5,6]]
print(my_list[1][1])
"""
演示tuple
"""

# 定义元组
t1=(1,'hello',True)
t2=()
t3=tuple()
print(f't1的类型是：{type(t1)}，内容是{t1}')
print(f't1的类型是：{type(t2)}，内容是{t2}')
print(f't1的类型是：{type(t3)}，内容是{t3}')

# 定义单个元素的元素
t4=('hello',)
print(f't4的类型是：{type(t4)}，t4的内容是：{t4}')
# 元组的嵌套
t5=((1,2,3),(4,5,6))
print(f't5的类型是{type(t5)},内容是{t5}')

# 下标索引去取出内容
num=t5[1][2]
print(f'从嵌套元组中取出的数据是：{num}')

# 元组的操作：index查找方法
t6=('传智教育','黑马程序员','python')
index=t6.index('黑马程序员')
print(f'在元组t6中查找黑马程序员，的下标是：{index}')

# 元组的操作：count统计方法
t7=('传智教育','黑马程序员','黑马程序员','黑马程序员','python')
num=t7.count('黑马程序员')
print(f'在元组t7中统计黑马程序员的数量有：{num}个')

# 元组的操作：len函数统计元组元素数量
t8=('传智教育','黑马程序员','黑马程序员','黑马程序员','python')
num=len(t8)
print(f'在元组t8中总共有{num}个元素')
# 元组的遍历：while
index=0
while index<len(t8):
    print(f'元组的元素有：{t8[index]}')
    index+=1


# 元组的遍历：for
for element in t8:
    print(f'2元组的元素有：{element}')

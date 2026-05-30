# 将数字类型转换成字符串
num_str=str(11)
print(type(num_str),num_str)

float_str=str(11.345)
print(float_str)

# 将字符串转换为数字
num=int('11')
print(type(num),num)

num2=float("11.345")
print(type(num2),num2)

# 错误示例，想要将字符串转换成数字，必须要求字符串里的内容都是数字
# num3=int('黑马程序员')
# print(type(num3),num3)

# 整数转浮点数
float_num=float(11)
print(type(float_num),float_num)

# 浮点数转整数
int_num=int(11.345)
print(type(int_num),int_num)

"""
任何类型都可以转换成字符串
字符串不可以随意转换成数字，字符串内必须只有整数才可以转换
浮点数转整数会丢失精度，小数点后的数字无法输出
"""
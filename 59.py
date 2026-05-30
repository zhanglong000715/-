my_str='itheima itcast boxuegu'
num=my_str.count('it')
print(f'字符串{my_str}中有：{num}个it')

num=my_str.replace(' ','|')
print(f'字符串{my_str}，被替换空格后，结果：{num}')

my_num_str=num.split('|')
print(f'字符串{num}，按照|分隔后，得到：{my_num_str}')
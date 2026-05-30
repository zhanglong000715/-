"""
演示异常，模块，包的综合案例练习
"""
# 创建my_utils 包，在包内创建：str_util.py 和 file_util.py 2个模块，并提供相应的函数

import my_utils.str_utils
from my_utils import file_utils

print(my_utils.str_utils.str_reverse('黑马程序员'))
print(my_utils.str_utils.substr('itheima',0,4))


file_utils.append_to_file('D:/test.txt','itheima')
file_utils.print_file_info('D:/test.txt')

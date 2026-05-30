"""
演示自定义模块
"""

# 导入自定义模块使用
# import s79
# from s79 import test
# test(1,2)

# 导入不同模块的同名功能
# from s79 import test
# from s2s79 import test
# test(1,2)
# __main__变量
# from s79 import test
# test(2,3)

# __all__变量
from s79 import *
test_a(1,2)
test_b(2,1)


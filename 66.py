"""
演示函数的多返回值示例
"""

# 演示使用多个变量，接收多个返回值
def test_return():
    return 1,'hello',True

x,y,z=test_return()
print(f'{type(x)},{type(y)},{type(z)}')
print(x)
print(y)
print(z)
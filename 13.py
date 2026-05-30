"""
演示python的input语句
获取键盘的输入信息
"""

print('请告诉我你是谁')
name=input()
print('我知道了,你是：%s' % name)

# 输入数字类型
num=input('请告诉我你的银行卡密码')
# 数字类型转换
num=int(num)
print('你的银行卡密码类型是：',type(num))
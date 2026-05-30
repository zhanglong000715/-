"""
 演示python中变量的相关操作
"""

# 定义一个变量，用来记录钱包余额
money=100
# 通过print语句，输出变量记录的内容
print('钱包还有',money,"元")

# 买了一个冰淇凌花费十元
print('买冰淇凌要减去十元')
print('钱包余额减去冰淇凌价格=',money-10)
print('买完冰淇凌后')
print('钱包还剩:',money-10,'元')

# 每隔一小时，输出一下钱包余额
money=money-10
print('现在是下午1点，钱包余额剩余',money,'元')
money=money-10
print('现在是下午2点，钱包余额剩余',money,'元')
money=money-10
print('现在是下午3点，钱包余额剩余',money,'元')
money=money-10
print('现在是下午4点，钱包余额剩余',money,'元')

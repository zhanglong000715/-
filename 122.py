"""
演示python的闭包特性
"""

# 简单闭包
# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
# fn = outer("黑马程序员")
# fn("大家好")

# 使用nonlocal关键字修改外部函数的值
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
# fn1 = outer(10)
# fn1(10)
# fn1(20)


# 使用闭包实现ATM小案例
def account_amount(initial_amount=0):

    def atm(num,deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存入+{num}元，当前余额{initial_amount}元")
        else:
            initial_amount-=num
            print(f"取出-{num}元，当前余额{initial_amount}元")

    return atm

atm = account_amount()
atm(100)
atm(200)
atm(100,False)












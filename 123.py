"""
演示装饰器的写法
"""

# 装饰器的一般写法(闭包)
# def sleep():
#     import time
#     import random
#     print("睡眠中......")
#     time.sleep(random.randint(1,5))
#
# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("起床了")
#
#     return inner

# fn = outer(sleep)
# fn()

# 装饰器的快捷写法(语法糖)
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("起床了")

    return inner
@outer
def sleep():
    import time
    import random
    print("睡眠中......")
    time.sleep(random.randint(1,5))

sleep()










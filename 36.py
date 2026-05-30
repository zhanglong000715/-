import random

age=10000
for i in range(1,21):
    if age>=1000:
        num=random.randint(1,10)
        if num<=4:
            print(f'员工{i}，绩效分{num}，不发工资，下一位')
        elif num<=10:
            age=age-1000
            print(f"员工{i}，发放工资1000元，账户余额还剩余{age}元。")

    elif age<=1000:
        break
print(f'余额不足，当前余额{age}元，不足以发工资，不发了，下个月再来')








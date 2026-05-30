num=100
age=0
for x in range(1,num):
    if x%2==0:
        age=age+1
print(f'1到100（不含100本身）范围内，有{age}个偶数。')

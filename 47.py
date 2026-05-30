# 定义全局变量
money=5000000
name='周杰轮'
# 定义功能函数
def func_a(show_header):
    if show_header:
        print('-----查询余额-----')
    print(f'{name}您好，您的余额剩余：{money}元')
def func_b(num):
    global money
    money+=num
    print('-----存款-----')
    print(f'{name}您好，您存款{num}元成功')
    func_a(False)
def func_c(num):
    global money
    money-=num
    print('-----取款------')
    print(f'{name}您好，您取款{num}元成功')
    func_a(False)
def func_d():
    print('-----主菜单-----')
    print(f'{name}您好，欢迎来到黑马银行ATM，请选择操作：')
    print('查询余额\t【输入1】')
    print('存款\t\t【输入2】')
    print('取款\t\t【输入3')
    print('退出\t\t【输入4】')
    return input('请输入你的选择：')

# 核心循环
while True:
    keyboard_input=func_d()
    if keyboard_input == '1':
        func_a(True)
        continue # 执行完回到循环开头
    elif keyboard_input == '2':
        num=int(input('请输入存款金额：'))
        func_b(num)
        continue
    elif keyboard_input == '3':
        num=int(input('请输入取款金额'))
        func_c(num)
        continue
    elif keyboard_input == '4':
        print('程序退出，欢迎下次光临')
        break
    else:
        print('输入错误，请重新输入')




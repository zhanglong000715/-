def list_while_func():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = 0
    list_a = []
    while index < len(list):
        num = list[index]
        if num % 2 == 0:
            list_a . append(num)
        index += 1

    print(f'通过while循环，从列表：{list}中取出偶数，组成新列表：{list_a}')


def list_for_func():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_a=[]
    for num in list:
        if num % 2 == 0:
            list_a . append(num)

    print(f'通过for循环，从列表：{list}中取出偶数，组成新列表：{list_a}')


list_for_func()
list_while_func()


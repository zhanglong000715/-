def list_while_func():
    list_a=[1,2,3,4,5,6,7,8,9,10]
    index=0
    list_b=[]
    while index<len(list_a):
        if list_a[index] %2 ==0:
            list_b.append(list_a[index])
        index+=1
    print(list_b)


def list_for_func():
    list_a=[1,2,3,4,5,6,7,8,9,10]
    list_b=[]
    for index in range(len(list_a)):
        if list_a[index] %2 ==0:
            list_b.append(list_a[index])

    print(list_b)



list_while_func()
list_for_func()
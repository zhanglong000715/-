mylist=[21,25,21,23,22,20]
mylist.append(31)
print(mylist)
mylist_2=[29,33,30]
mylist.extend(mylist_2)
print(mylist)
age=mylist[0]
print(mylist,age)
age=mylist[-1]
print(mylist,age)
age=mylist.index(31)
print(mylist,age)


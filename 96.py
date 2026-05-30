# 创建一个类
class Student:
    # 创建一个类的方法
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
stu_list=[]  # 定义一个空列表用作储存学生信息
idex=1        # 定义一个变量用于显示for循环次数
# 利用for循环录入十次学生信息并使用构建方法完成学生信息的录入并打印出结果
for i in range(10):
    # 让学生输入信息并将其赋值给一个变量
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    score = input("请输入学生地址")
    # 调用类并把它赋值给一个变量
    stu = Student(name,age,score)
    # 通过print语句输出stu变量里的元素
    print(f"学生{idex}信息录入完成，信息为：【学生姓名：{stu.name}，年龄{stu.age}，地址{stu.score}】")
    # 每循环一次都记录下来并增加index的值
    idex += 1
    # 将stu通过.append保存进一个叫stu_list的列表里
    stu_list.append(stu)
    # 防止循环边界问题导致最终显示“当前录入第11位学生”
    if idex <= 10:
        print(f"当前录入第{idex}位学生信息，总共需录入10位学生信息")
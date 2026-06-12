"""
演示设计模式之工厂
"""


class Person:
    pass

class Student(Person):
    pass

class Worker(Person):
    pass

class Teacher(Person):
    pass

class PersonFaculty:
    def get_person(self, p_type):
        if p_type == "w":
            return Worker()
        if p_type == "s":
            return Student()
        if p_type == "t":
            return Teacher()

pf = PersonFaculty()
worker = pf.get_person("w")
teacher = pf.get_person("t")
student = pf.get_person("s")

print(worker)
print(teacher)
print(student)


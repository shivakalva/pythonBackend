class Person:

    def __init__(self, personname, personage):
        self.name = personname
        self.age = personage

    def getname(self):
        print(self.name)

    def getage(self):
        print(self.age)


class student(Person):
    studentid = ""

    def __init__(self, studentname, studentage, studentid):
        Person.__init__(self, studentname, studentage)
        self.studentid = studentid

    def getId(self):
        return self.studentid


x = Person("shiva", "26")
print(x.getname())
print(x.getage())
y = student("shiva", "26", "123")
print(y.getId())

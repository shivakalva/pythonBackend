class first:
    def __init__(self, name, surname, aged):
        self.a = name
        self.b = surname
        self.age = aged

    def getdetails(self):
        print("details are" + " " + self.a, self.b, self.age)


class second(first):
    height = ''

    def __init__(self, sname, ssurname, sage, height):
        first.__init__(self, sname, ssurname, sage)
        self.height = height

    def getheight(self):
        print(self.height)


x = first("shiva", "kalva", "26")
# print(x.a)
# print(x.b)
# print(x.getdetails())
y = second("ram", "kalva", "27", "5.9")
print(y.a)
print(y.b)
print(y.getdetails())
print(y.getheight())

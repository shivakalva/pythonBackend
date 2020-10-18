# all the objects must be initialised in the init method
# __init__() method is called when an object is fully initialized


class employee:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    #
    def getage(self):
        print("they may age is ", self.age)

    def getinfo(self):
        print("hey name is ", self.name)

hi = employee("shiva",27)
print(hi.getinfo())
print(hi.getage())


his = employee("mark",24)
print(his.getinfo())
print(his.getage())

class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name + " " + "is sitting")

# obj = Dog("williams")
# obj.sit()
class pup(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def bark(self):
        print(self.name + " " + "barking")

    def dogage(self):
        print(self.age + " " + "doga ge")

pupobj = pup("jmmy","25")
pupobj.dogage()
pupobj.sit()
pupobj.bark()
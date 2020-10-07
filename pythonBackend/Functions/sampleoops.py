class oops:
    def __init__(self, a, b):
        self.firstname = a
        self.lastname = b

    def getName(self):
        return "my name is" + " " + self.firstname + " " + "ands my" + self.lastname

    def getDob(self, year):
        return "my DOB IS" + self.year()


calls = oops("shiva", "kalva")
print(calls.getName())
callss = oops(1992)
print(calls.getDob(1992))

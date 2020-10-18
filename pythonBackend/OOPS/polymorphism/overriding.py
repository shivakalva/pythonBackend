# Overriding and super keywor
class Emloyee:

    def setworkinghours(self):
        self.numberofworkinghours = 40

    def displayWorkingHours(self):
        print(self.numberofworkinghours)

class Trainer(Emloyee):

    def setworkinghours(self):
        self.numberofworkinghours = 45

    def resetworkinghours(self):
        super().setworkinghours()

Emloye = Emloyee()
Emloye.setworkinghours()
Emloye.displayWorkingHours()
T = Trainer()
T.setworkinghours()
T.displayWorkingHours()
T.resetworkinghours()
T.displayWorkingHours()
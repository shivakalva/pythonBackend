#instance methods are the methods of your class that make use of the  self parameter to access and modify the instance
# attributes of your class
# static methods are the methods that doesn't takes the self parameter and it ignores the binding of the object

class instance:

    def getdetails(self):
        self.name = "shiva"

    @staticmethod
    def getinfo():
        print("welcome")


yes = instance()
print(yes.getdetails())
print(yes.getinfo())
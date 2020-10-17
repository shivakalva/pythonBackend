# Self is the reference to the object itself
# First parameter we receive will be object
# when we create an object without self parameter
# when we create an instance attribute, our objective is that attribute is available for the life span of the object
   #  life span  -- create and destruction
class celf:
    def employeedetails(self):
        self.name = "Shiva"
        print(self.name)

        age = 30                      # the scope of the age is limited only this method
        print("age ", age)

    def printemployeedetails(self):
        print("another method")      # age cannot be accessed in this method because we didnot take name of obj
        print(self.name)
        print(age)

x = celf()
print(x.employeedetails())
print(x.printemployeedetails())

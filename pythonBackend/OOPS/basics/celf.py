# Self is the reference to the object itself
# First parameter we receive will be object
# when we create an object without self parameter it is available only for the specific method
# when we create an instance attribute, our objective is that attribute is available for the life span of the object
   #  life span  -- create and destruction
# Every instance method accepts has a default parameter that is being accepted. By convention, this parameter is named self.
#  The self parameter is used to refer to the attributes of that instance of the class.
class celf:
    def employeedetails(self):
        self.name = "Shiva"
        print(self.name)

        age = 30                      # the scope of the age is limited only this method  employeedetails
        print("age ", age)

    def printemployeedetails(self):
        print("another method")      # age cannot be accessed in this method because we didnot take name of obj
        print(self.name)
        print(age)

x = celf()
print(x.employeedetails())
print(x.printemployeedetails())

class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

        # defining class methods

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

        # Line: 19, end of superclass definition


# definition of subclass starts here
class Student(Person):  # Line: 22, Person is the  superclass and Student is the subclass
    studentId = ""

    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName,
                        studentAge)  # Line: 26, Calling the superclass constructor and sending values of attributes.
        self.studentId = studentId

    def getId(self):
        return self.studentId  # returns the value of student id


# Create an object of the superclass
person1 = Person("Richard", 23)  # Line: 35
# call member methods of the objects
person1.showAge()
# Create an object of the subclass  
student1 = Student("Max", 22, "102")  # Line: 39
print(student1.getId())
student1.showName()  # Line: 41

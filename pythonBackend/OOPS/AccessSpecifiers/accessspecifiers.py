# public  -- anywhere
# Protected --> _memberName  -- with in class and withinderived classes and no where else
# Private -->   __memberName   -- with in the class
class Car:
    numberOfWheels = 4
    _Color = "Red"
    __speed = 200  # Name Mangling

class BMW(Car):
    def __init__(self):
        print(self._Color)

car = Car()
print(car.numberOfWheels)
bmw = BMW()
print(car._Car__speed)



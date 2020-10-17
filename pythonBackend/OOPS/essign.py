class Essign:
    DailySleep = 8     # class attribute

person_1 = Essign()
print(person_1.DailySleep)

Essign.DailySleep = 10     # for object when we provide the name of the attribute it first checks with instance attrubte and then cass attributes
print(person_1.DailySleep) # instance attribute with samename


# First it checks for the instance attributes if they are not present they go to the class Attributes

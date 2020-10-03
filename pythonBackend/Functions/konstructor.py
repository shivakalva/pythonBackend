class konstructor:
    vars = 2  # class variables they are equal

    ###########Even thought we have not called the constructor, it was called explictly ###########
    def __init__(self, a, b):
        self.firstnumber = a  # instance variables they keep on changing for every object crreation
        self.secondnumber = b  # instance variables they keep on changing for every object crreation

    def getdata(self):
        print("i am getting the data")

    def summation(self):
        return self.firstnumber + self.secondnumber

x = konstructor(1, 2)
print(x.summation())
print(x.getdata())
x1 = konstructor(3, 4)
print(x1.summation())
# print(x.getdata())

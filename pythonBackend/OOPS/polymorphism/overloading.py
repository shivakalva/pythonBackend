class square:
    def __init__(self, side):
        self.side = side

    def __add__(self, other):
        return ((4 * squareOne.side) + (5 * squareTwo.side))

squareOne = square(5)
squareTwo = square(10)
print(squareOne + squareTwo)

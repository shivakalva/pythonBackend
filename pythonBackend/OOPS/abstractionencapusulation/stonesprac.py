class preciousStones:
    currentStones = 0
    collectionOfStones = []

    def __init__(self, name):
        self.name = name

        preciousStones.currentStones += 1

        if preciousStones.currentStones <=5:
            preciousStones.collectionOfStones.append(self)
        else:
            del preciousStones.collectionOfStones[0]
            preciousStones.collectionOfStones.append(self)

    @staticmethod
    def displaystones():
        for stones in preciousStones.collectionOfStones:
            print(stones.name, end = ' ')
        print()


stoneOne = preciousStones("Diamond")
stoneTwo = preciousStones("Ruby")
stoneThree = preciousStones("Emerald")
stoneFour = preciousStones("Saphire")
stoneFive = preciousStones("Onyx")
stoneFive.displaystones()
stoneSix = preciousStones("Amber")
stoneFive.displaystones()


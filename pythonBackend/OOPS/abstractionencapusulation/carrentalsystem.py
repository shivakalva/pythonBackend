class rentalCompany:
    def __init__(self, availableCars):
        self.cars = availableCars

    def printAvailableCars(self):
        print("Cars currently available and daily rate:  ")
        print('Ford Fiesta: £', self.cars['Ford Fiesta'])
        print('Ford Mondeo: £', self.cars['Ford Mondeo'])
        print('Ford Kuga: £', self.cars['Ford Kuga'])

    def printTotalRental(self, daysRequired, typeOfCar):
        return self.cars[typeOfCar * numberOfDays]


fordGarage = rentalCompany({'Ford Fiesta': 30, 'Ford Mondeo': 50, 'Ford Kuga': 100})
while True:
    print("Press 1 to list vehicles")
    print("Press 2 to select vehicle")
    print("Press 3 to exist")
    userChoice = int(input())
    if userChoice == 1:
        fordGarage.printAvailableCars()
    elif userChoice == 2:
        print("Which car would you like to borrow")
        typeOfCar = input()
        print("How long would you like to borrow it for")
        daysRequired = input()
        fare = fordGarage.printTotalRental()
        print("Total price is £", fare)
        print("Thank you")
    elif userChoice == 3:
        quit()

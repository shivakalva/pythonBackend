# greeting = input("what is your age? \n")
# name = int(greeting)
# print(name)

###################################################################
# squares = []
# for x in range(1, 11):
#  squares.append(x**2)
# print(squares)
###################################################################

squares = [x**2 for x in range(1,25)]
print(squares)
###################################################################
# Copying a list
# copy_of_bikes = bikes[:]

###################################################################

favourites = {'Shiva': 25, 'Ram': 36}
for name, value in favourites.items():
    print(name + " " + str(value))

###################################################################





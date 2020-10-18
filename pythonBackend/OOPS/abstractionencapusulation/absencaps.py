# library management systems  # first define the layers of abstraction   # library module and then customer module
# library module --> display a book, lend a book, add a book   # customer module -- > request a book, return a book

class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print("Available Books")
        for book in self.availableBooks:
            print(book)

    def lendBooks(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("you will get the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("out of stock buddy")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("you have retuned the book")


class Customer:
    def __init__(self):
        self.book = input()

    def requestBook(self):
        print(" enter the book you want to burrow")
        return self.book

    def returnBook(self):
        print(" please name the book you want to return")
        self.book = input()
        return self.book


library = Library(['Shiva', 'Ram', 'Hanuman'])

customer = Customer()

while True:
    print("enter 1 to display the available books")
    print(" enter 2 to request a book")
    print(" enter 3 to return a book")
    print(" enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBooks(requestedBook)
    elif userChoice is 3:
        returnedBook = Customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()

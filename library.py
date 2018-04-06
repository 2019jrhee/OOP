# Class => Library
# Layers of abstraction => display available books, to lend a book, to add a books

# Class => Customer
# Layers of abstraction => request for a book, return a books

class Library:

    def __init__(self,listofbooks):
        self.availablebooks = listofbooks

    def displayavailablebooks(self):
        print()
        print("Available Books: ")
        for book in self.availablebooks:
            print(book)

    def lendbook(self, requestedbook):
        if requestedbook in self.availablebooks:
            print("You have now borrowed the book")
            self.availablebooks.remove(requestedbook)
        else:
            print("Sorry, the book is not available in our list")


    def addbook(self, returnedbook):
        self.availablebooks.append(returnedbook)
        print("You have returned the book. Thank You")


class Customer:
    def requestbook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book
        print()

    def returnbook(self):
        print()
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book
        print()

library = Library(['Bunnie and Turtle', 'Red Scare', 'Diversity and Equality'])
customer = Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.displayavailablebooks()
    elif userChoice is 2:
        requestedbook = customer.requestbook()
        library.lendbook(requestedbook)
    elif userChoice is 3:
        returnedbook = customer.returnbook()
        library.addbook(returnedbook)
    elif userChoice is 4:
        quit()

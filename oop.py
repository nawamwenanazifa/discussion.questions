# 1.
# Create a class called Car with attributes brand and color. Instantiate an object of the Car class 
# and print its attributes.
# Define the Car class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Create an object of the Car class
my_car = Car(brand="Jeep", color="Red")

# Print the attributes of the Car object
print(f"\nMy car Brand is: {my_car.brand}\t")
print(f"\nMy car Color is: {my_car.color}\t")



#2.
# Add a method called start_engine to the Car class that prints a 
# message saying the engine of the car has started. Create an instance of Car and call the method.              

# Define the Car class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method to start the engine
    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started.")

# Create an object of the Car class
my_car = Car(brand="Jeep", color="Red")

# Call the start_engine method
my_car.start_engine()

#3.
# Create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount (only if sufficient balance exists).
#Print the account balance.
# Define the BankAccount class
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit an amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw an amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to print the account balance
    def print_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")

# Example usage
my_account = BankAccount(account_number="123456789", balance=500.0)

# Deposit money
my_account.deposit(200)

# Withdraw money
my_account.withdraw(100)

# Attempt to withdraw more than the available balance
my_account.withdraw(700)

# Print the account balance
my_account.print_balance()

#4.
# Implement a class called Library that manages a collection of books. 
# Each book has a title, author, and available status. The Library class should have methods to:
#Add a book to the library.
#Remove a book from the library.
#Check if a book is available by title.
#Borrow a book (mark it as unavailable if it’s available).
#Return a book (mark it as available again if it was borrowed).
class Book:
    #Represents a single book in the library.
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    #Manages a collection of books.
    def __init__(self):
        self.books = []

    # Add a book to the library
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    # Remove a book from the library
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    # Check if a book is available
    def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return book.available
        print(f"Book '{title}' not found in the library.")
        return False

    # Borrow a book
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"Sorry, '{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")

    # Return a book
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"Thank you for returning '{title}'.")
                else:
                    print(f"'{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")

# Example usage
library = Library()

# Add books
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

# Check availability
print("Is '1984' available?", library.is_available("1984"))  # True

# Borrow a book
library.borrow_book("1984")
print("Is '1984' available?", library.is_available("1984"))  # False

# Return a book
library.return_book("1984")
print("Is '1984' available?", library.is_available("1984"))  # True

# Remove a book
library.remove_book("To Kill a Mockingbird")





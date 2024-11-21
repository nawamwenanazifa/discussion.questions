#LOOPS
#1.Basic: Write a python program that prints all even numbers btn 1 and 20 using for loop
#initialising the loop
for even in range (1,21):
    if even % 2 == 0:
        print(even)

#2.Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10
valid_input = False
# for it to continue asking for input until valid 
while not valid_input:
    try:
       #Ask the user for input
        num = int(input("Enter a number greater than 10:"))
        #check if the input is valid
        if num > 10:
            #making it to exit the loop when the input is valid
            valid_input = True
            print(f"You entered: {num}")
        else:
            print("Please enter a number greater than 10:")
    except ValueError:
        print("Invalid input. Please enter a whole number:") 

#3. Advanced: Write a program that prints the multiplication tables(from 1 to 10) for numbers from 1 to 5 using nested for loops
#print multiplication tables for numbers to  1 to 5
#Outer loop for numbers to 1 to 5
for num in range (1,6):
    print(f"Multiplication Table of {num}:")
    #inner loop for multiplication factors 1 to 10
for factor in range (1,11):
    product = num * factor
    print(f"{num} x {factor}) =({product}")
# print newline for separation
print()     
#4.
# Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], whrite a program using for loop to find the sum of all odd numbers and print the result 
#List of integers 
numbers = (4,7,2,9,12,15)
#sum of odd numbers
odd_sum = 0
# iterate  over the list using a for loop
for  num in numbers:
#check if the number is odd
 if num % 2!= 0:
    #Add odd numbers to sum 
    odd_sum += num
    print("Sum of odd numbers:",odd_sum)     
                
                
#LISTS
#1.Basic: create a list of 5 fruits and print each fruit on a new line using a for loop
fruits = ["Avacado", "Cherry", "Mango", "Orange", "Pineaaple"]
for fruit in fruits:
    print(fruit)
    
#2.Intermediate: Write a funtion that takes a list of numbers and returns new list with each number  squared. Example:[1,2,3] should become [1,4,9]
#Define a function to square numbers
def square_numbers(numbers):
    return[n**2 for n in numbers]
numbers = [1,2,3,4,5]
squared_numbers
square_numbers(numbers)
print("Original list:", numbers)
print("Squared Numbers:", square_numbers)
#3.Advanced: Write a python program that takes two lists, list1 = [1,2,3] and list2 = [4,5,6],and combine them into single list,combined=[1,4,2,5,3,6]
#4. Challenge: Given a list of numbers, [3,1,4,1,5,2], write a program to find and print the two largest numbers in the list with out using the max()function.                   
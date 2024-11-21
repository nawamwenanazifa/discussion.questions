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
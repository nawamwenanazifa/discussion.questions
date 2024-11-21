
#LISTS
#1.Basic: create a list of 5 fruits and print each fruit on a new line using a for loop
fruits = ["Avacado", "Cherry", "Mango", "Orange", "Pineaaple"]
for fruit in fruits:
    print(fruit)
    
#2.Intermediate: Write a funtion that takes a list of numbers and returns new list with each number  squared. Example:[1,2,3] should become [1,4,9]
def square_numbers(numbers):
    # Use a list comprehension to square each number in the list
    return [number ** 2 for number in numbers]

numbers = [1, 2, 3]
squared_numbers = square_numbers(numbers)
print("Original list:", numbers)
print("Squared list:", squared_numbers)

#3.Advanced: Write a python program that takes two lists, list1 = [1,2,3] and list2 = [4,5,6],and combine them into single list,combined=[1,4,2,5,3,6]
list1= [1,2,3]
list2=[4,5,6]
list3=list1 + list2
print(list3)
#4. Challenge: Given a list of numbers, [3,1,4,1,5,2], write a program to find and print the two largest numbers in the list with out using the max()function.


numbers = [3, 1, 4, 1, 5, 2]

# Initialize variables to store the two largest numbers
largest = float('-inf')  # Smallest possible number
second_largest = float('-inf')

# Loop through the list to find the largest and second largest numbers
for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("The two largest numbers are:", largest, "and", second_largest)

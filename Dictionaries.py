# 1.
# Create a dictionary with three key-value pairs representing a student's information:
#  name, age, and grade. Print each key-value pair on a new line.

student_information = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Print each key-value pair on a new line
for key, value in student_information.items():
    print(f"{key}: {value}")

# 2.
# Write a function that takes a dictionary of people's names and their ages,
#  {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def agesOfPeople(people):

    
    return [name for name, age in people.items() if age >= 21]

# Example usage
people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
adults = agesOfPeople(people)

# Print the result
print("People 21 or older:", adults)

# 3.
# Given a dictionary representing items in a store with their prices, 
# {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of
#  items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.

# Dictionary representing items and their prices
store_prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}

# List of items bought
items_bought = ['apple', 'orange', 'banana', 'banana']

# Calculate the total cost
total_cost = 0
for item in items_bought:
    if item in store_prices:
        total_cost += store_prices[item]

# Print the total cost
print("Total cost:", total_cost)

# 4.
# Write a program that counts the occurrences of each word in a given sentence. 
# Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.

# Input sentence
sentence = "hello world hello"

# Split the sentence into words
words = sentence.split()

# Dictionary to store word counts
word_counts = {}

# Count occurrences of each word
for word in words:
        word_counts[word] = word_counts.get(word,0) +1
        print(f"\nWord count:{word_counts}\t")
   


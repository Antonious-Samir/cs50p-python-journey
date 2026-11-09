# ==============================================================================
# Author: Antonious Adel Samir
# Track: AI & Data Science Diploma | CS50P Fundamentals
# File: 03_Loops.py
# Description: Notes and code examples for loops in Python
# License: MIT License - Open for educational and reference purposes.
# ==============================================================================

# Imagine we want to write a program that prints "meow" 3 times.
# Will we just write print("meow") three times? Absolutely not!
# That is why we introduce a new keyword called WHILE.

# WHILE LOOP: Executes a specific block of code repeatedly under a certain condition.

# For example, if we want our app to meow 3 times:
i = 3  # First, we create an integer variable called 'i'
while i != 0:
    print("meow")
    i = i + 1

# NOTE: Do not run the code above on your PC!
# What was wrong with it? 
# The mistake is in the increment: i = i + 1. The value of 'i' will keep growing, 
# meaning it will never equal 0. This creates an "infinite loop."

# Here is the correct version counting downwards:
i = 3
while i != 0:
    print("meow")
    i = i - 1  # Decrementing ensures the condition (i != 0) will eventually be false.

# Flow Chart for the above loop:
#
#         ( Start )
#             |
#             v
#         [ i = 3 ]
#             |
#             v
#        /         \
#       /   i != 0  \
#       \           /
#        \         /
#         /       \
#   True /         \ False
#       v           v
#  ["meow"]     ( Stop )
#       |
#       v
#  [ i = i - 1 ]
#       |
#       +-----> (loops back to: i != 0)


# We can write the same logic using a positive increment:
i = 1
while i <= 3:
    print("meow")
    i = i + 1

# ==============================================================================
# 1. FOR LOOPS
# ==============================================================================

# We can perform the same repetition using a FOR loop with a list:
for i in [0, 1, 2]:
    print("meow")

# But what if you need to print "meow" 1,000 times? 
# You wouldn't write a list from 0 to 1000. Instead, we use the range() function:
for i in range(1000):
    print("meow")  

# If we don't actually use the variable 'i' inside the loop, 
# Python convention suggests using an underscore (_) as the variable name.
for _ in range(1000):
    print("meow")

# Alternatively, if we just want to print a string multiple times without a loop:
print("meow" * 3)  
# Output: meowmeowmeow

# To format this better, we can add a newline character (\n):
print("meow\n" * 3) 

# However, this leaves an empty blank line at the very end. 
# We can fix this by overriding the default end character of the print function:
print("meow\n" * 3, end="")  

# ==============================================================================
# 2. USER INPUT AND BREAKING LOOPS
# ==============================================================================

# Things get more exciting if we ask the user for the number of meows:
# We can intentionally use an infinite loop and break out of it 
# once the user provides valid input (a positive integer).
while True:
    n = int(input("What's n? "))
    if n > 0:
        break  # Escapes the loop once a valid positive number is entered

for _ in range(n):
    print("meow")

# ==============================================================================
# 3. CUSTOM FUNCTIONS
# ==============================================================================

# We can encapsulate this behavior inside functions to make our code modular.
def main_basic():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main_basic()


# Since there is no built-in function to specifically get a positive number,
# we can create one ourselves:
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n  # 'return' automatically breaks the loop and passes the value back

main()

# ==============================================================================
# 4. LISTS
# ==============================================================================

# Lists allow us to store multiple items in a single variable.
students = ["Hermione", "Harry", "Ron"]

# We can access individual items using their zero-based index:
print(students[0]) 
print(students[1])
print(students[2])

# A cleaner way to iterate through a list is using a FOR loop:
for student in students:
     print(student)

# If we need the index (the numerical position) alongside the item, 
# we can use the len() function to get the list's length, and range() to iterate over it:
for i in range(len(students)): 
    # Adding 1 to 'i' makes the output start at 1 instead of 0 for the user
    print(i + 1, students[i])

# ==============================================================================
# 5. DICTIONARIES (dicts)
# ==============================================================================

# Dictionaries are data structures that allow us to associate a key with a value 
# (like a real-world dictionary mapping a word to its definition).

# What if we want to know who is in what House at Hogwarts?
students_dict = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# Accessing values by their keys:
print(students_dict["Hermione"])
print(students_dict["Draco"]) 

# We can iterate through a dictionary dynamically:
for student in students_dict:
    # 'student' is the key, 'students_dict[student]' is the value.
    # The 'sep' parameter determines what goes between them when printed.
    print(student, students_dict[student], sep=", ") 

# ==============================================================================
# 6. LIST OF DICTIONARIES
# ==============================================================================

# For more complex data, we can create a list where each item is a dictionary.
# The 'None' keyword is used to represent the absence of a value (Draco has no patronus).
students_data = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None} 
]

for student in students_data:
    print(student["name"], student["house"], student["patronus"], sep=", ")


# ==============================================================================
# 7. PRACTICE TASKS
# ==============================================================================
# Try to write the code for these 5 simple tasks to test your understanding!

# Task 1: The Countdown (While Loop)
# Write a while loop that starts at 5 and counts down to 1. 
# Print each number, and after the loop finishes, print "Blastoff!".
# Write your code below:


# Task 2: Repeat After Me (For Loop)
# Use a for loop and the range() function to print the phrase "Python is fun!" 
# exactly 5 times.
# Write your code below:


# Task 3: Secret Password (Input & Break)
# Use a `while True` loop to ask the user for a password. 
# Keep asking until they type "cs50". Once they do, print "Access Granted" and break out of the loop.
# Write your code below:


# Task 4: Favorite Fruits (Lists)
# Create a list of your 3 favorite fruits. 
# Use a for loop to iterate through the list and print "I like [fruit]" for each one.
# Write your code below:


# Task 5: Country Capitals (Dictionaries)
# Create a dictionary with 3 countries as keys and their capitals as values 
# (e.g., "Egypt": "Cairo"). Loop through the dictionary and print:
# "[Capital] is the capital of [Country]"
# Write your code below:
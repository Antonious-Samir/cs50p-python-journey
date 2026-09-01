# ==============================================================================
# Author: Antonious Adel Samir
# Track: AI & Data Science Diploma | CS50P Fundamentals
# File: 01_syntax_and_basics.py
# Description: Notes and code examples exploring string manipulation, 
#              type casting, formatting, basic functions, and control flow.
# License: MIT License - Open for educational and reference purposes.
# ==============================================================================



#SYNTAX MODULE PART1
name = input("What is your name? ")
print("Hello,",name)


#How to do a comment 
#Using hash '#' for single lines 

#Or three double quotation 

"""
comment

as

well

"""
#examples for print 
print("Hello, \"friend\"") # Hello, "friend"
print('Hello,"friend"') # Hello,"friend"
print("Hello,", end="") # Hello, (no new line)
print(f"Hello, {name}") # Hello, name


#remove whitespace from the beginning and end of a string 
name = name.strip()

#however there are another functions to remove whitespace from the beginning only or the end only 
name = name.lstrip() #remove whitespace from the beginning of a string
name = name.rstrip() #remove whitespace from the end of a string


#capitalize the first letter of a string
name = name.capitalize()

#if we used title it will capitalize the first letter of each word in a string
name = name.title()


#remove whitespace from the beginning and end of a string and capitalize the first letter each word in a string
name = name.strip().title()

#you can shorten the code by chaining the methods together
name = input("What is your name? ").title().strip()

#split users name into first and last name
first_name, last_name = name.split(" ")
print(f"Hello, {first_name}") #Hello, first_name

#------------------------------------------------------------------------------------------------------------------------
#CALCULATOR MODULE PART1

x = input("What is X? ")
y = input("What is Y? ")
#which is the correct number
#z = x + y 
z = int(x) + int(y)
print(z)

# you cn put a function inside a function, this is called nesting functions
a = int(input("What is X? "))
b = int(input("What is Y? "))

# the same but using float for decimal numbers
a = float(input("What is X? "))
b = float(input("What is Y? "))

#you can do all of it in one line but is not recommended because it is hard to read and understand
print(int(input("What is X? ")) + int(input("What is Y? ")))


#how to round to the nearest whole number
z = round(a + b)
print(z)

#rounding to a specific number of decimal places
x = 3.14159
y = 2.71828
#round to 2 decimal places
z = round(x + y, 2)
print(z) # Output: 5.86 


#formating the string to show a comma in the number
x = 1000000
print(f"{x:,}")
"""
Applying the Rule: The algorithm checks the type of x (an integer in this case), converts the number into its digit representation,
and scans the digits from right to left, automatically inserting a comma after every 3 consecutive digits.

"""
print(f"{x:_}")  # Output: 1_000_000
y = 1000000.5
print(f"{y:,.2f}")  # Output: 1,000,000.50
z = 42
print(f"{z:05d}")  # Output: 00042

#-----------------------------------------------------------------------------------------
#SYNTAX MODULE PART2

#creating a function to say hello many times "def" Keywords short for definition.
# It tells Python you are creating a custom function. 
#"hello"The name you gave to this function."()"opens and closes the parameter list (what the function accepts as input). 
# ":" The colon signals the start of the function's code block (everything indented under this belongs to hello)
def hello():
    print("Hello")

name =input("What is your name?")
hello()
print (name) 
# that is a bit stupid as it will print Hello \n "name"
# to assign something to it "to" became a parameter
def hello(to):
    print("Hello",to)

name =input("What is your name?")
hello() 
print (name) 

#printing a welcome message then calling the function 
def hello(to = "users"):
    print ("Hello,", to)

hello()
name = input("What is your name?") #cuz In Python, indentation (leading whitespace) defines scope and code structure. 
#Unlike languages like C, C++, or Java that use curly braces {} to group code, Python relies entirely on spacing.
hello(name)

#define a main function that includes more than one function
def main():
    name = input("What's your name?")
    hello()

def hello():
    print("hello,", name )
    
main()
#----------------------------------------------------------------------------------------------------------------------------
#CALCULATOR MODULE PART2

#explaining the return function 
def main():
    x = int(input("What is the value of x?"))
    print("the value of x squared is", square(x))



def square(n):
    return n * n # that means n multiplied by n which is the square 
#however we can use a .py function for the power called pow(number, power) or ** like number ** power


main()


# ==============================================================================
# Author: Antonious Adel Samir
# Track: Python Learning Journey | AI & Data Science
# File: 01_syntax_and_basics.py
# Description: Python syntax and fundamentals including strings, type casting,
#              formatting, functions, and basic input/output.
# License: MIT License - Open for educational and reference purposes.
# ==============================================================================


# ============================================================
# 1. SYNTAX MODULE - PART 1
# ============================================================

# Basic input and output
name = input("What is your name? ")
print("Hello,", name)


# Comments
# Single-line comments use the hash symbol: #

"""
Multi-line comments/docstrings
can be written using triple quotes.
"""


# ------------------------------------------------------------
# Print examples
# ------------------------------------------------------------

print("Hello, \"friend\"")
print('Hello,"friend"')
print("Hello,", end="")  # Prevents a new line
print(f"Hello, {name}")


# ------------------------------------------------------------
# String methods
# ------------------------------------------------------------

# Remove whitespace from the beginning and end
name = name.strip()

# Remove whitespace from the beginning only
name = name.lstrip()

# Remove whitespace from the end only
name = name.rstrip()

# Capitalize the first letter
name = name.capitalize()

# Capitalize the first letter of each word
name = name.title()

# Strip whitespace and capitalize each word
name = name.strip().title()

# Methods can be chained together
name = input("What is your name? ").strip().title()


# Split a name into first and last name
first_name, last_name = name.split()
print(f"Hello, {first_name}")


# ============================================================
# 2. CALCULATOR MODULE - PART 1
# ============================================================

# input() returns a string, so we need type casting
x = input("What is X? ")
y = input("What is Y? ")

# x + y would concatenate the strings
z = int(x) + int(y)
print(z)


# ------------------------------------------------------------
# Nested functions
# ------------------------------------------------------------

# A function can be used inside another function
a = int(input("What is X? "))
b = int(input("What is Y? "))


# ------------------------------------------------------------
# Floating-point numbers
# ------------------------------------------------------------

# Use float() when working with decimal numbers
a = float(input("What is X? "))
b = float(input("What is Y? "))


# You can write it in one line, but this is harder to read
print(int(input("What is X? ")) + int(input("What is Y? ")))


# ------------------------------------------------------------
# Rounding numbers
# ------------------------------------------------------------

# Round to the nearest whole number
z = round(a + b)
print(z)


# Round to a specific number of decimal places
x = 3.14159
y = 2.71828

z = round(x + y, 2)
print(z)  # Output: 5.86


# ------------------------------------------------------------
# Number formatting
# ------------------------------------------------------------

# Format large numbers with commas
x = 1000000
print(f"{x:,}")  # Output: 1,000,000

# Use underscores as digit separators
print(f"{x:_}")  # Output: 1_000_000

# Format a floating-point number to 2 decimal places
y = 1000000.5
print(f"{y:,.2f}")  # Output: 1,000,000.50

# Add leading zeros
z = 42
print(f"{z:05d}")  # Output: 00042


# ============================================================
# 3. SYNTAX MODULE - PART 2
# ============================================================

# ------------------------------------------------------------
# Creating a function
# ------------------------------------------------------------

# "def" is used to define a custom function.
# The function body must be indented.

def hello():
    print("Hello")


hello()


# ------------------------------------------------------------
# Function parameters
# ------------------------------------------------------------

def hello(to):
    print("Hello,", to)


name = input("What is your name? ")
hello(name)


# ------------------------------------------------------------
# Default parameters
# ------------------------------------------------------------

def hello(to="user"):
    print("Hello,", to)


hello()  # Uses the default value

name = input("What is your name? ")
hello(name)  # Uses the provided value


# ------------------------------------------------------------
# main() function and scope
# ------------------------------------------------------------

def main():
    name = input("What's your name? ")
    hello(name)


def hello(name):
    print("Hello,", name)


main()


# ============================================================
# 4. CALCULATOR MODULE - PART 2
# ============================================================

# ------------------------------------------------------------
# Using return
# ------------------------------------------------------------

def main():
    x = int(input("What is the value of x? "))
    print("The value of x squared is", square(x))


def square(n):
    # return sends the calculated value back to the caller
    return n * n


# You can also calculate powers using:
# pow(number, power)
# or:
# number ** power


main()


# ============================================================
# 5. PRACTICE
# ============================================================

# Try these exercises yourself:
#
# 1. Ask the user for their name and print a welcome message.
# 2. Ask for two numbers and calculate their average.
# 3. Create a function that calculates the cube of a number.
# 4. Create a function that takes a name and prints "Hello, <name>".
# 5. Ask for a number and print it formatted with commas.

# ==============================================================================
# Author: Antonious Adel Samir
# Track: AI & Data Science Diploma | CS50P Fundamentals
# File: 02_conditions, comparisons, Some Boolean logic.py
# Description: Notes and code examples exploring string manipulation, 
#              type casting, formatting, basic functions, and control flow.
# License: MIT License - Open for educational and reference purposes.
# ==============================================================================

#CONDITIONS "IF" MODULE PART1
#First condition is IF statement and it explicitly compares the a variable or a string or whatever to anoter variable or intiger or whatever
#for example here is a code that compares the scores to an integer and outputs the grade 
#and if the condition true it will output that and if not, in code words "elif" which is else if it will check and so on 

score = int(input("score:"))

if 90 <= score and score <= 100: #you can make it shorter like $if 90 <= score <= 100
    print ("grade is A") #i have to make sure that there is an indentation
elif score >= 80 and score < 90 :
    print ("grade is B")
elif score >=70 and score <80 :
    print ("grade is C")
elif score >=60 and score <70 :
    print ("grade is D")
else:                           #if any of the previous conditions does have not met 
    print ("grade is F antastic")

#-----------------------------------------------------------------------------------------
#CONDITIONS "IF" MODULE PART2

#comparison 
#as i can use if to compare the value and if true it will do the code after the indentation 

x = int(input("what the value of x"))
y = int(input("what the value of y"))

if x > y :
    print("x is greater than y")

elif y > x :
    print ("y is greater than x")

else : #which explicitly says if x not greater than y and not smaller than y
    print ("y is equal to x")

name = input ("what's your name? \n")

#-----------------------------------------------------------------------------------------
#CONDITIONS "IF" MODULE PART3
#let us use a defined main function that we discussed in the previous lesson 
#and we wanna identify the input integer if it is even or odd

#using only if conditions 
x = int(input("what is x?"))
if x % 2==0:          #which means that if the remainder equal to zero 
    print("even")
else:
    print("odd")


#using def and if 

def main():
    x = int (input("what is X?"))
    if is_even(x):
        print ("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0 :
        return True
    else:
        return False 


main()

""""
instead of writing 

def is_even(n):
    if n % 2 == 0 :
        return True
    else:
    return False 

you can simply write 
def is_even(n):
    return True if n % 2 == 0 else False 


"""

#-----------------------------------------------------------------------------------------
#CONDITIONS "IF" MODULE PART4

#here is a simple code that takes the name and output the house 


name = input ("what's your name? \n") #\n means new line as if you run this code it will take the input from a new line 

if name =="Harry":
    print ("Gryffindor")
elif name =="Hermione":
    print ("Gryfindor")
elif name == "Ron":
    print ("Gryfindor")
elif name == "Draco":
    print ("Stytherin")
else:
    print ("Who?") 


#Or you can write it all in one statement so the code will be more compactly

name = input ("what's your name? \n")

if name =="Harry" or name == "Hermione" or name == "Ron":
    print ("Gryffindor")
elif name == "Draco":
    print ("Stytherin")
else:
    print ("Who?")



#BUT another technique is called "MATCH" will allow you to express the idea more compactly 

name = input ("what's your name? \n")

match name:
    case "Harry":
        print ("Gryffindor")
    case "Hermione":
        print ("Gryfindor")
    case "Ron":
        print ("Gryfindor")
    case "Draco":
        print ("Stytherin")
    case _: # the " _" means for any case has not yet been handled "make sure to leave space between the "_" and "case" "
        print ("who")


#also we can make it more compactly

name = input ("what's your name? \n")

match name:
    case "Harry" | "Hermione" | "Ron": #using vertical bar which means or
        print("Gryfindor")
    case "Draco":
        print("Stytherin")
    case _:
        print("Who?")


# ============================================================
# 5. PRACTICE
# ============================================================

# 1. Ask the user for a number and determine whether it is
#    positive, negative, or zero.

# 2. Ask the user for their age and determine whether they
#    are a child, teenager, or adult.

# 3. Ask for two numbers and determine which one is larger.

# 4. Create a function called is_positive() that returns
#    True if a number is positive and False otherwise.

# 5. Create a simple menu using match.
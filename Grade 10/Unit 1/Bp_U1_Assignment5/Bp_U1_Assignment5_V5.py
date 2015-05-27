"""
Name: Basil
Class: ICS201-01
Date: 10/02/14
Assignment 5
"""

#Imports libraries
import math, random

#Asks user for a number and saves it to variable a
a = input("Enter a number")

print "Rounded down integer", math.floor(a)
print "Rounded up integer", math.ceil(a)

"""
1. The math.floor() command tells it to round down to the nearest float, the
   math.ceil() command tells it to round up to the nearest float
2. It has to be a number, not a string
3. The return value is a floating point number
"""

################################################################################

#Asks for two numbers and saves them to variables a and b
a = input("Enter a number")
b = input("Enter another number")

#Prints absolute value of both numbers
print "The absolute value of the first number is", math.fabs(a)
print "The absolute value of the second number is", math.fabs(b)

#Prints the numbers converted to radians
print "The first number, in radians is:", math.radians(a)
print "The second number, in radians is:", math.radians(b)

################################################################################
import random
#Asks user for two numbers and stores them in variables a & b
a = input("Enter a number")
b = input("Enter another number")

#Prints a random integer between the two numbers given
print random.randint(a, b)

#Prints a random float between 0.0 and 1.0
print random.random()

#Prints a float between the two parameters
print random.uniform(a, b)

"""
1. What do they do?
    They find random integers and floats in between given numbers
2. What data type does the parameter have to be?
    An integer or a float
3. What data type is the return value?
    An integer or float
"""

################################################################################

#Imports the library 'String'
import string

#Prints out all ASCII characters that are considered puncuation
print string.punctuation

#Prints all characters considered uppercase
print string.uppercase

#Prints all characters considered lowercase
print string.lowercase

"""
I used this in the Password Generator program to randomize all of the
ASCII characters for the password to be created
"""

################################################################################

x=input("Enter a Number")
y=input("Enter a Second Number")

print "The sum is", x+y
print "The difference is", x-y
print "The average is", x+y/2
print "The maximum is", max (x, y)
print "The minimum is", min (x, y)
print "The distance is", abs (x-y)
print "The square is", x+y**2
print "The cube is", x+y**3
print "The fourth power is", x+y**4
print "The absolute values are", abs(x), "&", abs(y)
print "The modulus is", divmod(x, y)
print "The first number to the power of the second number is", pow(x, y)
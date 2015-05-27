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
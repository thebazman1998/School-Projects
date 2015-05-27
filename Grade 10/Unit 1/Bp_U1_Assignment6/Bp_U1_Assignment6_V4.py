"""
Name: Basil
Class: ICS201-01
Date: 18/02/14
Assignment 6
"""

################################################################################

def repeat( param ):
    print param, param

#main
word = raw_input("Please enter a word")
repeat(word)

"""
This program just prints out a word that you enter twice with a space in between
"""

################################################################################

def clearScreen():
    print "\n" * 26

#main
print "Hello World"
clearScreen()

################################################################################

def repeat( param, numTimes ):
    print param * numTimes

#main
word = raw_input("Please enter a word")
times = input("Please enter a number")
repeat(word, times)

################################################################################

"""
Because python interprets the code one line at a time, you must put the method
definition before the method call
"""

################################################################################

def printNameBox(someString):
    dashes = "-" * len(name)
    horizontalLines = "+" + dashes + "+"
    middleLine = "|" + name + "|"
    print horizontalLines, "\n", middleLine, "\n", horizontalLines

#main
name = raw_input("Please enter your name")
printNameBox(name)

################################################################################

import random

def stars(numTimes):
    print numTimes * "*"

#main
for i in range(0, 20):
    numStars = random.randint(1, 10)
    stars(numStars)
    
################################################################################

import math

radius = input("Please enter the radius")
radius = radius * 1.0

areaOfCircle = math.pi * radius ** 2
volumeOfSphere = (4/3) * math.pi * radius ** 3

print "The radius is:", radius
print "The area of the circle is:", areaOfCircle
print "The Volume of the sphere is:", volumeOfSphere

################################################################################

def tax( item_price, tax_rate ):
    print "Subtotal:", item_price
    tax_amount = item_price * tax_rate
    print "Tax:", tax_amount
    total_price = tax_amount + item_price
    print "Total:", total_price

item_price = input("Enter the item price, in dollars")
tax_rate = input("Enter the tax rate, in decimal form")
tax(item_price, tax_rate)

################################################################################

def fahrenheit_to_celcius( temp ):
    c = (5/9) * (temp - 32)
    c = round(c, 0)
    print "The temperature, in Celcius, is", c

def celcius_to_fahrenheit( temp ):
    f = (temp * 9/5) + 32
    f = round(f, 0)
    print "The temperature, in Fahrenheit, is", f

temp1 = input("Enter a temperature to convert to Fahrenheit")
celcius_to_fahrenheit(temp1)
555
temp2 = input("Enter a temperature to convert to Celcius")
fahrenheit_to_celcius(temp2)

################################################################################
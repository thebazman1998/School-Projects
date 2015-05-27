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
numStars = random.randint(1, 10)
stars(numStars)
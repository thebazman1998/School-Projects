"""
Name: Basil
Class: ICS201-01
Date: 19/02/14
Assignment 7
"""

def compare( x, y ):
    if x < y:
        print x, "is less than", y
        
    elif x > y:
        print x, "is greater than", y
        
    else:
        print x, "and", y, "are equal"

################################################################################

def isVowel( character ):
    if character == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
        print character, "is a vowel"
    elif character == "y" or "Y":
        print character, "is sometimes a vowel"
    else:
        print character, "is a consonant"

################################################################################

def isDivisibleBy3( n ):
    if n % 3 == 0:
        print n,"is divisible by 3"
    else:
        print n, "is not divisible by 3"

################################################################################

def weight_class( n ):
    
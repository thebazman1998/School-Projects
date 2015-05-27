'''
Name: Basil
Class: ICS201-01
Date: 04/02/14
Assignment 4
'''

#Imports libraries
import random, string, os

#Define variables
small = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "^!\$%&/()=?{[]}+~#-_.:,;<>|\\"
characters = string.ascii_letters + string.punctuation + string.digits

print string.ascii_letters
print string.digits
print string.punctuation
print characters
print small + nums + big + special

#Random Password Generation
password = random.choice(characters)
while len(password) != 21:
    password = password + random.choice(characters)
    
#Display password
print "Your password is:", password
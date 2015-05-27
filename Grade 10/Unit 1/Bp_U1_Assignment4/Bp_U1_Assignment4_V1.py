'''
Name: Basil
Class: ICS201-01
Date: 04/02/14
Assignment 4
'''

import random

firstName = raw_input("Enter your first name")

#Chooses first 4 digits randomly from firstName variable
a = random.choice(firstName)
b = random.choice(firstName)
c = random.choice(firstName)
d = random.choice(firstName)

last4digits = "123456789"

#Chooses last 4 digits randomly from 1-9
e = random.choice (last4digits)
f = random.choice (last4digits)
g = random.choice (last4digits)
h = random.choice (last4digits)

password = a+b+c+d+e+f+g+h
print password
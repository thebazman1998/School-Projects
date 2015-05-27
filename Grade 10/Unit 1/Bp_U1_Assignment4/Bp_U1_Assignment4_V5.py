'''
Name: Basil
Class: ICS201-01
Date: 04/02/14
Assignment 4
'''

#Imports libraries
import random, string, os

#Define variable
characters = string.ascii_letters + string.punctuation + string.digits

print string.ascii_letters
print string.digits
print string.punctuation
print characters

#Random Password Generation
password = random.choice(characters)
while len(password) != 21:
    password = password + random.choice(characters)
    
#Display password
print "Your password is:", password\

Quit = "a"
while Quit != "quit":
    Quit = raw_input("Type quit to quit program")
    Quit = Quit.lower()

"""
Questions
1 - How does the random module work? What does it do? Give some examples
        It selects random characters from the list/variable you feed it using 
        psuedo-random number generators. It is used for things like creating a
        random pass-word or username, or rolling a die.
2 - What does the string module do? What is a string?
        It is a database of pre-made strings, a combination of characters that
        are not used for adding, multiplying, etc.
3 - Why were they so important in this assignment?
        The random library was necessary to randomize the password, and the
        string library saved time so that instead of typing all of the
        characters out, it already had them in strings.
"""

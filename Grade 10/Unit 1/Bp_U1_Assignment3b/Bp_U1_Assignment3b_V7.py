"""
Name: Basil
Class: ICS201-01
Date: 11/02/14
Assignment 3a
"""

################################################################################

#OS Module

#Imports libraries
import os
import subprocess

#Prints out all functions in the OS library
for a in dir(os): print a

#Prints your CWD
print "Your present working directory is", os.getcwd()

#Saves your CWD in variable directory in lowercase
directory = os.getcwd()
directory = directory.lower()

#Asks if you would like to open the directory and waits for yes or no
option1 = raw_input("Would you like to open this directory?")
option1 = option1.lower()
while type(option1) == type("s"):

#If option1 == yes, sets variable option1 to 1
        if option1 == "yes":
                option1 = 1
                
#If option1 == no, sets variable option1 to 0
        elif option1 == "no":
                option1 = 0
                
#If option one doesn't equal either of those, asks user to retype answer
        else:
                option1 = raw_input("Please retype answer")

#If option1 == 1, opens CWD in Windows Explorer
if option1 == 1:
        subprocess.Popen('explorer "{0}"'.format(directory))
        
#If not, prints out "Okay"
else:
        print "Okay"
        
################################################################################

#Pygame Module

#Imports pygame library
import pygame

#Prints all functions in pygame library
for i in dir(pygame): print i

#Saves pygame version to variable pygame_Version
pygame_Version = pygame.version.ver

#Checks if pygame is up to date
if pygame.version.vernum < (1, 9, 2,):

#If pygame is not up to date, asks user to update pygame
        print "Warning: older version of pygame detected, please update."
        
#If pygame is up to date, tells user that there is no need for an update
else:
        print "Your have the newest version of pygame,", pygame_Version

################################################################################

#Math Module

import math
for i in dir(math): print i

while quit != "quit":
        quit = raw_input("Type quit to quit the program")
        quit = quit.lower()
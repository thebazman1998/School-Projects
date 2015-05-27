"""
Name: Basil
Class: ICS201-01
Date: 11/02/14
Assignment 3a
"""

################################################################################

#OS Module

import os
for i in dir(os): print i

print "Your present working directory is", os.getcwd()

option1 = raw_input("Would you like to open this directory?")
while type(option1) == type("ksjdfh"):
        if option1 = yes or Yes:
                option1 = 1
        elif option1 = no or No:
                option1 = 0
        else:
                option1 = raw_input("Please retype answer")


if option1 = 1:
        open os.getcwd()

################################################################################

#Pygame Module

import pygame

pygame_Version = pygame.version.ver

if pygame.version.vernum < (1, 9, 2,):
    print "Warning: older version of pygame detected, please update."
else:
    print "Your have the newest version of pygame,", pygame_Version

for i in dir(pygame): print i
################################################################################

#Math Module

import math
for i in dir(math): print i


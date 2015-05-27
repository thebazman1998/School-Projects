"""
Name: Basil
Class: ICS201
Date: 01/04/14
Assignment 4
"""

import random, pygame

# Menu Code
def menu():
    menu_choice = raw_input("Which program would you like to run?\n>> ")
    
    if "1" in menu_choice:
        question1()
    elif "2" in menu_choice:
        question2()
    elif "3" in menu_choice:
        question3()
    elif "4" in menu_choice:
        question4()
    elif "5" in menu_choice:
        question5()
    else:
        menu()

# Questions
def question1():
    for i in range(0, 6):
        print "*" * random.randint(0, 26)

def question2():
    word = raw_input("Enter a word\n>> ")
    for i in word:
        print i

def question3():
    pass

def question4():
    pass

def question5():
    pass





menu()
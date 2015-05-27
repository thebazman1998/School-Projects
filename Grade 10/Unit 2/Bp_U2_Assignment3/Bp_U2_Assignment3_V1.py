"""
Name: Basil
Class: ICS201-01
Date: 27/03/14
Unit 2 Assignment 3
"""

import time

# Methods

def wait(num):# Easier to type & easier to understand wait(#) rather than time.sleep(#)
    time.sleep(num)

def question1():
    done = False
    while done == False:
        print "Have a good day"
        wait(0.5)
        cont = raw_input("Type more to continue\n>> ")
        if cont == "more":
            pass
        else:
            print "Done"
            wait(0.5)
            break

def question2():
    pass

def question3():
    pass

def question4():
    pass

def question5():
    pass

def question6():
    pass

def question7():
    pass

def question8():
    pass

def question9():
    pass

# Menu Code
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
elif "6" in menu_choice:
    question6()
elif "7" in menu_choice:
    question7()
elif "8" in menu_choice:
    question8()
elif "9" in menu_choice:
    question9()
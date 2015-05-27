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
    # Set variable 'done' to False
    done = False
    
    # Function loop
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
    # Define variables
    end = False
    x = 0
    
    # Function loop
    while end == False:
        new_word = raw_input("Enter a word - Typing 'end' will count and display total # of words\n>> ")
        if new_word == "end":
            return x
        else:
            x += 1

def question3():
    # Set variable 'done' to False
    done = False
    num_of_num = 0
    total_num = 0
    
    # Function loop
    while done == False:
        new_num = input("Enter a number - (-1) will print out the average")
        if new_num != -1:
            total_num += new_num
            num_of_num += 1
        else:
            avg_num = (total_num * 1.0) / num_of_num
            return avg_num

def question4():
    count_to = 0
    count_by = 0
    
    for i in range(count_to, 100, count_by):
        return i

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
    print question2()
elif "3" in menu_choice:
    print question3()
elif "4" in menu_choice:
    print question4()
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
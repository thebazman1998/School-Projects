"""
Name: Basil
Class: ICS201-01
Date: 31/03/14
Unit 2 Assignment 3
"""

import time
import random

# Methods

# Menu Code
def menu():
    menu_choice = raw_input("Which program would you like to run?\n>> ")
    
    if "1" in menu_choice:
        question1()
    elif "2" in menu_choice:
        print question2()
    elif "3" in menu_choice:
        print question3()
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
    else:
        menu()

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
            wait(0.5)
        else:
            avg_num = (total_num * 1.0) / num_of_num
            wait(0.5)
            return avg_num

def question4():
    count_to = input("Please enter the number to count down from 100 to\n>> ")
    count_by = input("Please enter the number to count down by\n>> ")
    count_by = count_by * -1
    
    for i in range(100, count_to, count_by):
        print i
        wait(0.5)

def question5():
    print "Rolling die..."
    wait(0.5)
    first_roll = random.randint(1, 6)
    print "Your first roll is:", first_roll
    next_roll = 0
    count = 0
    wait(0.5)
    
    while next_roll != first_roll:
        next_roll = random.randint(1, 6)
        print "Rolling die..."
        wait(0.5)
        print next_roll
        count += 1
    
    print "It took you", count, "roll(s) to get a", first_roll, "again"

def question6():
    # Asks user for a desired sum and stores it in 'sum_of_dice' variable
    sum_of_dice = input("Please enter a desired dice sum\n>> ")
    
    # Makes sure 'sum_of_dice' is a valid sum
    while sum_of_dice not in range(2,12):
        sum_of_dice = input("The sum must be in between two and twelve\n>> ")
    
    die1 = 0
    die2 = 0
    counter = 0
    while die1 + die2 != sum_of_dice:
        print "Try", counter
        
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die1_and_die2 = die1 + die2
        counter += 1
        
        print "Rolling dice..."
        wait(0.5)
        print "First die:", die1, "Second die:", die2, "Sum:", die1_and_die2
        wait(0.5)
        
def question7():
    
    play_again = True
    
    while play_again == True:
        answer = random.randint(1, 100)
        guess = guess = input("Guess a number between 1 and 100\n>> ")
        counter = 1
        
        while guess != answer:
            counter += 1
            
            if guess > answer:
                guess = input("Guess lower\n>> ")
                
            if guess < answer:
                    guess = input("Guess higher\n>> ")
                    
        print "Good job! It took you", counter, "tries."
        
        play_again = raw_input("Would you like to play again?\n>> ")
        if "y" in play_again:
            play_again = True
        else:
            play_again = False

def question8():
    pass

def question9():
    pass

menu()
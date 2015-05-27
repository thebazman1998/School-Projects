"""
Name: Basil
Class: ICS201-01
Date: 17/03/14
Unit 2 Assignment 1
"""

import time

def one_to_one_thousand(num):
    
    answer = num
    
    while answer <= 1000:
        print answer
        answer += num

def multiple_table(num):
    for i in range(0, 13):
        print num, "x", i, "=", num * i

def powers_of(num):
    for i in range(0, 13):
        print num, "^", i, "=", num ** i

def num_sum_and_avg():
    
    num_of_num = input("Please enter the number of numbers.\n>> ")
    total = 0
    
    for a in range(0, num_of_num):
        num = input("Please enter a number.\n>> ")
        total += num
        
    avg = total / num_of_num
        
    total = str(total)
    avg = str(avg)
    
    string = "The sum of the numbers is: " + total + "\nThe average of the numbers is: " + avg
    return string

def one_to_one_hundred():
    total = 0
    for i in range(1, 100):
        total += i
    return total

def range_sum():
    x = input("Enter the low end of the range.\n>> ")
    y = input("Enter the high end of the range.\n>> ")
    
    total = 0
    
    for i in range(x, y):
        total += i
    return total

def cd_from_ten():
    for i in range(10, -1, -1):
        print i
        time.sleep(0.5) #time.sleep only works when you run the program out of IDLE
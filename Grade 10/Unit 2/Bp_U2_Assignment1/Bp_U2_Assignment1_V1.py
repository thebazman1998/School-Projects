"""
Name: Basil
Class: ICS201-01
Date: 05/03/14
Unit 2 Assignment 1
"""

def one_to_one_thousand(num):
    
    answer = num
    
    while answer <= 1000:
        print answer
        answer = answer + num

def multiple_table(num):
    print "1 *", num, "=", 1 * num
    print "2 *", num, "=", 2 * num
    print "3 *", num, "=", 3 * num
    print "4 *", num, "=", 4 * num
    print "5 *", num, "=", 5 * num
    print "6 *", num, "=", 6 * num
    print "7 *", num, "=", 7 * num
    print "8 *", num, "=", 8 * num
    print "9 *", num, "=", 9 * num
    print "10 *", num, "=", 10 * num
    print "11 *", num, "=", 11 * num
    print "12 *", num, "=", 12 * num

def powers_of(num):
    print num, "^ 0 =", num ** 0
    print num, "^ 1 =", num ** 1
    print num, "^ 2 =", num ** 2
    print num, "^ 3 =", num ** 3
    print num, "^ 4 =", num ** 4
    print num, "^ 5 =", num ** 5
    print num, "^ 6 =", num ** 6
    print num, "^ 7 =", num ** 7
    print num, "^ 8 =", num ** 8
    print num, "^ 9 =", num ** 9
    print num, "^ 10 =", num ** 10
    print num, "^ 11 =", num ** 11
    print num, "^ 12 =", num ** 12

def num_add():
    
    num_of_num = input("Please enter the number of numbers.\n>>")
    total = 0
    
    for a in range(0, num_of_num):
        num = input("Please enter a number.\n>> ")
        total = total + num
    
    total = str(total)
    
    string = "The sum of the numbers is: " + total
    return string
print num_add()
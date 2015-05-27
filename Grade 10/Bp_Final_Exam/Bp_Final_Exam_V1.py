'''
Created on Jun 24, 2014

@author: Basil

Final Exam
'''

def menu():
    choice = input('Which program would you like to run? (1-3, -1 for quit)\n>> ')
    if choice == 1:
        question1()
        menu()
    if choice == 2:
        question2()
        menu()
    if choice == 3:
        question3()
        menu()

def question1():
    string1 = raw_input('Please enter a word.\n>> ')
    string2 = raw_input('Please enter another word.\n>> ')
    count = 0
    
    if len(string1) > len(string2):
        stringbig = len(string1)
    else:
        stringbig = len(string2)
    
    for i in range(0, stringbig - 1):
        if string1[i : i + 2] == string2[i : i + 2]:
            count += 1
    print count

def question2():
    numbers= input('Please enter an array.\n>> ')
    
    if numbers == (6):
        print 'true'
        return True
    
    lennum = len(numbers) - 1
    
    if numbers[0] == 6 or numbers[lennum] == 6:
        print 'true'
        return True
    else:
        print 'false'
        return False

def question3():
    num1 = input('Please enter a number\n>> ')
    num2 = input('Please enter another number\n>> ')
    num3 = input('Please enter a third number\n>> ')
    
    if num1 == 13:
        sumnum = 0
    elif num2 == 13:
        sumnum = num1
    elif num3 == 13:
        sumnum = num1 + num2
    else:
        sumnum = num1 + num2 + num3
    print sumnum

menu()
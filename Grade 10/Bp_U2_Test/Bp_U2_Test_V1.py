'''
Created on Apr 29, 2014

@author: Basil
'''

def menu():
    menu_choice = raw_input('Would you like to view the Communication, Application, or Thinking section?\n>> ')
    menu_choice = menu_choice.lower()
    
    if menu_choice == 'communication':
        communication()
        
    elif menu_choice == 'application':
        application()
    
    elif menu_choice == 'thinking':
        thinking()
        
def communication():
    print 'Explain the types of loops available in python. Give an example of each.'
    print '    While loop: loops the piece of code until the logic is false.'
    print '        If not sure when loop is going to end, or if waiting for user input (such as in a game) a while loop would be appropriate.'
    print '    For loop: loops the piece of code a certain amount.'
    print '        If the loop is going to run a predeterminimum_numed amount of times, like when using a counter, a for loop is appropriate.'
    menu()

def application():
    x = input('Which question would you like to view (1-4)?\n>> ')
    if x == 1:
        maximum_num_minimum_num_set = False
        total = 0
        for i in range(0, 20):
            num = float(input('Please enter a decimal.\n>> '))
            
            total += num
            
            if maximum_num_minimum_num_set == False:
                minimum_num = num
                maximum_num = num
            
            if num > maximum_num:
                maximum_num = num
            
            if num < minimum_num:
                minimum_num = num
            
            maximum_num_minimum_num_set = True
        
        avg = total / 20.0
        
        print 'The sum is:', total
        print 'The average is:', avg
        print 'The maximum is:', maximum_num
        print 'The minimum is:', minimum_num
    
    if x == 2:
        for i in range(200, 0, -2):
            print i
    
    if x == 3:
        num = input('Please enter a positive number\n>> ')
        min = num
        max = num
        
        while num > 0:
            num = input('Please enter another number (enter a negative value to quit and display values)\n>> ')
        
            if num < 0:
                break
        
            if num > max:
                max = num
        
            if num < min:
                min = num
            
        print 'The maximum is:', max
        print 'The minimum is:', min
    
    if x == 4:
        for i in range(0, 7):
            space = (7 - i) * ' '
            star = i * '*'
            println = space + star
            print println
            
        for i in range(7, 0, -1):
            space = (7 - i) * ' '
            star = i * '*'
            println = space + star
            print println
            
def thinking():
    num = input('Please enter a positive number.\n>> ')
    divisors = []
    counter = 0
    total = 0
    for i in range(1, num):
        remainder = num % i
        if remainder == 0:
            divisors.append(i)
            counter += 1
            
    for i in range(0, len(divisors)):
        total += divisors[i]
        
    if total == num:
        print 'This is a perfect number'
    else:
        print 'This is not a perfect number'

#Main
menu()
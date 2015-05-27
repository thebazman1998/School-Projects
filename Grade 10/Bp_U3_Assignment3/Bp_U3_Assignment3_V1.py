'''
Created on May 21, 2014

@author: Basil
'''

def menu():
    choice = raw_input('Which program would you like to run? Options are 1, 3, and 9. Type end to quit.\n>> ')
    
    if choice == '1':
        question1()
        menu()
    elif choice == '3':
        question3()
        menu()
    elif choice == '9':
        question9()
        menu()
    elif choice != 'end':
        menu()

def question1():
    first_name = raw_input('Please enter your first name. Type end to quit.\n>> ')
    
    if first_name == 'end':
        menu()
    
    middle_name = raw_input('Please enter your middle name. Type end to quit.\n>> ')
    
    if middle_name == 'end':
        menu()
    
    last_name = raw_input('Please enter your last name. Type end to quit.\n>> ')
    
    if last_name == 'end':
        menu()
    
    full_name = [first_name, middle_name, last_name]
    
    print full_name[0]
    print ' ' * 20 + full_name[1]
    print ' ' * 40 + full_name[2]

def question3():
    done = False
    list1 = []
    
    while not done:
        item = raw_input('Enter an item to be added to list1. Type end to finish.\n>> ')
        if item == 'end':
            done = True
        else:
            list1.append(item)
    print list1

def question9():
    items = ['Pencil', 'Paper', 'Eraser', 'Binder', 'Stapler', 'Pen']
    prices = [1.99, 0.99, 1.79, 5.99, 13.89, 1.99]
    done = False
    
    while not done:
        choice = input('The list of items is:\n1. Pencil\n2. Paper\n3. Eraser\n4. Binder\n5. Stapler\n6. Pen\nWhich item would you like to know the price of? Type -1 to quit.\n>> ')
        if choice == -1:
            done = True
        choice -= 1
        
        print 'The', items[choice], 'costs', prices[choice]

menu()
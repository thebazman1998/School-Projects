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
    user_input = 0
    total = user_input
    num_of_num = 0
    
    while user_input != "=":
        user_input = raw_input("Enter a number ('=' to exit)\n>> ")
        if user_input != "=":
            user_input = int(user_input)
            total += user_input
            num_of_num += 1
        else:
            break
    
    average = total / num_of_num
    
    print "The average is:", average

def question4():
    r = input("How big would you like the radius of the circles?\n>> ")
    pygame.init()
    
    # Set screen size
    size = [900, 600]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Bp_U2_Assignment4")
    
    # Draw functions go under this comment
    for i in range(0, 5):
        red = random.randint(32, 255)
        green = random.randint(32, 255)
        blue = random.randint(32, 255)
            
        color = (red, green, blue)
            
        pygame.draw.circle(screen, color, [random.randint(0, 900), random.randint(0, 600)], r)        
    # Draw functions go above this comment
    # Loop until the user clicks close
    done = False
    clock = pygame.time.Clock()
    
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Redifines done as True to exit loop
        pygame.display.flip()
    pygame.quit()    

def question5():
    word = raw_input("Enter a Word\n>> ")
    counter = len(word) -1
    for i in word:
        print word[counter]
        counter -= 1

menu()
"""
HALLWAY
VERSION 2
"""

import methods

def introHall(cut):
    print "---HALLWAY--- \n"
    print "You step through the door and find yourself in a short hallway."

    if cut == 1:
        print "You see a first-aid kit on the floor, and put a few bandages over your cuts."
    elif cut == 2:
        pass
    
    print "There is a door at the end. You take a closer look."
    print "Just like all of the other doors you have encountered, it is locked from the inside, but it seems to lead to the street!\n"
    print "\nYou see the door, a crystal chandelier, and a rug over the hardwood floor.\n"
    print "\nYou have unlocked a new command! Type 'move object' to move the object.\n"

def descHall():
    print "\nYou see the door, a crystal chandelier, and a rug over the hardwood floor.\n"

def playHall():
        
    rugMove = 0
    
    while rugMove == 0:

        command = raw_input(">> ")
        
        if command == "move rug" or command == "use rug":
            print "\nYou move the rug to reveal a long thin broom handle."
            print "\nObtained new item: Broom handle!\n"
        
        elif "chandelier" in command:
            print "\nThe chandelier is out of reach!"
            print "If only you had something to extend your reach...\n"
        
        elif command == "break rug":
            print "\nUnable to break rug.\n"
        
        elif "door" in command:
            print "\nThe door is locked tight, and you have no chance of breaking it.\n"
        
        elif command == "quit":
            
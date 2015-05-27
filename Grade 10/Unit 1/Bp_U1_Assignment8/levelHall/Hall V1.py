"""
HALLWAY
VERSION 1
"""

import methods

def introHall():
    print "\nYou step through the door and find yourself in a short hallway."
    print "There is a door at the end. You take a closer look."
    print "Just like all of the other doors you have encountered, it is locked from the inside, but it seems to lead to the street!\n"
    print "\nYou see the door, a crystal chandelier, and a rug over the hardwood floor.\n"
    print "\nYou have unlocked a new command!!! Type 'move object' to move the object.\n"

def playHall():
    
    command = raw_input(">> ")
    
    rugMove = 0
    
    while rugMove == 0:
        if command == "move rug":
            print "\nYou move the rug to reveal a long thin broom handle."
            print "\nObtained new item: Broom handle!\n"
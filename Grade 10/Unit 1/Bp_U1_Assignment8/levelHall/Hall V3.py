"""
HALLWAY
VERSION 3
"""

import methods

def Bp_introHall(cut):
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

def Bp_descHall(rug):
    if rug == 0:
        print "\nYou look around the hall and see the door, a crystal chandelier, and a rug over the hardwood floor.\n"
    elif rug == 1:
        print "\nYou look around the hall and see the door, a crystal chandelier, and rug half overturned, covering the hardwood floor.\n"

def Bp_playHall():
        
    rugMove = 0
    chandelier = 0
    
    while rugMove and chandelier == 0:

        command = raw_input(">> ")
        
        if command == "move rug" or command == "use rug":
            print "\nYou move the rug to reveal a long thin broom handle."
            print "\nObtained new item: Broomhandle!\n"
            rugMove = 1
        
        elif "chandelier" in command:
            print "\nThe chandelier is out of reach!"
            print "If only you had something to extend your reach...\n"
        
        elif command == "break rug":
            print "\nUnable to break rug.\n"
        
        elif "door" in command:
            print "\nThe door is locked tight, and you have no chance of breaking it.\n"
        
        elif command == "quit":
            methods.Ib_quitGame()
        
        elif command == "look":
            Bp_descHall(0)
        
        elif command == "help":
            methods.Ib_giveInstructions(2)
            
            
    while rugMove == 1 and chandelier == 0:
        
        command = raw_input(">> ")
        
        if command == "break chandelier" or command == "use broomhandle, chandelier":
            print "\nYou rustle the chandelier with the long broomhandle, and a key falls onto the hardwood floor!/n"
            print "\nNew item obtained: key!\n"
            chandelier = 1
        
        elif "door" in command:
            print "\nThe door is locked tight, and you have no chance of breaking it.\n"
        
        elif command == "quit":
            methods.Ib_quitGame()
        
        elif command == "look":
            Bp_descHall(1)
        
        elif command == "help":
            methods.Ib_giveInstructions(2)
    
    
    while rugMove == 1 and chandelier == 1:

        if command == "use key, door" or command == "unlock door":
            print "\nYou have escaped! Congatulations!\n"
            methods.Ib_key2continue(2)
            methods.Ib_gameOver()

        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "look":
            Bp_descHall(1)

        elif command == "help":
            methods.Ib_giveInstructions(2)
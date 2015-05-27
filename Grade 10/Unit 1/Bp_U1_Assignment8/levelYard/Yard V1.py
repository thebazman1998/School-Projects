"""
BACKYARD
VERSION 1
"""

import methods

def introYard():
    print "---BACKYARD--- \n"
    print "You climb out the window, and emerge with some cuts on your arms, legs and face."
    print "You don't want to try that again.\n"
    print "You discover that you are now in what appears to be a backyard."
    print "You see a lawnmower, a plugged-in hose, a dying garden, some long grass, and a locked sliding-door.\n"

def descYard():
    print "\nYou are in somebody's backyard."
    print "You can see a lawnmower, a plugged-in hose, a dying garden, some long grass, and a locked sliding-door leading into the house."

def playYard():
    
    endLevel = 0    
    mow = 0
    
    while mow == 0 and endLevel == 0: # While user has not mowed the grass and level is not over
        
        command = raw_input(">> ")
        
        if command == "open door":
            print "\nThe door is locked.\n"
        
        elif command == "unlock door" or command == "use key, door":
            print "\nYou don't have the key.\n"
        
        elif command == "break door":
            print "\nYou are too cut and tired after climbing out of the window to break the glass.\n"
        
        elif command == "use lawnmower, grass":
            print "\nYou proceed to mow the grass, only to find that the lawnmower doesn't start!\nYou decide to check to see if there is anything blocking the blades, and you find a medium sized rock. Hmm... this could be good for breaking something.\n"
            mow = 1 # User has now attempted to mow the grass.
            inventory = 1 # User now has rock in inventory.
            
        elif command == "use lawnmower, garden":
            print "\nYou proceed to mow the garden, only to find that the lawnmower doesn't start!\nYou decide to check to see if there is anything blocking the blades, and you find a medium sized rock. Hmm... this could be good for breaking something.\n"
            mow = 1 # User has now attempted to mow the garden.
            inventory = 1 # User now has rock in inventory.
        
        elif command == "use hose, garden" or command == "use hose, lawnmower" or command == "use hose, grass" or command == "use hose, door":
            print "\nNo water comes out.\n"
        
        elif command == "break hose" or command == "break lawnmower":
            print "\nIt is too strong to break.\n"
        
        elif command == "unlock lawnmower" or command == "unlock hose":
            print "\nThere is nothing to unlock!\n"
        
        elif command == "look":
            descYard()
        
        elif command == "inventory":
            print "\nYou are not carrying anything.\n"
        
        elif command == "help":
            methods.giveInstructions(1)
        
        elif command == "quit":
            methods.quitGame()
        
        else:
            print "\nEnter a valid command.\n"

    while endLevel == 0: # While level is not finished
    
        command = raw_input(">> ")

        if command == "break door" or command == "use rock, door":
            print "\nIt worked! The glass door is broken.\n"
            endLevel = 1
            # Third Level
        
        elif command == "open door":
            print "\nThe door is locked.\n"
    
        elif command == "unlock door":
            print "\nYou don't have the key.\n"
    
        elif command == "use lawnmower, grass" or command == "use lawnmower, garden":
            print "\nThe lawnmower isn't working"
    
        elif command == "use hose, garden" or command == "use hose, lawnmower" or command == "use hose, grass" or command == "use hose, door":
            print "\nNo water comes out.\n"
    
        elif command == "break hose" or command == "break lawnmower":
            print "\nIt is too strong to break.\n"
    
        elif command == "unlock lawnmower" or command == "unlock hose":
            print "\nThere is nothing to unlock!\n"
    
        elif command == "look":
            descYard()
    
        elif command == "inventory":
            print "\nYou are carrying a rock.\n"
    
        elif command == "help":
            methods.giveInstructions(1)
    
        elif command == "quit":
            methods.quitGame()

        else:
            print "\nEnter a valid command.\n"



introYard()
playYard()
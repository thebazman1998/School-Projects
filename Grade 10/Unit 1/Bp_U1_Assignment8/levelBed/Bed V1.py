def introBed():
    print "---BEDROOM--- \n"
    print "You wake up on a plain bed, in a small room."
    print "There is a chained-up door, a slightly-open window, and a cabinet.\n"
    print "As you get up from the bed, you turn around, and find that the bed disappeared!\n"
    print "Reminder: Usable commands are open, unlock, break, use, look, inventory, help, and quit.\n"

def descBed():
    print "\nYou are in a small room."
    print "There is a chained-up door, a slightly-opened window, and a cabinet.\n"

def playBed(): # Bedroom Level

    key = 0
    
    while key == 0: # While user doesnt have key, and level has not finished

        command = raw_input(">> ")
        
        if command == "open door":
            print "\nThe door is locked.\n"
            
        elif command == "open cabinet":
            print "\nYou found a key in the cabinet, it has been added to your inventory.\n"
            key = 1 # User has key in inventory

        elif command == "open window":
            print "\nYou try to open the window but it gets stuck.\n"

        elif command == "unlock door":
            print "\nYou cannot unlock the door without a key.\n"
        
        elif command == "unlock cabinet" or command == "unlock window":
            print "\nThere is nothing to unlock.\n"

        elif command == "break cabinet":
            print "\nBro, you don't even lift. No way you'll be able to do that!\n"

        elif command == "break door":
            print "\nYou aren't trained in breaching doors.\n"

        elif command == "break window":
            print "\nYou broke some dude's window...Congrats!"
            print "You climb out the window into the next room.\n"
            secondRoom(2) # Begin next level (no key obtained)

        elif command == "use cabinet, window" or command == "use cabinet, door":
            print "\nThe cabinet is too heavy to pick up.\n"

        elif command == "use window, cabinet" or command == "use window, door" or command == "use door, window" or command == "use door, cabinet":
            print "...What?"

        elif command == "look":
            descBed()

        elif command == "inventory":
            print "\nYou have nothing in your inventory.\n"

        elif command == "quit":
            methods.quitGame()

        elif command == "help":
            methods.clear(1)
            methods.giveInstructions(1)
        else:
            print "\nPlease use a valid command.\n"
    
    while key == 1: # While user has key in their inventory

        command = raw_input(">> ")

        if command == "unlock cabinet" or command == "unlock window":
            print "\nThere is nothing to unlock.\n"
        
        elif command == "unlock door" or command == "use key, door":
            print "\nYou unlocked the door with your key, and entered the next room.\n"
            print "You don't think you'll need the key later, so you leave it in the keyhole.\n"
            secondRoom(1) # Begin next level (key has been used)

        elif command == "use key, cabinet":
            print "\nYou scratch the cabinet with the key.\n"
        
        elif command == "use key, window":
            print "\nYou scratch the window with the key.\n"

        elif command == "use cabinet, window" or command == "use cabinet, door":
            print "\nThe cabinet is too heavy to pick up.\n"

        elif command == "use window, cabinet" or command == "use window, door" or command == "use door, window" or command == "use door, cabinet":
            print "...What?"

        elif command == "open door":
            print "\nThe door is locked, but the key you found looks like it might fit.\n"
        
        elif command == "open cabinet":
            print "\nThere is nothing left in the cabinet.\n"

        elif command == "open window":
            print "\nYou try to open the window but it gets stuck.\n"

        elif command == "break window":
            print "\nYou broke some dude's window...Congrats!"
            print "You climb out the window into the next room.\n"
            secondRoom(3) # Begin next level (with key)

        elif command == "break cabinet":
            print "\nBro, you don't even lift. No way you'll be able to do that.\n"

        elif command == "break door":
            print "\nYou aren't trained in breaching doors.\n"

        elif command == "look":
            descBed()

        elif command == "inventory":
            print "\nYou are carrying a key\n"

        elif command == "quit":
            methods.quitGame()

        elif command == "help":
            methods.clear(1)
            methods.giveInstructions(1)
        
        else:
            "\nPlease enter a valid command.\n"



def secondRoom(x): # Chooses which level user will play next

    methods.key2continue(1)
    
    if x == 1: # If user exits from door, begin Living Room level
        
        introLive()
        playLive()
        
    elif x == 2 or x == 3: # If user exits from window, begin Backyard level
        
        k = x - 2 # k will represent whether user has obtained a key or not (0 for no | 1 for yes)
        
        introYard(k)
        playYard()

introBed()
playBed()

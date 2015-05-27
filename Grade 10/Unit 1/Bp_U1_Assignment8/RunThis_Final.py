"""
+========================================================+
|Ian_Bantoto_and_Basil Pocklington,_ICS_201,_Assignment_8|
+========================================================+
|_Assignment_8_-_Three_to_Four_Level_Text_Adventure_Game_|
+========================================================+

"""

import methods # commonly used methods

# Introductions to each level

def Ib_introBed():
    print "---BEDROOM--- \n"
    methods.Ib_wait(0.2)
    print "You wake up on a plain bed, in a small room."
    methods.Ib_wait(0.2)
    print "There is a chained-up door, a slightly-open window, and a cabinet."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)
    print "As you get up from the bed, you turn around, and find that the bed disappeared!"
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)
    print "Reminder: Usable commands are open, unlock, break, use, look, inventory, help,"
    methods.Ib_wait(0.2)
    print "quit, and restart."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)

def Ib_introLive():
    print "---LIVING ROOM---"
    methods.Ib_wait(0.2)    
    print
    methods.Ib_wait(0.2)    
    print "You step through the door and find yourself in someone's old living room."
    methods.Ib_wait(0.2)
    print "There is a suspiciously-stuffed couch, a knife, a television, a remote"
    methods.Ib_wait(0.2)
    print "beside the television, and a locked door."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)
    print 'You turn around and try to open the door to go back to sleep,'
    methods.Ib_wait(0.2)
    print 'but it doesn\'t budge. "The door must have locked itself", you think to yourself.'
    methods.Ib_wait(0.2)

def Bp_introYard(key):
    print "---BACKYARD---"
    methods.Ib_wait(0.2)    
    print    
    methods.Ib_wait(0.2)
    print "You climb out the window, and emerge with some cuts on your arms, legs and face."
    methods.Ib_wait(0.2)

    # If User doesn't have a key, do nothing
    if key == 0:
        pass

    # If User has a key, tell them they lost it
    else:
        print "You notice that you lost the key you found whilst climbing out of the window."
        methods.Ib_wait(0.2)
        
    print "You don't want to try that again."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)
    print "You discover that you are now in what appears to be a backyard."
    methods.Ib_wait(0.2)
    print "You see a lawnmower, a plugged-in hose, a dying garden, some long grass,"
    methods.Ib_wait(0.2)
    print "and a locked sliding-door."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)

def Bp_introHall(cut):
    print "---HALLWAY---"
    methods.Ib_wait(0.2)    
    print
    methods.Ib_wait(0.2)
    print "You step through the door and find yourself in a short hallway."
    methods.Ib_wait(0.2)

    # If User has cuts, give them bandages.
    if cut == 1:
        pass

    # If User does not have cuts, do nothing.
    elif cut == 2:
        print "You see a first-aid kit on the floor, and put a few bandages over your cuts."
        methods.Ib_wait(0.2)
    
    print "There is a door at the end. You take a closer look."
    methods.Ib_wait(0.2)
    print "Just like all of the other doors you have encountered, it is locked from"
    methods.Ib_wait(0.2)
    print "the outside, but it seems to lead to the street!"
    methods.Ib_wait(0.2)
    print "\nYou see the door, a crystal chandelier, and a rug over the hardwood floor."
    methods.Ib_wait(0.2)
    print "\nYou have unlocked a new command! Type 'move object' to move the object."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)



# Descriptions of each level(look command)

def Ib_descBed():
    print "\nYou are in a small room."
    methods.Ib_wait(0.2)
    print "There is a chained-up door, a slightly-opened window, and a cabinet."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)

def Ib_descLive(x):
    print "\nYou are in someone's living room."
    methods.Ib_wait(0.2)
    if x == 0:
        print "There is a suspiciously-stuffed couch, a knife, a television, a remote"
        methods.Ib_wait(0.2)
        print "beside the television, and a locked door."
        methods.Ib_wait(0.2)
        print
        methods.Ib_wait(0.2)
    elif x == 1:
        print "There is a torn-up couch, a knife, a television across it, a remote"
        methods.Ib_wait(0.2)
        print "beside the television, and a locked door."
        methods.Ib_wait(0.2)
        print
        methods.Ib_wait(0.2)

def Bp_descYard():
    print "\nYou are in somebody's backyard."
    methods.Ib_wait(0.2)
    print "You can see a lawnmower, a plugged-in hose, a dying garden, some long grass,"
    methods.Ib_wait(0.2)
    print "and a locked sliding-door leading into the house."
    methods.Ib_wait(0.2)
    print
    methods.Ib_wait(0.2)
    
def Bp_descHall(rug):
    print "\nYou are in a hallway leading to a door outside."
    methods.Ib_wait(0.2)
    if rug == 0:
        print "You look around the hall and see the door, a crystal chandelier, and a rug over the hardwood floor."
        methods.Ib_wait(0.2)
        print
        methods.Ib_wait(0.2)
    elif rug == 1:
        print "You look around the hall and see the door, a crystal chandelier,"
        methods.Ib_wait(0.2)
        print "and a rug half overturned, covering the hardwood floor."
        methods.Ib_wait(0.2)
        print
        methods.Ib_wait(0.2)



# Begin each level

def Ib_playBed(): # Bedroom Level

    # Does the User have the key? 1 for yes, 0 for no.
    key = 0
    
    while key == 0: # While User doesn't have key, and level has not finished

        command = raw_input(">> ")
        
        if command == "open door":
            print "\nThe door is locked."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
        elif command == "open cabinet":
            print "\nYou found a key in the cabinet, it has been added to your inventory."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            print "Obtained new item: key!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # User has key in inventory
            key = 1

        elif command == "open window":
            print "\nYou try to open the window but it gets stuck."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "unlock door":
            print "\nYou cannot unlock the door without a key."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "unlock cabinet" or command == "unlock window":
            print "\nThere is nothing to unlock."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break cabinet":
            print "\nBro, you don't even lift. No way you'll be able to do that!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break door":
            print "\nYou aren't trained in breaching doors."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break window":
            print "\nYou broke some dude's window...Congrats!"
            methods.Ib_wait(0.1)
            print "You climb out the window into the next room."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # Begin next level (no key obtained)
            Ib_secondRoom(2)

        elif command == "use cabinet, window" or command == "use cabinet, door":
            print "\nThe cabinet is too heavy to pick up."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use window, cabinet" or command == "use window, door" or command == "use door, window" or command == "use door, cabinet":
            print "\n...What?"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "look":
            Ib_descBed()

        elif command == "inventory":
            print "\nYou have nothing in your inventory."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)

        elif command == "restart":
            Ib_restart()

        else:
            print "\nPlease use a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

    # While user has key in their inventory
    while key == 1: 

        command = raw_input(">> ")

        if command == "unlock cabinet" or command == "unlock window":
            print "\nThere is nothing to unlock."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "unlock door" or command == "use key, door":
            print "\nYou unlocked the door with your key, and entered the next room."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            print "You don't think you'll need the key later, so you leave it in the keyhole."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # Begin next level (key has been used)
            Ib_secondRoom(1)

        elif command == "use key, cabinet":
            print "\nYou scratch the cabinet with the key."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "use key, window":
            print "\nYou scratch the window with the key."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use cabinet, window" or command == "use cabinet, door":
            print "\nThe cabinet is too heavy to pick up."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use window, cabinet" or command == "use window, door" or command == "use door, window" or command == "use door, cabinet":
            print "...What?"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "open door":
            print "\nThe door is locked, but the key you found looks like it might fit."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "open cabinet":
            print "\nThere is nothing left in the cabinet."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "open window":
            print "\nYou try to open the window but it gets stuck."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break window":
            print "\nYou broke some dude's window...Congrats!"
            methods.Ib_wait(0.1)
            print "You climb out the window into the next room."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # Begin next level (with key)
            Ib_secondRoom(3)

        elif command == "break cabinet":
            print "\nBro, you don't even lift. No way you'll be able to do that."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break door":
            print "\nYou aren't trained in breaching doors."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "look":
            Ib_descBed()

        elif command == "inventory":
            print "\nYou are carrying a key"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "restart":
            Ib_restart()

        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)
        
        else:
            "\nPlease enter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

def Ib_playLive(): # Living Room Level

    # Does the User have the key? 1 for yes, 0 for no.
    key = 0

    # Has the level finished? 1 for yes, 0 for no.
    endLevel = 0

    # While user does not have the key, and level is not finished.
    while key == 0 and endLevel == 0:
    
        command = raw_input(">> ")
    
        if command == "open couch":
            print "\nYou cannot do that wihout some sort of sharp object."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "open television":    
            print "\nYou cannot open the television."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "open remote":
            print "\nYou open the remote, then close it because you dd not find anything useful."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "open knife":
            print "\nThe knife turns out to be a Swiss Army Knife,"
            methods.Ib_wait(0.1)
            print "but the other functions of the knife dont work,"
            methods.Ib_wait(0.1)
            print "so you put it back where it was."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "open door":
            print "\nThe door is locked."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "break couch":
            print "\nYou cannot do that without a sharp object."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break television":
            print "\nDude, it's a flat-screen 4K! Why would you want to do that?"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break remote":
            print "\nThe remote is invincible."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break knife":
            print "\nYou do not have the strength required to break the knife."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break door":
            print "\nYou aren't trained in breaching doors."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "unlock couch" or command == "unlock remote" or command == "unlock knife":
            print "\nThere is nothing to unlock!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "unlock door":
            print "\nYou cannot unlock the door without a key."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "use remote, television":
            print "\nYou turned on the television, it plays a movie you don't like,"
            methods.Ib_wait(0.1)
            print "so you shut it off."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
        elif command == "use knife, couch":
            print "\nYou sliced open the couch, and found a key!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            print "Obtained new item: key!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
            # User now has key in inventory.
            key = 1
        
        elif command == "use remote, door" or command == "use remote, couch" or command == "use remote, knife":
            print "\nNothing happened."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
                    
        elif command == "use knife, door":
            print "\nThat will take too long."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use knife, remote":
            print "\nYou scratch up the backside of the remote. You sure taught it a lesson."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
        elif command == "use knife, television":
            print "\nYou scratched up the best-looking television screen you've ever seen..."
            methods.Ib_wait(0.1)
            print "You monster."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
        elif command == "use knife" or command == "use remote":
            print '\nYou are using the command wrong, type "help" for commands and how to use them.'
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "look":
            Ib_descLive(0)
    
        elif command == "quit":
            methods.Ib_quitGame()
        
        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)

        elif command == "inventory":
            print "\nYou are not carrying anything."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "restart":
            Ib_restart()
        
        else:
            print "\nPlease enter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

    # While the level has not finished
    while endLevel == 0:
        
        command = raw_input(">> ")
        
        if command == "open couch":
            print "\nThe couch has alraedy been opened."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "open television":
            print "\nDude, it's a flat-screen 4K! Why would you want to do that?"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "open remote":
            print "\nYou open the remote, then close it because you dd not find anything useful in it."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "open knife":
            print "\nThe knife turns out to be a Swiss Army Knife,"
            methods.Ib_wait(0.1)
            print "but the other functions of the knife dont work,"
            methods.Ib_wait(0.1)
            print"so you put it back where it was."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
        elif command == "open door":
            print "\nThe door is locked, but the key you found looks like it might fit."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break couch":
            print "\nThe couch has already been opened."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break television":
            print "\nDude, it's a flat-screen 4K! Why would you want to do that?"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break remote":
            print "\nThe remote is invincible."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break knife":
            print "\nYou do not have the strength required to break the knife."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "break door":
            print "\nYou aren't trained in breaching doors, but you have a key that can unlock the door."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "unlock couch" or command == "unlock remote" or command == "unlock knife" or command == "unlock key":
            print "\nThere is nothing to unlock."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "unlock door" or command == "use key, door":
            print "\nYou unlocked the door with your key, and entered the next room."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # End the level
            endLevel = 1
        
        elif command == "use key, television" or command == "use knife, television":
            print "\nYou scratched up the best-looking television screen you've ever seen..."
            methods.Ib_wait(0.1)
            print "You monster."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "use key, couch":
            print "\nYou scratch up the couch even more."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "use key, remote":
            print "\nYou scratch the remote with the key."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "use key, knife" or command == "use knife, key":
            print "\nYou scratch the knife and key together. Nothing happens."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use knife, couch":
            print "\nYou tear up the couch even more."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use knife, door":
            print "\nThat will take too long."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use knife, remote":
            print "\nYou scratch up the backside of the remote. You sure taught it a lesson."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
        elif command == "use knife" or command == "use remote" or command == "use key":
            print '\nYou are using the command wrong, type "help" for commands and how to use them.'
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "use remote, television":
            print "\nYou turned on the television, it plays a movie you don't like,"
            methods.Ib_wait(0.1)
            print "so you shut it off."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif "use remote, " in command:
            print "\nNothing happened."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        elif command == "look":
            Ib_descLive(1)
    
        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "restart":
            Ib_restart()
        
        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)

        elif command == "inventory":
            print "You are carrying a key."
        
        else:
            print "\nPlease enter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

    # After the level has been completed.
    while endLevel == 1:
        Ib_thirdRoom(1)

def Bp_playYard(): # Backyard Level

    # Is the level finished? 1 for yes, 0 for no.
    endLevel = 0

    # Has the User used the lawnmower? 1 for yes, 0 for no.
    mow = 0

    # While user has not mowed the grass and level is not over.
    while mow == 0 and endLevel == 0:
        
        command = raw_input(">> ")
        
        if command == "open door":
            print "\nThe door is locked."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "unlock door":
            print "\nYou don't have the key."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "break door":
            print "\nYou are too cut and tired after climbing out of the window to break the glass."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "use lawnmower, grass":
            print "\nYou proceed to mow the grass, only to find that the lawnmower doesn't start!\nYou decide to check to see if there is anything blocking the blades,"
            methods.Ib_wait(0.1)
            print "and you find a medium sized rock."
            methods.Ib_wait(0.1)
            print "Hmm... this could be good for breaking something."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            print "Obtained new item: Rock!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # User has now attempted to mow the garden, and has rock in inventory.
            mow = 1

        elif command == "use lawnmower, garden":
            print "\nYou proceed to mow the garden, only to find that the lawnmower doesn't start!\nYou decide to check to see if there is anything blocking the blades,"
            methods.Ib_wait(0.1)
            print "and you find a medium sized rock."
            methods.Ib_wait(0.1)
            print "Hmm... this could be good for breaking something."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            print "Obtaind new item: Rock!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # User has now attempted to mow the garden, and has rock in inventory.
            mow = 1
        
        elif 'use hose, ' in command:
            print "\nNo water comes out."
            methods.Ib_wait(0.1)
        
        elif command == "break hose" or command == "break lawnmower":
            print "\nIt is too strong to break."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "unlock lawnmower" or command == "unlock hose":
            print "\nThere is nothing to unlock!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "look":
            Bp_descYard()
        
        elif command == "inventory":
            print "\nYou are not carrying anything."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "help":
            methods.Ib_giveInstructions(1)

        elif command == "restart":
            Ib_restart()

        elif command == "quit":
            methods.Ib_quitGame()
        
        else:
            print "\nEnter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

    # While the level is not finished.
    while endLevel == 0:
    
        command = raw_input(">> ")

        if command == "use rock, door" or command == "use rock, sliding door":
            print "\nIt worked! The glass door is broken."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # End the level.
            endLevel = 1
        
        elif command == "open door":
            print "\nThe door is locked."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "unlock door":
            print "\nYou need a key to do that."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif "use lawnmower, " in command:
            print "\nThe lawnmower isn't working."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif "use hose, " in command:
            print "\nNo water comes out."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "break hose" or command == "break lawnmower":
            print "\nIt is too strong to break."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "unlock lawnmower" or command == "unlock hose":
            print "\nThere is nothing to unlock!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "look":
            Bp_descYard()
    
        elif command == "inventory":
            print "\nYou are carrying a rock."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
    
        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)
    
        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "restart":
            Ib_restart()

        else:
            print "\nPlease enter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

    # After the level has been completed.
    while endLevel == 1:
        Ib_thirdRoom(2)

def Bp_playHall(): # Hallway Level
    
    # Has the User moved the rug? 1 for yes, 0 for no.
    rugMove = 0
    
    # Has the User interacted with the chandelier? 1 for yes, 0 for no.
    chandelier = 0
    
    # While the User has not interacted with chandelier and rug.
    while rugMove == 0 and chandelier == 0:

        command = raw_input(">> ")
        
        if command == "move rug" or command == "use rug":
            print "\nYou move the rug to reveal a long thin broom handle."
            methods.Ib_wait(0.1)
            print "\nObtained new item: Broomhandle!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            # User has now interacted with rug.
            rugMove = 1
        
        elif "chandelier" in command:
            print
            methods.Ib_wait(0.1)
            print "The chandelier is out of reach!"
            methods.Ib_wait(0.1)
            print "If only you had something to extend your reach..."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "break rug":
            print
            methods.Ib_wait(0.1)            
            print "Unable to break rug."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)            
        
        elif "door" in command:
            print
            methods.Ib_wait(0.1) 
            print "The door is locked tight, and you have no chance of breaking it."
            methods.Ib_wait(0.1) 
            print
            methods.Ib_wait(0.1) 
        
        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "restart":
            methods.Ib_restart()
        
        elif command == "look":
            Bp_descHall(0)
        
        elif command == "help":
            methods.Ib_giveInstructions(2)

        elif command == "inventory":
            print "\nYou are not carrying anything."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        else:
            print "\nPlease enter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
            
    # While the User has interacted with rug, but not with chandelier.
    while rugMove == 1 and chandelier == 0:
        
        command = raw_input(">> ")
        
        if command == "break chandelier" or command == "use broomhandle, chandelier" or command == "use handle, chandelier" or command == "use broom, chandelier":
            print "\nYou rustle the chandelier with the long broomhandle, and a key falls onto the hardwood floor!"
            methods.Ib_wait(0.1)
            print "\nObtained new item: key!"
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

            #User has now interacted with chandelier.
            chandelier = 1
        
        elif "door" in command:
            print "\nThe door is locked tight, and you have no chance of breaking it."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)
        
        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "restart":
            Ib_restart()

        elif command == "look":
            Bp_descHall(1)
        
        elif command == "help":
            methods.Ib_giveInstructions(2)
            
        elif command == "inventory":
            print "\nYou are carrying a long broomhandle."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

        else:
            print "\nPlease enter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)

    # While the User has interacted with rug and chandelier.
    while rugMove == 1 and chandelier == 1:

        command = raw_input(">> ")

        if command == "use key, door" or command == "unlock door":
            print "\nYou have escaped the house! Congatulations!\n"
            methods.Ib_key2continue(2)
            methods.Ib_gameOver()

        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "restart":
            Ib_restart()

        elif command == "look":
            Bp_descHall(1)

        elif command == "help":
            methods.Ib_giveInstructions(2)
            
        elif command == "inventory":
            print "\nYou are carrying a key and a long broomhandle."
            methods.Ib_wait(0.1)
            methods.Ib_wait(0.1)

        else:
            print "\nPlease enter a valid command."
            methods.Ib_wait(0.1)
            print
            methods.Ib_wait(0.1)



# Other functions

def Ib_secondRoom(x): # Chooses which level User will play next

    methods.Ib_key2continue(1)
    
    if x == 1: # If User exits from door, begin Living Room level
        
        Ib_introLive()
        Ib_playLive()
        
    elif x == 2 or x == 3: # If User exits from window, begin Backyard level
        
        k = x - 2 # k -> Has User obtained a key or not (1 for yes | 0 for no)
        
        Bp_introYard(k)
        Bp_playYard()
        
def Ib_thirdRoom(x): # Begin the next level
    
    methods.Ib_key2continue(1)

    Bp_introHall(x)
    Bp_playHall()

def Ib_restart(): # Starts over from Bed level
    print
    methods.Ib_wait(0.3)
    print "Restarting..."
    methods.Ib_wait(0.3)
    print "..."
    methods.Ib_wait(0.3)
    print "..."
    methods.Ib_wait(0.3)
    print "..."

    Ib_playGame()

def Ib_playGame(): # Starts (or restarts) game
    methods.BI_welcomeScreen()
    methods.Ib_key2play()
    Ib_introBed()
    Ib_playBed()



# main

Ib_playGame()

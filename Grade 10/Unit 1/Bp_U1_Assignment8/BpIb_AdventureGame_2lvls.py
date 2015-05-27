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
    print "You wake up on a plain bed, in a small room."
    print "There is a chained-up door, a slightly-open window, and a cabinet.\n"
    print "As you get up from the bed, you turn around, and find that the bed disappeared!\n"
    print "Reminder: Usable commands are open, unlock, break, use, look, inventory, help, and quit.\n"

def Ib_introLive():
    print "---LIVING ROOM---\n"
    print "You step through the door and find yourself in someone's old living room."
    print "There is a suspiciously-stuffed couch, a knife, a television across it,\na remote beside the television, and a locked door.\n"
    print 'You turn around and try to open the door to go back to sleep,'
    print 'but it doesn\'t budge. "The door must have locked itself", you think to yourself.\n'

def Bp_introYard(key):
    print "---BACKYARD--- \n"
    print "You climb out the window, and emerge with some cuts on your arms, legs and face."

    if key == 0: # If user doesn't have a key, do nothing
        pass
    else: # If user has a key, tell them they lost it
        print "You notice that you lost the key you found whilst climbing out of the window."
        
    print "You don't want to try that again.\n"
    print "You discover that you are now in what appears to be a backyard."
    print "You see a lawnmower, a plugged-in hose, a dying garden, some long grass, and a locked sliding-door.\n"

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

# Descriptions of each level(look command)

def Ib_descBed():
    print "\nYou are in a small room."
    print "There is a chained-up door, a slightly-opened window, and a cabinet.\n"

def Ib_descLive(x):
    print "\nYou are in someone's living room."
    if x == 0:
        print "There is a suspiciously-stuffed couch, a knife, a television across it,\na remote beside the television, and a locked door.\n"
    elif x == 1:
        print "There is a torn-up couch, a television across it,\na remote right beside the television, and a locked door.\n"

def Bp_descYard():
    print "\nYou are in somebody's backyard."
    print "You can see a lawnmower, a plugged-in hose, a dying garden, some long grass, and a locked sliding-door leading into the house.\n"

# Begin each level

def Ib_playBed(): # Bedroom Level

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
            Ib_descBed()

        elif command == "inventory":
            print "\nYou have nothing in your inventory.\n"

        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)
        else:
            print "\nPlease use a valid command.\n"
    
    while key == 1: # While user has key in their inventory

        command = raw_input(">> ")

        if command == "unlock cabinet" or command == "unlock window":
            print "\nThere is nothing to unlock.\n"
        
        elif command == "unlock door" or command == "use key, door":
            print "\nYou unlocked the door with your key, and entered the next room.\n"
            print "You don't think you'll need the key later, so you leave it in the keyhole.\n"
            Ib_secondRoom(1) # Begin next level (key has been used)

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
            Ib_secondRoom(3) # Begin next level (with key)

        elif command == "break cabinet":
            print "\nBro, you don't even lift. No way you'll be able to do that.\n"

        elif command == "break door":
            print "\nYou aren't trained in breaching doors.\n"

        elif command == "look":
            Ib_descBed()

        elif command == "inventory":
            print "\nYou are carrying a key\n"

        elif command == "quit":
            methods.Ib_quitGame()

        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)
        
        else:
            "\nPlease enter a valid command.\n"



def Ib_secondRoom(x): # Chooses which level user will play next

    methods.Ib_key2continue(1)
    
    if x == 1: # If user exits from door, begin Living Room level
        
        Ib_introLive()
        Ib_playLive()
        
    elif x == 2 or x == 3: # If user exits from window, begin Backyard level
        
        k = x - 2 # k will represent whether user has obtained a key or not (0 for no | 1 for yes)
        
        Bp_introYard(k)
        Bp_playYard()



def Ib_playLive(): # Living Room Level
    
    key = 0
    endLevel = 0
    
    while key == 0 and endLevel == 0: # While user does not have the key, and level is not finished
    
        command = raw_input(">> ")
    
        if command == "open couch":
            print "\nYou cannot do that wihout some sort of sharp object.\n"

        elif command == "open television":    
            print "\nYou cannot open the television.\n"
        
        elif command == "open remote":
            print "\nYou open the remote, then close it because you dd not find anything useful in it.\n"
    
        elif command == "open knife":
            print "\nThe knife turns out to be a Swiss Army Knife,\nbut the other functions of the knife dont work,\nso you put it back where it was.\n"
        
        elif command == "open door":
            print "\nThe door is locked.\n"
    
        elif command == "break couch":
            print "\nYou cannot do that without a sharp object.\n"

        elif command == "break television":
            print "\nDude, it's a flat-screen 4K! Why would you want to do that?\n"

        elif command == "break remote":
            print "\nThe remote is invincible.\n"

        elif command == "break knife":
            print "\nYou do not have the strength required to break the knife.\n"

        elif command == "break door":
            print "\nYou aren't trained in breaching doors.\n"
        
        elif command == "unlock couch" or command == "unlock remote" or command == "unlock knife":
            print "\nThere is nothing to unlock!\n"
        
        elif command == "unlock door":
            print "\nYou cannot unlock the door without a key.\n"
    
        elif command == "use remote, television":
            print "\nYou turned on the television, it plays a movie you don't like, so you shut it off.\n"
            
        elif command == "use knife, couch":
            print "\nYou sliced open the couch, and found a key!\n"
            key = 1 # User now has key in inventory
        
        elif command == "use remote, door" or command == "use remote, couch" or command == "use remote, knife":
            print "\nNothing happened.\n"
                    
        elif command == "use knife, door":
            print "\nThat will take too long.\n"

        elif command == "use knife, remote":
            print "\nYou scratch up the backside of the remote. You sure taught it a lesson.\n"
            
        elif command == "use knife, television":
            print "\nYou scratched up the best-looking television screen you've ever seen...You monster.\n"
            
        elif command == "use knife" or command == "use remote":
            print '\nYou are using the command wrong, type "help" for commands and how to use them.\n'
        
        elif command == "look":
            Ib_descLive(0)
    
        elif command == "quit":
            methods.Ib_quitGame()
        
        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)

        elif command == "inventory":
            print "\nYou are not carrying anything.\n"
        
        else:
            print "\nPlease enter a valid command.\n"

    while endLevel == 0: # While the level is not finished
        
        command = raw_input(">> ")
        
        if command == "open couch":
            print "\nThe couch has alraedy been opened.\n"
        
        elif command == "open television":
            print "\nDude, it's a flat-screen 4K! Why would you want to do that?\n"

        elif command == "open remote":
            print "\nYou open the remote, then close it because you dd not find anything useful in it.\n"
        
        elif command == "open knife":
            print "\nThe knife turns out to be a Swiss Army Knife,\nbut the other functions of the knife dont work,\nso you put it back where it was.\n"
            
        elif command == "open door":
            print "\nThe door is locked, but the key you found looks like it might fit.\n"        

        elif command == "break couch":
            print "\nThe couch has already been opened.\n"

        elif command == "break television":
            print "\nDude, it's a flat-screen 4K! Why would you want to do that?\n"

        elif command == "break remote":
            print "\nThe remote is invincible.\n"

        elif command == "break knife":
            print "\nYou do not have the strength required to break the knife.\n"

        elif command == "break door":
            print "\nYou aren't trained in breaching doors, but you have a key that can unlock the door.\n"

        elif command == "unlock couch" or command == "unlock remote" or command == "unlock knife" or command == "unlock key":
            print "\nThere is nothing to unlock.\n"

        elif command == "unlock door" or command == "use key, door":
            print "\nYou unlocked the door with your key, and entered the next room.\n"
            endLevel = 1 # End the level
        
        elif command == "use key, television" or command == "use knife, television":
            print "\nYou scratched up the best-looking television screen you've ever seen...\nYou monster.\n"
        
        elif command == "use key, couch":
            print "\nYou scratch up the couch even more.\n"
        
        elif command == "use key, remote":
            print "\nYou scratch the remote with the key.\n"
        
        elif command == "use key, knife" or command == "use knife, key":
            print "\nYou scratch the knife and key together. Nothing happens.\n"

        elif command == "use knife, couch":
            print "\nYou tear up the couch even more.\n"

        elif command == "use knife, door":
            print "\nThat will take too long.\n"

        elif command == "use knife, remote":
            print "\nYou scratch up the backside of the remote. You sure taught it a lesson.\n"
            
        elif command == "use knife" or command == "use remote" or command == "use key":
            print '\nYou are using the command wrong, type "help" for commands and how to use them.\n'

        elif command == "use remote, television":
            print "\nYou turned on the television, it plays a movie you don't like, so you shut it off.\n"

        elif "use remote, " in command:
            print "\nNothing happened.\n"

        elif command == "look":
            Ib_descLive(1)
    
        elif command == "quit":
            methods.Ib_quitGame()
        
        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)

        elif command == "inventory":
            print "You are carrying a key."
        
        else:
            print "\nPlease enter a valid command.\n"

    while endLevel == 1: # While the level is over
        Ib_thirdRoom(1)

def Bp_playYard(): # Backyard Level
    
    endLevel = 0    
    mow = 0
    
    while mow == 0 and endLevel == 0: # While user has not mowed the grass and level is not over
        
        command = raw_input(">> ")
        
        if command == "open door":
            print "\nThe door is locked.\n"
        
        elif command == "unlock door":
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
        
        elif 'use hose, ' in command:
            print "\nNo water comes out.\n"
        
        elif command == "break hose" or command == "break lawnmower":
            print "\nIt is too strong to break.\n"
        
        elif command == "unlock lawnmower" or command == "unlock hose":
            print "\nThere is nothing to unlock!\n"
        
        elif command == "look":
            Bp_descYard()
        
        elif command == "inventory":
            print "\nYou are not carrying anything.\n"
        
        elif command == "help":
            methods.Ib_giveInstructions(1)
        
        elif command == "quit":
            methods.Ib_quitGame()
        
        else:
            print "\nEnter a valid command.\n"

    while endLevel == 0: # While the level is not finished
    
        command = raw_input(">> ")

        if command == "use rock, door" or command == "use rock, sliding door":
            print "\nIt worked! The glass door is broken.\n"
            endLevel = 1 # End the level
        
        elif command == "open door":
            print "\nThe door is locked.\n"
    
        elif command == "unlock door":
            print "\nYou need a key to do that.\n"
    
        elif "use lawnmower, " in command:
            print "\nThe lawnmower isn't working\n"
    
        elif "use hose, " in command:
            print "\nNo water comes out.\n"
    
        elif command == "break hose" or command == "break lawnmower":
            print "\nIt is too strong to break.\n"
    
        elif command == "unlock lawnmower" or command == "unlock hose":
            print "\nThere is nothing to unlock!\n"
    
        elif command == "look":
            Bp_descYard()
    
        elif command == "inventory":
            print "\nYou are carrying a rock.\n"
    
        elif command == "help":
            methods.Ib_clear(1)
            methods.Ib_giveInstructions(1)
    
        elif command == "quit":
            methods.Ib_quitGame()

        else:
            print "\nPlease enter a valid command.\n"

    while endLevel == 1: #While the level is over
        Ib_thirdRoom(2)



def Ib_thirdRoom(x): # Begin the next level
    
    methods.Ib_key2continue(1)

    Bp_introHall(x)
    Bp_playHall()



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
def Ib_gameOver():
    
    
    methods.key2continue(1)
    methods.quitGame()


# main
methods.BI_welcomeScreen()
methods.Ib_key2play()
Ib_introBed()
Ib_playBed()

Ib_gameOver()

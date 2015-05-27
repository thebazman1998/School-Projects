def introLive():
    print "---LIVING ROOM---\n"
    print "You step through the door and find yourself in someone's old living room."
    print "There is a suspiciously-stuffed couch, a knife, a television across it,\na remote beside the television, and a locked door.\n"
    print 'You turn around and try to open the door to go back to sleep,'
    print 'but it doesn\'t budge. "The door must have locked itself", you think to yourself.\n'

def descLive(x):
    print "\nYou are in someone's living room."
    if x == 0:
        print "There is a suspiciously-stuffed couch, a knife, a television across it,\na remote beside the television, and a locked door.\n"
    elif x == 1:
        print "There is a torn-up couch, a television across it,\na remote right beside the television, and a locked door.\n"

def playLive(): # Living Room Level
    
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
            descLive(0)
    
        elif command == "quit":
            methods.quitGame()
        
        elif command == "help":
            methods.clear(1)
            methods.giveInstructions(1)

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
            descLive(1)
    
        elif command == "quit":
            methods.quitGame()
        
        elif command == "help":
            methods.clear(1)
            methods.giveInstructions(1)

        elif command == "inventory":
            print "You are carrying a key."
        
        else:
            print "\nPlease enter a valid command.\n"

    while endLevel == 1: # While the level is over
        thirdRoom(1)

def thirdRoom(x): # Begin the next level
    
    methods.key2continue(1)

    introHall(x)
    playHall()

def playHall(): # Hallway Level
        
    rugMove = 0
    
    while rugMove == 0:

        command = raw_input(">> ")

        if command == "quit":
            methods.quitGame()

introLive()
playLive()

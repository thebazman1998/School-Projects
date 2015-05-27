import methods

def introLive():
    print "---LIVING ROOM---\n"
    print "You find yourself in someone's old living room."
    print "There is a suspiciously-stuffed couch, a knife, a television across it,\na remote beside the television, and a locked door."
    print "You turn around and try to open the door to go back to sleep, but it doesn't budge."
    print '"The door must have locked itself", you think to yourself.\n'

def descLive(x):
    print "\nYou are in someone's living room."
    if x == 0:
        print "There is a suspiciously-stuffed couch, a knife, a television across it,\na remote beside the television, and a locked door."
    elif x == 1:
        print "There is a torn-up couch, a television across it,\na remote right beside the television, and a locked door."

def playLive():
    
    key = 0
    
    while key == 0:
    
        command = raw_input()
    
        if command == "open couch":
            print "\nYou cannot do that wihout a sharp object\n"

        elif command == "open television":    
            print "\nYou cannot open the television\n"
        
        elif command == "open remote":
            print "\nYou open the remote, then close it because you dd not find anything in it.\n"
    
        elif command == "open knife":
            print "\n...What?\n"
        
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
        
        elif command == "unlock couch":
            print "\n...What?\n"
        
        elif command == "unlock remote":
            print "\n...What?\n"
        
        elif command == "unlock knife":
            print "\n...What?\n"
        
        elif command == "unlock door":
            print "\nYou cannot unlock the door without a key.\n"
    
        elif command == "use remote, television":
            print "\nYou turned on the television, it plays a movie you don't like, so you shut it off.\n"
            
        elif command == "use knife, couch":
            print "\nYou sliced open the couch, and found a key!\n"
            key = 1
        
        elif command == "use remote, couch":
            print "\nThe couch cannot be controlled by the remote.\n"
        
        elif command == "use remote, door":
            print "\nThe door cannot be controlled by the remote\n"
            
        elif command == "use knife, door":
            print "\nThat will take too long.\n"
            
        elif command == "use knife, television":
            print "You scratched up the best-looking television screen you've ever seen...You monster."
            
        elif command == "use knife" or command == "use remote" or command == "use key" or command == "":
            print 'You are using the command wrong, type "help" for commands and how to use them.'
        
        elif command == "look":
            descLive(0)
    
        elif command == "quit":
            methods.quitGame()
        
        elif command == "help":
            methods.clear(1)
            methods.giveInstructions(1)
        
        else:
            print "\nPlease enter a valid command.\n"

    while key == 1:
        
        command = raw_input()
        
        if command == "open couch":
            print "\nThe couch has alraedy been opened.\n"
        
        elif command == "open television":
            print "\nDude, it's a flat-screen 4K! Why would you want to do that?\n"

        elif command == "open remote":
            print "\nYou open the remote, then close it because you dd not find anything in it.\n"
        
        elif command == "open knife":
            print "\n...What?\n"
            
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

        elif command == "unlock couch":
            print "\n...What?\n"
        
        elif command == "unlock remote":
            print "\n...What?\n"
        
        elif command == "unlock knife":
            print "\n...What?\n"

        elif command == "unlock door":
            print "\nYou unlocked the door with your key, and entered the next room.\n"
            #thirdLevel()
        
        elif command == "use key, door":
            print "\nYou unlocked the door with your key, and entered the next room.\n"
            #thirdLevel()
        
        elif command == "use key, television":
            print "\nYou scratched up the best-looking television screen you've ever seen...You monster.\n"
        
        elif command == "use key, couch":
            print "\nYou scratch up the couch even more.\n"
        
        elif command == "use key, remote":
            print "\n...What?\n"
        
        elif command == "use key, knife":
            print "\n...What?\n"

        elif command == "use knife, couch":
            print "\nYou tear up the couch even more.\n"

        elif command == "use knife, door":
            print "\nThat will take too long.\n"
            
        elif command == "use knife, television":
            print "You scratched up the best-looking television screen you've ever seen...You monster."
            
        elif command == "use knife" or command == "use remote" or command == "use key" or command == "":
            print 'You are using the command wrong, type "help" for commands and how to use them.'

        elif command == "look":
            descLive(1)
    
        elif command == "quit":
            methods.quitGame()
        
        elif command == "help":
            methods.clear(1)
            methods.giveInstructions(1)
        
        else:
            print "\nPlease enter a valid command.\n"


introLive()
playLive()

#open, break, unlock, open, use

#couch, knife, tv, remote, door.....key
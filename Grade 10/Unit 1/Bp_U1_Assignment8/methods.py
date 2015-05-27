import sys

def BI_welcomeScreen(): # Clear the screen, then welcome the player
    Ib_clear(50)
    print "               __________________________"
    Ib_wait(0.1)
    print "              /         \                \ "
    Ib_wait(0.1)
    print "             |           \______     _____\ "
    Ib_wait(0.1)
    print "             |     __    |      |   |"
    Ib_wait(0.1)
    print "             |    /  \   |      |   |"
    Ib_wait(0.1)
    print "             |    \__/   |      |   |"
    Ib_wait(0.1)
    print "   __________|           |______|   |_______________"
    Ib_wait(0.1)
    print "  /__________|          _/______|   |______________/"
    Ib_wait(0.1)
    print " /___________|           \______|   |_____________/"
    Ib_wait(0.1)
    print "/____________|     ____   \_____|   |____________/"
    Ib_wait(0.1)
    print "             |    /    \   |    |   |"
    Ib_wait(0.1)
    print "             |   |      |  |    |   |"
    Ib_wait(0.1)
    print "             |    \____/   |    |   |"
    Ib_wait(0.1)
    print "             |             |____|   |______"
    Ib_wait(0.1)
    print "             |             /              /"
    Ib_wait(0.1)
    print "              \___________/______________/"
    print "\n"
    Ib_wait(0.1)
    print "+=====================================================+"
    Ib_wait(0.1)
    print "|Welcome to our very first text-adventure escape game!|"
    Ib_wait(0.1)
    print "|__________By Ian Bantoto && Basil Pocklington________|"
    Ib_wait(0.1)
    print "+=====================================================+"
    print "\n"
    
    play = ''

    while play.upper() != 'Y' and play.upper() != 'N': # Ask player if they want to play
        play = raw_input("Would you like to play?(Y/N): ")
            
    if play.upper() == 'Y' or play.upper() == 'YES':
        Ib_clear(50)
        Ib_giveInstructions(0)
    
    elif play.upper() == 'N' or play.upper() == 'NO':
        print "Goodbye!"
        Ib_wait(0.5)
        sys.exit(0)

def Ib_giveInstructions(x): # Give player instructions if they want them
    if x == 0:
        answer = ''
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = raw_input("Would you like to learn how to play?(Y/N): ")
        
        if answer.upper() == 'Y':
            print "\nUse these commands to interact with the environment in order to escape.\n"
            print "The list of commmands is: \n"
            Ib_wait(0.5)
            print "type: open object/exit [opens object/exit]"
            Ib_wait(0.5)
            print "type: unlock exit [unlocks exit]"
            Ib_wait(0.5)
            print "type: break object/exit [breaks object/exit]"
            Ib_wait(0.5)
            print "type: use object, object/exit [uses object on object/exit]"
            Ib_wait(0.5)
            print "type: look [Used to observe surroundings]"
            Ib_wait(0.5)
            print "type: inventory [Look at inventory]"
            Ib_wait(0.5)
            print "type: help [Opens list of commands]"
            Ib_wait(0.5)
            print "type: quit [Quits the game]"
            Ib_wait(0.5)
            print "type: restart [Restarts the game]"
            Ib_wait(0.3)
            print
            Ib_wait(0.3)
            print "Good luck!"
            Ib_wait(0.3)
            print
            Ib_wait(0.3)
        
        elif answer.upper() == 'N':
            print "\nOkay then, good luck!\n"

    elif x == 1:
        print "The list of commmands is: \n\n"
        Ib_wait(0.5)
        print "type: open object/exit [opens object/exit]"
        Ib_wait(0.5)
        print "type: unlock exit [unlocks exit]"
        Ib_wait(0.5)
        print "type: break object/exit [breaks object/exit]"
        Ib_wait(0.5)
        print "type: use object, object/exit [uses object on object/exit]"
        Ib_wait(0.5)
        print "type: look [Used to observe surroundings]"
        Ib_wait(0.5)
        print "type: inventory [Look at inventory]"
        Ib_wait(0.5)
        print "type: help [Opens list of commands]"
        Ib_wait(0.5)
        print "type: quit [Quits the game]"
        Ib_wait(0.5)
        print "type: restart [Restarts the game]\n"
        Ib_wait(0.5)
        print "These commands can be used to interact with the environment."
        Ib_wait(0.3)
        print
        Ib_wait(0.3)
        
    elif x == 2:
        print "The list of commmands is: \n\n"
        Ib_wait(0.5)
        print "type: open object/exit [opens object/exit]"
        Ib_wait(0.5)
        print "type: unlock exit [unlocks exit]"
        Ib_wait(0.5)
        print "type: break object/exit [breaks object/exit]"
        Ib_wait(0.5)
        print "type: use object, object/exit [uses object on object/exit]"
        Ib_wait(0.5)
        print "type: move object [moves object]"
        Ib_wait(0.5)
        print "type: look [Used to observe surroundings]"
        Ib_wait(0.5)
        print "type: inventory [Look at inventory]"
        Ib_wait(0.5)
        print "type: help [Opens list of commands]"
        Ib_wait(0.5)
        print "type: quit [Quits the game]"
        Ib_wait(0.5)
        print "type: restart [Restarts the game]"
        Ib_wait(0.3)
        print
        Ib_wait(0.3)
        print "These commands can be used to interact with the environment."
        Ib_wait(0.3)
        print
        Ib_wait(0.3)

        
def Ib_gameOver():
            
        Ib_clear(50)
        print "               __________________________"
        Ib_wait(0.1)
        print "              /         \                \ "
        Ib_wait(0.1)
        print "             |           \______     _____\ "
        Ib_wait(0.1)
        print "             |     __    |      |   |"
        Ib_wait(0.1)
        print "             |    /  \   |      |   |"
        Ib_wait(0.1)
        print "             |    \__/   |      |   |"
        Ib_wait(0.1)
        print "   __________|           |______|   |_______________"
        Ib_wait(0.1)
        print "  /__________|          _/______|   |______________/"
        Ib_wait(0.1)
        print " /___________|           \______|   |_____________/"
        Ib_wait(0.1)
        print "/____________|     ____   \_____|   |____________/"
        Ib_wait(0.1)
        print "             |    /    \   |    |   |"
        Ib_wait(0.1)
        print "             |   |      |  |    |   |"
        Ib_wait(0.1)
        print "             |    \____/   |    |   |"
        Ib_wait(0.1)
        print "             |             |____|   |______"
        Ib_wait(0.1)
        print "             |             /              /"
        Ib_wait(0.1)
        print "              \___________/______________/"
        Ib_wait(0.1)
        print
        Ib_wait(0.3)
        print "Congratulations for completing our game!"
        Ib_wait(0.3)
        print "We look forward to you playing our games in the near future!"
        Ib_wait(0.3)
            
        Ib_quitGame()

def Ib_key2play(): # Confirm that the player wants to start playing
    key = raw_input("Press Enter to start playing! ")
    Ib_wait(0.7)
    Ib_clear(50)

def Ib_key2continue(x): # Confirm player is fine with the screen being cleared

    if x == 0:
        temp = raw_input("Press Enter to start playing! ")
    elif x == 1:
        temp = raw_input("Press Enter to continue to the next room! ")
    elif x == 2:
        temp = raw_input("Press Enter to continue!")
        
    Ib_wait(0.7)
    Ib_clear(50)

def Ib_quitGame(): # Exits game,

    print "\nThanks for playing!"
    Ib_wait(0.3)
    print
    Ib_wait(0.3)
    blank = raw_input("Press Enter to close the program ")

    Ib_wait(0.2)
    print
    Ib_wait(0.2)
    print "Quitting..."
    Ib_wait(0.2)
    print "..."
    Ib_wait(0.2)
    print "..."
    Ib_wait(0.2)
    print "..."
    sys.exit(0)

def Ib_wait(x): # Pauses for x seconds
    import time
    time.sleep(x)

def Ib_clear(x): # Clear paramater amount of lines
    print "\n" * x

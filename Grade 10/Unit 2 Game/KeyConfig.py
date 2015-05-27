'''
Created on Apr 30, 2014

@author: Basil
'''
def main():
    default = raw_input('The Defaults are:\nP1 Left =   a\nP1 Right =  d\nP1 Jump =   w\nP1 Crouch = s\nP1 Punch =  v\nP1 Kick =   b\n \nP2 Left =  k\nP2 Right = ;\nP2 Up =    o\nP2 Down =  l\nP2 Punch = ]\nP2 Kick =  BckSlsh\n \nWould you like to change them?\n>> ')
    default = default.lower()

    if 'y' in default:
        values()
    elif 'n' in default:
        p1_key_left = ord('a')
        p1_key_right = ord('d')
        p1_key_up = ord('w')
        p1_key_down = ord('s')
        p1_key_punch = ord('v')
        p1_key_kick = ord('b')
    
        p2_key_left = ord('k')
        p2_key_right = ord(';')
        p2_key_up = ord('o')
        p2_key_down = ord('l')
        p2_key_punch = ord(']')
        p2_key_kick = ord('\\')
        
        music = ord('m')
        restart = ord('r')
        
        player1_controls = [p1_key_left, p1_key_right, p1_key_up, p1_key_down, p1_key_punch, p1_key_kick]
        player2_controls = [p2_key_left, p2_key_right, p2_key_up, p2_key_down, p2_key_punch, p2_key_kick]
        controls = [player1_controls, player2_controls, music, restart]
        return controls

def values():
    print '\nControl Configuration\n'
    
    p1_key_left = ord(raw_input('Player 1 left\n>> '))
    p1_key_right = ord(raw_input('Player 1 right\n>> '))
    p1_key_up = ord(raw_input('Player 1 up\n>> '))
    p1_key_down = ord(raw_input('Player 1 crouch\n>> '))
    p1_key_punch = ord(raw_input('Player 1 punch\n>> '))
    p1_key_kick = ord(raw_input('Player 1 kick\n>> '))
    
    p2_key_left = ord(raw_input('Player 2 left\n>> '))
    p2_key_right = ord(raw_input('Player 2 right\n>> '))
    p2_key_up = ord(raw_input('Player 2 up\n>> '))
    p2_key_down = ord(raw_input('Player 2 crouch\n>> '))
    p2_key_punch = ord(raw_input('Player 2 punch\n>> '))
    p2_key_kick = ord(raw_input('Player 2 kick\n>> '))
    
    print 'P1 Left:  ' + chr(p1_key_left) + '\nP1 Right: ' + chr(p1_key_right) + '\nP1 Up:    ' + chr(p1_key_up) + '\nP1 Down:  ' + chr(p1_key_down) + '\nP1 Punch: ' + chr(p1_key_punch) + '\nP1 Kick:  ' + chr(p1_key_kick)
    print
    print 'P2 Left:  ' + chr(p2_key_left) + '\nP2 Right: ' + chr(p2_key_right) + '\nP2 Up:    ' + chr(p2_key_up) + '\nP2 Down:  ' + chr(p2_key_down) + '\nP2 Punch: ' + chr(p2_key_punch) + '\nP2 Kick:  ' + chr(p2_key_kick)
    print
    
    confirm = (raw_input('Is this correct?\n>> ')).lower()
    if confirm == 'n' or confirm == 'no':
        values()
    if confirm == 'y' or confirm == 'yes':
        player1_controls = [p1_key_left, p1_key_right, p1_key_up, p1_key_down, p1_key_punch, p1_key_kick]
        player2_controls = [p2_key_left, p2_key_right, p2_key_up, p2_key_down, p2_key_punch, p2_key_kick]
        controls = [player1_controls, player2_controls]
        return controls
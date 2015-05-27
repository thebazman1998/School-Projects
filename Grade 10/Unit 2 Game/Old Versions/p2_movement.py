'''
Created on May 5, 2014

@author: Basil
'''
            if (player.left+player.right)/2 > (player2.right+player2.left)/2:        # P1 face right, P2 face left
                if player2.bottom >= 700:
                    if jump2Count > 20 and jump2Count < 28:
                        jump2Count += 1
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                    else:
                        jump2Count = 3
                    if not(move2Left or move2Right or punch2 or kick2):
                        if not(crouching2):
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Idle Stance/tmp-'+ str(idle2Count/5) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if idle2Count != 36*5:
                                idle2Count += 1
                            else:
                                idle2Count = 0
                        else:
                            player2Image = pygame.image.load('Graphics/Cvs Jin Crouch/tmp-'+ str(crouch2Count) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if crouch2Count < 2:
                                crouch2Count += 1
                    else:
                        if punch2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Punch/tmp-'+ str(punch2Count) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if punch2Count < 5:
                                punch2Count += 1
                            else:
                                punch2Count = 0
                                punch2 = False
                        elif kick2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Kick/tmp-'+ str(kick2Count/2) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if kick2Count < 6*2:
                                kick2Count += 1
                            else:
                                kick2Count = 0
                        # This '2'  |   was typed by Ian's little brother Martin Bantoto
                        #           v
                                kick2 = False
                        elif move2Right:
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking Back/tmp-'+ str(walk2Count) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if walk2Count < 10:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                        elif move2Left:
                            crouch2Count = 0
                            if walk2Count == 10:
                                walk2Count = 9
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking/tmp-'+ str(walk2Count) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if walk2Count < 9:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                else:
                    if move2Up:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                        if jump2Count < 8:
                            jump2Count += 1
                        elif jump2Count > 8:
                            jump2Count = 2
                    else:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                        if jump2Count < 21:
                            jump2Count += 1
                        
                if player2.bottom == 700:
                    player2Image = pygame.image.load('player2Right.png')
                    
            else:      # P1 face left, P2 face right
                if player2.bottom >= 700:
                    if jump2Count > 20 and jumpCount < 28:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                        jump2Count += 1
                    else:
                        jump2Count = 3
                    if not(move2Left or move2Right or punch2 or kick2):
                        if not(crouching2):
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Idle Stance/tmp-'+ str(idle2Count/5) + '.gif')
                            if idle2Count != 36*5:
                                idle2Count += 1
                            else:
                                idle2Count = 0
                        else:
                            player2Image = pygame.image.load('Graphics/Cvs Jin Crouch/tmp-'+ str(crouch2Count) + '.gif')
                            if crouch2Count < 2:
                                crouch2Count += 1
                    else:
                        if punch2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Punch/tmp-'+ str(punch2Count) + '.gif')
                            if punch2Count < 5:
                                punch2Count += 1
                            else:
                                punch2Count = 0
                                punch2 = False
                        elif kick2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Kick/tmp-'+ str(kick2Count/2) + '.gif')
                            if kick2Count < 6*2:
                                kick2Count += 1
                            else:
                                kick2Count = 0
                                kick2 = False
                        elif move2Left:
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking Back/tmp-'+ str(walk2Count) + '.gif')
                            if walk2Count < 10:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                        elif move2Right:
                            crouch2Count = 0
                            if walk2Count == 10:
                                walk2Count = 9
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking/tmp-'+ str(walk2Count) + '.gif')
                            if walk2Count < 9:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                else:
                    if move2Up:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        if jump2Count < 8:
                            jump2Count += 1
                        elif jump2Count > 8:
                            jump2Count = 2
                    else:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        if jump2Count < 21:
                            jump2Count += 1
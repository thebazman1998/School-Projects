import pygame, sys, KeyConfig
pygame.init()

# Get controls
controls = KeyConfig.main()

player1_controls = controls[0]
player2_controls = controls[1]

# Assign movement controls
p1l = player1_controls[0]
p1r = player1_controls[1]
p1u = player1_controls[2]
p1d = player1_controls[3]

p2l = player2_controls[0]
p2r = player2_controls[1]
p2u = player2_controls[2]
p2d = player2_controls[3]

# Assign combat controls
p1p = player1_controls[4]
p1k = player1_controls[5]

p2p = player2_controls[4]
p2k = player2_controls[5]

def start():
    
    screen = pygame.display.set_mode([1280,700])
    
    pygame.display.set_caption("START")
    done = False
    
    rail = pygame.Rect(0, 0, 1280, 150)
    
    while not done:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            
            if event.type == pygame.KEYDOWN:
                done = True
            
            screen.fill((0,0,0))
            
            back = pygame.Rect(0, 0, 700, 1280)
            backImage = pygame.image.load('Background.jpg')
            backStretched = pygame.transform.scale(backImage, (1280, 700))
            
            if rail.bottom < 750:
                rail.bottom += 25
            
            railImage = pygame.image.load('Railing Transparent.png')
            railStretched = pygame.transform.scale(railImage, (1280, 150))
            
            screen.blit(backStretched,back)
            screen.blit(railStretched,rail)
            
            pygame.display.flip()


def play():
    
    back = pygame.Rect(0, 0, 700, 1280)
    backImage = pygame.image.load('Background.jpg')
    backStretched = pygame.transform.scale(backImage, (1280, 700))
    
    rail = pygame.Rect(0, 600, 1280, 150)
    railImage = pygame.image.load('Railing Transparent.png')
    railStretched = pygame.transform.scale(railImage, (1280, 150))

    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = True
    jump = True
    punch = False
    kick = False
    crouching = False
    moving = (moveLeft or moveRight or moveUp or moveDown)
    
    move2Left = False
    move2Right = False
    move2Up = False
    move2Down = True
    jump2 = True
    punch2 = False
    kick2 = False
    crouching2 = False
    moving2 = (move2Left or move2Right or move2Up or move2Down)
    
    pHei = 180
    pWid  = 80
    
    player = pygame.Rect(560-pWid, 600-pHei, pWid, pHei)
    playerImage = pygame.image.load('Graphics/Cvs Asuka Idle Stance Right/tmp-2.gif')
    playerStretchedImage = pygame.transform.scale(playerImage, (pWid, pHei))
    
    p1BoxVul = player

    p1 = 90
    
    player2 = pygame.Rect(720+pWid, 600-pHei, pWid, pHei)
    player2Image = pygame.image.load('player2Left.png')
    player2StretchedImage = pygame.transform.scale(player2Image, (pWid, pHei))
    
    p2BoxVul = player2
    
    p2 = 90
    
    crouchCount = 0
    idleCount = 0
    jumpCount = 18
    walkCount = 0
    punchCount = 0
    kickCount = 0
    
    screen = pygame.display.set_mode([1280,700])
    
    pygame.display.set_caption("PLAY")
    
    clock = pygame.time.Clock()
    restart = pygame.K_r

    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = 1
                    screen = pygame.display.set_mode([1280,700])
                    while loop == 1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    loop = 0
                                    
                        pygame.display.flip()
                        
                        if p1 > 0:
                            screen.blit(board,boardBox)
                        if p2 > 0:
                            screen.blit(board2,board2Box)
                        
                        if p1 > 0:
                            screen.blit(playerStretchedImage, player)
        
                        if p2 > 0:
                            screen.blit(player2StretchedImage, player2)
                            
                        screen.blit(railStretched,rail)
                            
                        pause1 = pygame.Rect((640-60,240),(40,100))
                        pause2 = pygame.Rect((640+60,240),(40,100))

                        pygame.draw.rect(screen, (255,255,255), pause1)
                        pygame.draw.rect(screen, (255,255,255), pause2)
                                    
                        if loop == 0:
                            break
                        else:
                            continue
                        
                        pygame.display.flip()
                                
                if event.key == p1u:               # If p1 tries to move up
                    if p1 > 0 and moveUp == False:
                        if jump == False:
                            moveUp = True
                            jump = True
                            moveDown = False
                
                elif event.key == p1p:
                    if p1 > 0 and not(move2Up or crouching):
                        punch = True
                        crouching = False
                
                elif event.key == p1k:
                    if p1 > 0 and not(moveUp or crouching):
                        kick = True
                        crouching = False
                                    
                if event.key == p2u:               # If p2 tries to move up
                    if p2 > 0 and move2Up == False:
                        if jump2 == False:
                            move2Up = True
                            jump2 = True
                            move2Down = False
                
                elif event.key == p2p:
                    if p2 > 0 and not(move2Up or crouching2):
                        punch2 = True
                
                elif event.key == p2k:
                    if p2 > 0 and not(move2Up or crouching2):
                        kick2 = True
                        
                elif pygame.key == restart:
                    play()                
                    
            if event.type == pygame.KEYUP:         # Disable horizontal movement
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if p1 > 0:                        # If p1 lets go of a key
                    if jump:
                        pass
                    else:
                        if event.key == p1l:
                            moveLeft = False
                            moveRight = False
                        if event.key == p1r:
                            moveRight = False
                            moveLeft = False
                if p2 > 0:                        # If p2 lets go of a key
                    if jump2:
                        pass
                    else:
                        if event.key == p2l:
                            move2Left = False
                            move2Right = False
                        if event.key == p2r:
                            move2Right = False
                            move2Left = False
        
        screen.fill((0,0,0))        
        #screen.blit(backStretched,back)
        
        # Display Health Bars
        
        board = pygame.image.load('Graphics/Health Bar/Health Bar '+ str(p1) + '.gif')
        board = pygame.transform.scale(board, (600, 100))
        
        boardBox = pygame.Rect((10,10),(1,1))
        
        board2 = pygame.image.load('Graphics/Health Bar/Health Bar '+ str(p2) + '.gif')
        board2 = pygame.transform.flip(board2,1,0)
        board2 = pygame.transform.scale(board2, (600, 100))
        
        board2Box = pygame.Rect((660,10),(1,1))
        
        screen.blit(board,boardBox)
        screen.blit(board2,board2Box)
        
        # Try to move Characters
        
        keys = pygame.key.get_pressed()
        
        if p1 > 0:
            if keys[p1d]:
                crouching = True
                moveRight = False
                moveLeft = False
            else:
                crouching = False
            if not(crouching):
                if keys[p1l]:
                    if player.top > pHei:
                        if punch or kick:
                            pass
                        else:
                            moveLeft = True
                            moveRight = False
                    else:
                        moveRight = False
                        moveLeft = True
                elif keys[p1r]:
                    if player.top > pHei:
                        if punch or kick:
                            pass
                        else:
                            moveRight = True
                            moveLeft = False
                    else:
                        moveLeft = False
                        moveRight = True
        if p2 > 0:
            if keys[p2d]:
                crouching2 = True
                move2Right = False
                move2Left = False
            else:
                crouching2 = False
            if not(crouching):
                if keys[p2l]:
                    if player2.top > pHei:
                        if punch2 or kick2:
                            pass
                        else:
                            move2Left = True
                            move2Right = False
                    else:
                        move2Right = False
                        move2Left = True
                elif keys[p2r]:
                    if player2.top > pHei:
                        if punch2 or kick2:
                            pass
                        else:
                            move2Right = True
                            move2Left = False
                    else:
                        move2Left = False
                        move2Right = True
        
        # Move Characters
        
        if p1 > 0:
            if moveDown and player.bottom < 700:
                player.top += 20
            if player.bottom == 700:
                jump = False
                moveDown = False
            if moveUp and player.top > 0:
                if player.top < 240:
                    moveUp = False
                    moveDown = True
                else:
                    player.top -= 20
            if moveLeft and not(punch or kick):
                if player.left > 0:
                    if not(p1BoxVul.colliderect(p2BoxVul)):
                        player.left -= 10
                    else:
                        player.left += 5
                        player2.left -= 5
                        moveLeft = False
                else:
                    moveLeft = False
                    moveRight = True
            if moveRight and not(punch or kick):
                if player.right < 1280:
                    if not(p1BoxVul.colliderect(p2BoxVul)):
                        player.left += 10
                    else:
                        player.left -= 5
                        player2.left += 5
                        moveRight = False
                else:
                    moveRight = False
                    moveLeft = True
        if p2 > 0:
            if move2Down and player2.bottom < 700:
                player2.top += 20
            if player2.bottom == 700:
                jump2 = False
                move2Down = False
            if move2Up and player2.top > 0:
                if player2.top < 240:
                    move2Up = False
                    move2Down = True
                else:
                    player2.top -= 20
            if move2Left and not(punch2 or kick2):
                if player2.left > 0:
                    if not(p2BoxVul.colliderect(p1BoxVul)):
                        player2.left -= 10
                    else:
                        player2.left += 5
                        player.left -= 5
                        move2Left = False
                else:
                    move2Left = False
                    move2Right = True

            if move2Right:
                if not(punch2 or kick2):
                    if player2.right < 1280:
                        if not(p2BoxVul.colliderect(p1BoxVul)):
                            player2.left += 10
                        else:
                            player2.left -= 5
                            player.left += 5
                            move2Left = True
                    else:
                        move2Right = False
                        move2Left = True
            
        # Animate sprites
        
        if p1 > 0 and p2 > 0:
            if (player.left+player.right)/2 > (player2.right+player2.left)/2:        # P1 face right, P2 face left
                if player.bottom >= 700:
                    if jumpCount > 20 and jumpCount < 28:
                        jumpCount += 1
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                    else:
                        jumpCount = 3
                    if not(moveLeft or moveRight or punch or kick):
                        if not(crouching):
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Idle Stance Right/tmp-'+ str(idleCount/5) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if idleCount != 36*5:
                                idleCount += 1
                            else:
                                idleCount = 0
                        else:
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Crouch Right/tmp-'+ str(crouchCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if crouchCount < 2:
                                crouchCount += 1
                    else:
                        if punch:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Punch Right/tmp-'+ str(punchCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if punchCount < 5:
                                punchCount += 1
                            else:
                                punchCount = 0
                                punch = False
                        elif kick:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Kick Right/tmp-'+ str(kickCount/2) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if kickCount < 6*2:
                                kickCount += 1
                            else:
                                kickCount = 0
                                kick = False
                        elif moveRight:
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Back Right/tmp-'+ str(walkCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if walkCount < 10:
                                walkCount += 1
                            else:
                                walkCount = 0
                        elif moveLeft:
                            crouchCount = 0
                            if walkCount == 10:
                                walkCount = 9
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Right/tmp-'+ str(walkCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if walkCount < 9:
                                walkCount += 1
                            else:
                                walkCount = 0
                else:
                    if moveUp:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                        if jumpCount < 8:
                            jumpCount += 1
                        elif jumpCount > 8:
                            jumpCount = 2
                    else:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                        if jumpCount < 21:
                            jumpCount += 1
                        
                if player2.bottom == 700:
                    player2Image = pygame.image.load('player2Right.png')
                    
            else:      # P1 face left, P2 face right
                if player.bottom >= 700:
                    if jumpCount > 20 and jumpCount < 28:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                        jumpCount += 1
                    else:
                        jumpCount = 3
                    if not(moveLeft or moveRight or punch or kick):
                        if not(crouching):
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Idle Stance Right/tmp-'+ str(idleCount/5) + '.gif')
                            if idleCount != 36*5:
                                idleCount += 1
                            else:
                                idleCount = 0
                        else:
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Crouch Right/tmp-'+ str(crouchCount) + '.gif')
                            if crouchCount < 2:
                                crouchCount += 1
                    else:
                        if punch:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Punch Right/tmp-'+ str(punchCount) + '.gif')
                            if punchCount < 5:
                                punchCount += 1
                            else:
                                punchCount = 0
                                punch = False
                        elif kick:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Kick Right/tmp-'+ str(kickCount/2) + '.gif')
                            if kickCount < 6*2:
                                kickCount += 1
                            else:
                                kickCount = 0
                                kick = False
                        elif moveLeft:
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Back Right/tmp-'+ str(walkCount) + '.gif')
                            if walkCount < 10:
                                walkCount += 1
                            else:
                                walkCount = 0
                        elif moveRight:
                            crouchCount = 0
                            if walkCount == 10:
                                walkCount = 9
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Right/tmp-'+ str(walkCount) + '.gif')
                            if walkCount < 9:
                                walkCount += 1
                            else:
                                walkCount = 0
                else:
                    if moveUp:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        if jumpCount < 8:
                            jumpCount += 1
                        elif jumpCount > 8:
                            jumpCount = 2
                    else:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        if jumpCount < 21:
                            jumpCount += 1
                            
                if player2.bottom == 700:
                    player2Image = pygame.image.load('player2Left.png')
            
        # Draw player characters

        if moveUp or moveDown or punch:
            playerStretchedImage = pygame.transform.scale(playerImage, (pWid+15, pHei+20))
        elif kick:
            playerStretchedImage = pygame.transform.scale(playerImage, (pWid+40, pHei+20))
        elif jump:
            playerStretchedImage = pygame.transform.scale(playerImage, (pWid+15, pHei+20))
        else:
            playerStretchedImage = pygame.transform.scale(playerImage, (pWid, pHei))
            
        if move2Up or move2Down or punch2:
            player2StretchedImage = pygame.transform.scale(player2Image, (pWid, pHei))
        elif kick2:
            player2StretchedImage = pygame.transform.scale(player2Image, (pWid, pHei))
        elif jump2:
            player2StretchedImage = pygame.transform.scale(player2Image, (pWid, pHei))
        else:
            player2StretchedImage = pygame.transform.scale(player2Image, (pWid, pHei))
            
        # Adjust Vulnerable Hitboxes
        
        if player.bottom == 700:
            if crouching:
                if crouchCount == 2:
                    p1BoxVul = pygame.Rect((player.left,player.top+(pHei/3)),(pWid,(2*pHei)/3))
                elif crouchCount == 1:
                    p1BoxVul = pygame.Rect((player.left,player.top+(pHei/6)),(pWid,(5*pHei)/6))
                else:
                    pass
            elif punch:
                if punchCount < 2:
                    p1BoxVul = pygame.Rect((player.left+(pWid/3),player.top),((2*pWid)/3,pHei))
                else:
                    p1BoxVul = pygame.Rect((player.left+(pWid/4),player.top),((5*pWid)/7,pHei))
            elif kick:
                if kickCount < 5 and kickCount > 0:
                    if p1BoxVul.right < p2BoxVul.left:
                        p1BoxVul = pygame.Rect((player.left-(pWid/8)+30,player.top),((5*pWid)/6-30,pHei))
                    elif p2BoxVul.right < p1BoxVul.left:
                        p1BoxVul = pygame.Rect((player.left+((3*pWid)/4)+20,player.top),((5*pWid)/6-20,pHei))
                else:
                    if p1BoxVul.right < p2BoxVul.left:
                        p1BoxVul = pygame.Rect((player.left-(pWid/8)+10,player.top),((5*pWid)/6-10,pHei))
                    elif p2BoxVul.right < p1BoxVul.left:
                        p1BoxVul = pygame.Rect((player.left+((3*pWid)/4),player.top),((5*pWid)/6-20,pHei))
            else:
                p1BoxVul = player
        
        if player2.bottom == 700:
            if crouching2:
                pass
            elif punch2:
                pass
            elif kick2:
                pass
            else:
                p2BoxVul = player2
        
        if not(jump):
            pygame.draw.rect(screen, (0,50,0), p1BoxVul)
        if not(jump2):
            pygame.draw.rect(screen, (0,50,0), p2BoxVul)
        
        if p1 > 0:
            screen.blit(playerStretchedImage, player)
        if p2 > 0:
            screen.blit(player2StretchedImage, player2)

        # Draw Railing
            
        screen.blit(railStretched,rail)
        
        # Update display
        
        pygame.display.flip()
        
        clock.tick(45)

def paused(p1, p2, p1Image, p2Image):
    
    size = [1280, 700]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("PAUSED")
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if pygame.KEYDOWN:
                if pygame.key == pygame.K_SPACE:
                    break
                
        screen.fill((0,0,0))
        
        pygame.display.flip()
        
#start()
play()
import pygame, time

pygame.init()
pygame.mixer.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
  
pygame.display.set_caption("Beep music")

done = False
clock = pygame.time.Clock()

while not done:
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a_punch = pygame.mixer.Sound("Audio/Asuka_Punch.wav")
                a_punch.play()
            elif event.key == pygame.K_d:
                a_kick = pygame.mixer.Sound("Audio/Asuka_Kick.wav")
                a_kick.play()
            elif event.key == pygame.K_w:
                a_jump = pygame.mixer.Sound("Audio/Asuka_Jump.wav")
                a_jump.play()
            elif event.key == pygame.K_LEFT:
                j_punch = pygame.mixer.Sound("Audio/Jin_Punch.wav")
                j_punch.play()
            elif event.key == pygame.K_RIGHT:
                j_kick = pygame.mixer.Sound("Audio/Jin_Kick.wav")
                j_kick.play()
            elif event.key == pygame.K_UP:
                j_jump = pygame.mixer.Sound("Audio/Jin_Jump.wav")
                j_jump.play()
    
    screen.fill((0,0,0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
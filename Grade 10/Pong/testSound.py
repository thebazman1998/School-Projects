import pygame, time

pygame.init()
pygame.mixer.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
  
pygame.display.set_caption("Beep music")

done = False
clock = pygame.time.Clock()

count = 1

while not done:
    
    #if count > 50000000001:
        #count += 1
    #else:
        #count = 1
    
    beep = pygame.mixer.Sound("beep.ogg")
    peep = pygame.mixer.Sound("peep.ogg")
    plop = pygame.mixer.Sound("plop.ogg")
    
    #if count == 1 or count == 40000000001:
        #plop.play()
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                beep.play()
            elif event.key == pygame.K_RIGHT:
                peep.play()
            elif event.key == pygame.K_DOWN:
                plop.play()
    
    screen.fill((0,0,0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame, sys

start1 = pygame.image.load('Graphics/Start Screen1.jpg')
start2 = pygame.image.load('Graphics/Start Screen2.jpg')

start1 = pygame.transform.scale(start1, (1280, 700))
start2 = pygame.transform.scale(start2, (1280, 700))

loc1 = pygame.Rect(0, 0, 1, 1)

def shatter():
    
    screen = pygame.display.set_mode([1280,700])
    
    pygame.display.set_caption("START")
    
    clock = pygame.time.Clock()
    
    done = False
    frameCount = 0
    
    while not done:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            
            frame = pygame.image.load('Graphics/Title Screen Shatter/Title Screen Shatter_000'+str(frameCount)+'.jpg')
            frame = pygame.transform.scale(frame, (1280, 700))
            
            screen.blit(frame,loc1)
            
            pygame.display.flip()
            
            frameCount += 1
            if frameCount > 15:
                break
            
            clock.tick(5)

shatter()
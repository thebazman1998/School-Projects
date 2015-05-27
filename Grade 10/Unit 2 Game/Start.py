'''
Created on May 10, 2014

@author: basil
'''

import pygame, sys

start1 = pygame.image.load('Graphics/Start Screen (No Click).jpg')
start2 = pygame.image.load('Graphics/Start Screen (With Click).jpg')

start1 = pygame.transform.scale(start1, (1280, 700))
start2 = pygame.transform.scale(start2, (1280, 700))

loc1 = pygame.Rect(0, 0, 1, 1)

def start():
    
    screen = pygame.display.set_mode([1280,700])
    
    pygame.display.set_caption("START")
    
    clock = pygame.time.Clock()
    
    done = False
    
    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
                
            screen.blit(start1, loc1)
            
            pygame.display.flip()

            screen.blit(start2, loc1)
            
            clock.tick(4)
            
            pygame.display.flip()
            
start()
'''
Created on Apr 16, 2014

@author: Basil
'''

import pygame, sys, random
from pygame.locals import *

def rand_color(color):
    if color == "red":
        r = random.randint(0, 255)
        g = 0
        b = 0
    elif color == "green":
        r = 0
        g = random.randint(0, 255)
        b = 0
    elif color == "blue":
        r = 0
        g = 0
        b = random.randint(0, 255)
    elif color == "grey":
        r = random.randint(0, 255)
        g = r
        b = r
    else:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    
    end_color = (r, g, b)
    return end_color

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


# set up pygame
pygame.init()
mainClock = pygame.time.Clock()
tick = 100
pause = False

# set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Basil Animation (Press "Esc" to pause, and 0-9 for game speed: 0 is fast, 9 is slow)')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

# set up the colors
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# WHITE = (255, 255, 255)

# set up the bouncer and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
bouncer = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':UPLEFT}
bouncer2 = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':DOWNLEFT}
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tick = 100
            elif event.key == pygame.K_2:
                tick = 90
            elif event.key == pygame.K_3:
                tick = 80
            elif event.key == pygame.K_4:
                tick = 70
            elif event.key == pygame.K_5:
                tick = 60
            elif event.key == pygame.K_6:
                tick = 50
            elif event.key == pygame.K_7:
                tick = 40
            elif event.key == pygame.K_8:
                tick = 30
            elif event.key == pygame.K_9:
                tick = 20
            elif event.key == pygame.K_0:
                tick = 0
            elif event.key == pygame.K_ESCAPE:
                pause = True
        while pause == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit() 
                    

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # draw the black background onto the surface
    windowSurface.fill(rand_color("grey"))

    # move the bouncer data structure
    if bouncer2['dir'] == DOWNLEFT:
        bouncer2['rect'].left -= MOVESPEED
        bouncer2['rect'].top += MOVESPEED
    if bouncer2['dir'] == DOWNRIGHT:
        bouncer2['rect'].left += MOVESPEED
        bouncer2['rect'].top += MOVESPEED
    if bouncer2['dir'] == UPLEFT:
        bouncer2['rect'].left -= MOVESPEED
        bouncer2['rect'].top -= MOVESPEED
    if bouncer2['dir'] == UPRIGHT:
        bouncer2['rect'].left += MOVESPEED
        bouncer2['rect'].top -= MOVESPEED

    # check if the bouncer2 has move out of the window
    if bouncer2['rect'].top < 0:
        # bouncer2 has moved past the top
        if bouncer2['dir'] == UPLEFT:
            bouncer2['dir'] = DOWNLEFT
        if bouncer2['dir'] == UPRIGHT:
            bouncer2['dir'] = DOWNRIGHT
    if bouncer2['rect'].bottom > WINDOWHEIGHT:
        # bouncer2 has moved past the bottom
        if bouncer2['dir'] == DOWNLEFT:
            bouncer2['dir'] = UPLEFT
        if bouncer2['dir'] == DOWNRIGHT:
            bouncer2['dir'] = UPRIGHT
    if bouncer2['rect'].left < 0:
        # bouncer2 has moved past the left side
        if bouncer2['dir'] == DOWNLEFT:
            bouncer2['dir'] = DOWNRIGHT
        if bouncer2['dir'] == UPLEFT:
            bouncer2['dir'] = UPRIGHT
    if bouncer2['rect'].right > WINDOWWIDTH:
        # bouncer2 has moved past the right side
        if bouncer2['dir'] == DOWNRIGHT:
            bouncer2['dir'] = DOWNLEFT
        if bouncer2['dir'] == UPRIGHT:
            bouncer2['dir'] = UPLEFT

    # draw the bouncer2 onto the surface
    pygame.draw.rect(windowSurface, rand_color("red"), bouncer2['rect'])

    # move the bouncer data structure
    if bouncer['dir'] == DOWNLEFT:
        bouncer['rect'].left -= MOVESPEED
        bouncer['rect'].top += MOVESPEED
    if bouncer['dir'] == DOWNRIGHT:
        bouncer['rect'].left += MOVESPEED
        bouncer['rect'].top += MOVESPEED
    if bouncer['dir'] == UPLEFT:
        bouncer['rect'].left -= MOVESPEED
        bouncer['rect'].top -= MOVESPEED
    if bouncer['dir'] == UPRIGHT:
        bouncer['rect'].left += MOVESPEED
        bouncer['rect'].top -= MOVESPEED

    # check if the bouncer has move out of the window
    if bouncer['rect'].top < 0:
        # bouncer has moved past the top
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = DOWNLEFT
        if bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = DOWNRIGHT
    if bouncer['rect'].bottom > WINDOWHEIGHT:
        # bouncer has moved past the bottom
        if bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = UPLEFT
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = UPRIGHT
    if bouncer['rect'].left < 0:
        # bouncer has moved past the left side
        if bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = DOWNRIGHT
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = UPRIGHT
    if bouncer['rect'].right > WINDOWWIDTH:
        # bouncer has moved past the right side
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = DOWNLEFT
        if bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = UPLEFT
    
    # If Bouncer hits Bouncer2
    if doRectsOverlap(bouncer['rect'], bouncer2['rect']):
        if bouncer['dir'] == UPLEFT:
            if bouncer2['dir'] == UPRIGHT:
                bouncer['dir'] = UPRIGHT
                bouncer2['dir'] = UPLEFT
            elif bouncer2['dir'] == DOWNRIGHT:
                bouncer['dir'] = DOWNRIGHT
                bouncer2['dir'] = UPLEFT

    # draw the bouncer onto the surface
    pygame.draw.rect(windowSurface, rand_color("red"), bouncer['rect'])

    # check if the bouncer has intersected with any food squares.
    for food in foods[:]:
        if doRectsOverlap(bouncer['rect'], food):
            foods.remove(food)
        elif doRectsOverlap(bouncer2['rect'], food):
            foods.remove(food)

    # draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, rand_color("blue"), foods[i])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(tick)
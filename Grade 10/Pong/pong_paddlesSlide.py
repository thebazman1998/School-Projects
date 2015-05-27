import pygame

pygame.init()

size = [900, 600]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

pygame.display.set_caption("Pong")

x1 = 0
y1 = 0

x2 = 10
y2 = 250

x3 = 870
y3 = 250

way = 'right'
height = 'down'

d2 = ''
d3 = ''

while not done:

    for event in pygame.event.get(): # User did something
        
        key=pygame.key.get_pressed()
        
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                d2 = ''
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                d3 = ''
        
        if key[pygame.K_w]:
            if y2 == 0:
                d2 = ''
            else:
                d2 = 'up'
        elif key[pygame.K_s]:
            if y2 == 500:
                d2 = ''
            else:
                d2 = 'down'
        
        if key[pygame.K_UP]:
            if y3 == 0:
                d3 = ''
            else:
                d3 = 'up'
        elif key[pygame.K_DOWN]:
            if y3 == 500:
                d3 = ''
            else:
                d3 = 'down'

    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255,255,255), [x2, y2, 20, 100])
    pygame.draw.rect(screen, (255,255,255), [x3, y3, 20, 100])
    pygame.draw.rect(screen, (255,255,255), [x1, y1, 20, 20])
    
    if d2 == '':
        pass
    elif d2 == 'up':
        if y2 > 1:
            y2 -= 10
        else:
            d2 = ''
    elif d2 == 'down':
        if y2 < 500:
            y2 += 10
        else:
            d2 = ''
    if d3 == '':
        pass
    elif d3 == 'up':
        if y3 > 1:
            y3 -= 10
        else:
            d3 = ''
    elif d3 == 'down':
        if y3 < 500:
            y3 += 10
    
    if way == 'right':
        if x1 < 860:
            x1 += 10
        elif x1 == 860:
            #
            x1 -= 10
            way = 'left'
    
    elif way == 'left':
        if x1 > 20:
            x1 -= 10
        elif x1 == 20:
            #
            x1 += 10
            way = 'right'
    
    if height == 'down':
        if y1 < 580:
            y1 += 10
        elif y1 == 580:
            y1 -= 10
            height = 'up'
    
    elif height == 'up':
        if y1 > 0:
            y1 -= 10
        elif y1 == 0:
            y1 += 10
            height = 'down'
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

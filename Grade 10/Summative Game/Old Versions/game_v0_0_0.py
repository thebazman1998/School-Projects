import pygame, sys

pygame.init()
pygame.mixer.init()

# Controls

n1, n2, n3, n4 = ord("1"), ord("q"), ord("a"), ord("z")
start = ord("6")

clock = pygame.time.Clock()

def play(song, diff):
    
    # Variables
    
    k1, k2, k3, k4, k5 = False, False, False, False, False
    strumUp, strumDown, strum = False, False, False
    
    locx, locy = 400, 600
    
    box_k1, box_k2, box_k3 = pygame.Rect(locx,locy,100,60), pygame.Rect(locx+100,locy,100,60), pygame.Rect(locx+200,locy,100,60)
    box_k4, box_k5, box_k0 = pygame.Rect(locx+300,locy,100,60), pygame.Rect(locx+400,locy,100,60), pygame.Rect(locx,locy,500,60)
    
    barTick = 0
    
    s = open("Audio/song1.txt","r")
    
    bar = []
    for line in s:
        bar.append(line)
    
    # Images
    
    h1, h2, h3 = pygame.image.load("Graphics/keys_held/held_1.png"), pygame.image.load("Graphics/keys_held/held_2.png"), pygame.image.load("Graphics/keys_held/held_3.png")
    h4, h5, h0 = pygame.image.load("Graphics/keys_held/held_4.png"), pygame.image.load("Graphics/keys_held/held_5.png"), pygame.image.load("Graphics/frets_blank.png")
    
    # Audio

    pygame.display.set_caption("Playing song")
    
    pygame.mixer.music.load("Audio/song"+song+".ogg")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.4)

    beep = pygame.mixer.Sound("beep.ogg")
    
    # Necessary Stuff
    
    screen = pygame.display.set_mode([1280,700])
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    strumUp = True
                elif event.key == pygame.K_DOWN:
                    strumDown = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LALT:
                    k5 = False
        
        screen.fill((255,255,255))
            
        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        
        # Keys being held down
        
        if keys[pygame.K_ESCAPE]:
            k1 = True
        else:
            k1 = False
        
        if keys[pygame.K_F1]:
            k2 = True
        else:
            k2 = False
        
        if keys[pygame.K_F2]:
            k3 = True
        else:
            k3 = False
        
        if keys[pygame.K_F3]:
            k4 = True
        else:
            k4 = False
        
        if keys[pygame.K_F4]:
            k5 = True
        else:
            k5 = False
        
        pygame.draw.rect(screen, (0,0,0), box_k0)
        
        screen.blit(h0,box_k0)
            
        # Display if notes are being held
        
        if k1:
            screen.blit(h1,box_k1)
        
        if k2:
            screen.blit(h2,box_k2)
        
        if k3:
            screen.blit(h3,box_k3)
        
        if k4:
            screen.blit(h4,box_k4)
        
        if k5:
            screen.blit(h5,box_k5)
        
        strum = (strumUp or strumDown)
        
        if strum and (k1 or k2 or k3 or k4 or k5):
            beep.play()
            
        if barTick < 240:
            barTick += 1
        else:
            barTick = 0
        
        strumUp, strumDown = False, False
        
        pygame.display.flip()
        clock.tick(30)
        
# Main

print
print "Songs"
print
print "1. Back in Black"
print "2. "
print "3. "
print

backSong = str(input("Which song would you like to play? "))

print
print "Difficulty"
print
print "1. Medium: 4 notes"
print "2. Hard: 5 notes"
print

diffSong = str(input("What difficulty? "))
        
play(backSong,diffSong)
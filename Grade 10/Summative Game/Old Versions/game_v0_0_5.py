import pygame, sys

pygame.init()
pygame.mixer.init()

# Controls

n1, n2, n3, n4 = ord("1"), ord("q"), ord("a"), ord("z")
start = ord("6")

clock = pygame.time.Clock()

def songSelect():
    print
    print "Songs"
    print
    print "1. Back in Black"
    print "2. "
    print "3. "
    print
    
    backSong = str(input("Which song would you like to play? "))
    
    if backSong == 1:
        bpm = 90
        beat = 8
    else:
        bpm = 60
        beat = 4
    
    print
    print "Difficulty"
    print
    print "1. Medium: 4 notes"
    print "2. Hard: 5 notes"
    print
    
    diffSong = str(input("What difficulty? "))
    
    return [backSong, diffSong, beat, bpm]

def start():
    
    screen = pygame.display.set_mode([1280,700])
    done = False
    
    while not(done):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
            if event.type == pygame.KEYDOWN:
                play(backSong,diffSong,maxBeat,bpm)
            if event.type == pygame.MOUSEBUTTONDOWN:
                play(backSong,diffSong,maxBeat,bpm)
                
        screen.fill((0,0,0))
        
        pygame.display.flip()

def play(song, diff, maxBeat, bpm):
    
    # Variables
    
    k1, k2, k3, k4, k5 = False, False, False, False, False
    track1, track2, track3, track4, track5 = [], [], [], [], []
    tracks = [track1, track2, track3, track4, track5]
    strumUp, strumDown = False, False
    strum = (strumUp or strumDown)
    
    locx, locy = 400, 600
    
    box_k1, box_k2, box_k3 = pygame.Rect(locx,locy,100,60), pygame.Rect(locx+100,locy,100,60), pygame.Rect(locx+200,locy,100,60)
    box_k4, box_k5, box_k0 = pygame.Rect(locx+300,locy,100,60), pygame.Rect(locx+400,locy,100,60), pygame.Rect(locx,locy,500,60)
    box_keys = pygame.Rect(locx,locy+15,500,25)
    
    barTick, beatTick, barCount, beatCount = 0, 0, 0, 0
    speed = int(diff) * 5
    
    toBePlayed = []
    
    s = open("Audio/song1.txt","r")
    
    bar = []
    for line in s:
        bar.append(line)
    
    # Images
    
    h1, h2, h3 = pygame.image.load("Graphics/keys_held/held_1.png"), pygame.image.load("Graphics/keys_held/held_2.png"), pygame.image.load("Graphics/keys_held/held_3.png")
    h4, h5, h0 = pygame.image.load("Graphics/keys_held/held_4.png"), pygame.image.load("Graphics/keys_held/held_5.png"), pygame.image.load("Graphics/frets_blank.png")
    
    p1, p2, p3 = pygame.image.load("Graphics/notes_reg/reg_1.png"), pygame.image.load("Graphics/notes_reg/reg_2.png"), pygame.image.load("Graphics/notes_reg/reg_3.png")
    p4, p5 = pygame.image.load("Graphics/notes_reg/reg_4.png"), pygame.image.load("Graphics/notes_reg/reg_5.png")
    
    # Audio

    pygame.display.set_caption("Playing song")
    
    pygame.mixer.music.load("Audio/song"+song+".ogg")
    pygame.mixer.music.play(-1, 1.0)
    pygame.mixer.music.set_volume(0.2)

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
        
        screen.fill((0,0,0))
            
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
        
        pygame.draw.rect(screen, (0,0,0), box_keys)
        
        screen.blit(h0,box_k0)
            
        # Display if frets are being held
        
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
        
        # Add notes from file to memory

        currentBar = bar[barCount]
        currentBar = currentBar.split("|")
        
        currentBar = currentBar[1:len(currentBar):2]
        currentBeat = currentBar[beatCount]
        
        if barCount < len(bar):
            
            if beatTick < 4:
                beatTick += 1
            else:
                add = True
                beatTick = 0
                if beatCount < 7:
                    beatCount += 1
                else:
                    beatCount = 0
        
            if barTick < 39:
                barTick += 1
            else:
                barCount += 1
                barTick = 0
            
        else:
            break
        
        if ("-" not in currentBeat) and add:
            if "1" in currentBeat:
                track1.append([400,0,100,60])
            if "2" in currentBeat:
                track2.append([500,0,100,60])
            if "3" in currentBeat:
                track3.append([600,0,100,60])
            if "4" in currentBeat:
                track4.append([700,0,100,60])
            if "5" in currentBeat:
                track5.append([800,0,100,60])
        
        add = False
        
        # Draw notes on track
        for i in toBePlayed:
            i[1] += speed
            if i[0] == 400:
                p = p1
            elif i[0] == 500:
                p = p2
            elif i[0] == 600:
                p = p3
            elif i[0] == 700:
                p = p4
            else:
                p = p5
            screen.blit(p,pygame.Rect(i[0],i[1],i[2],i[3]))
        for i1 in track1:
            i1[1] += speed
            screen.blit(p1,pygame.Rect(i1[0],i1[1],i1[2],i1[3]))
        for i2 in track2:
            i2[1] += speed
            screen.blit(p2,pygame.Rect(i2[0],i2[1],i2[2],i2[3]))
        for i3 in track3:
            i3[1] += speed
            screen.blit(p3,pygame.Rect(i3[0],i3[1],i3[2],i3[3]))
        for i4 in track4:
            i4[1] += speed
            screen.blit(p4,pygame.Rect(i4[0],i4[1],i4[2],i4[3]))
        for i5 in track5:
            i5[1] += speed
            screen.blit(p5,pygame.Rect(i5[0],i5[1],i5[2],i5[3]))
            
        # Detect if note is supposed to be played
        
        for track in tracks:
            for note in track:
                x = pygame.Rect(note[0],note[1],note[2],note[3])
                if x.colliderect(box_keys):
                    toBePlayed.append(note)
                    track.remove(note)
        if len(toBePlayed) > 0:
            note = toBePlayed[0]
            x = pygame.Rect(note[0],note[1],note[2],note[3])
            if not(x.colliderect(box_keys)) or strum:
                toBePlayed = []
                note = None
                    
        # Reset strumming

        strumUp, strumDown = False, False
        
        pygame.display.flip()
        clock.tick(60)

def songEnd():
    pass

# Main    

select = songSelect()
backSong, diffSong, maxBeat, bpm = select[0], select[1], select[2], select[3]
start()
play(backSong,diffSong,maxBeat,bpm)
songEnd()
import pygame, sys, time

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

def diffSelect():
    
    screen = pygame.display.set_mode([1280,700])
    pygame.display.set_caption("Choose Difficulty")
    font = pygame.font.Font("Graphics/poophead.ttf", 30)
    location1 = (500,200,250,80)
    select = location1
    done = False
    g = 0
    
    while not(done):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    break
                elif event.key == pygame.K_F1:
                    select == location1
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if select == location1:
                        g = 0
                        select = location2
                    else:
                        g = 0
                        select = location1
                        
        screen.fill((0,0,0))
        
        diffs = font.render("DIFFICULTIES",4,(255,255,255))
        
        diff1 = font.render("Intermediate",4,(255,255,255))
        diff2 = font.render("Expert",4,(255,255,255))
        
        location1 = (500,200,250,80)
        location2 = (500,350,250,80)
        
        screen.blit(diffs,(500,50,150,150))
        
        pygame.draw.rect(screen,(0,g,0),select)
        
        screen.blit(diff1,location1)
        screen.blit(diff2,location2)
        
        if g < 152:
            g += 3
        
        pygame.display.flip()
    
    if select == location1:
        return "1"
    else:
        return "2"

def songSelect():

    screen = pygame.display.set_mode([1280,700])
    pygame.display.set_caption("Choose Song")
    font = pygame.font.Font("Graphics/poophead.ttf", 30)
    location1 = (500,200,250,80)
    select = location1
    done = False
    g = 0
    
    while not(done):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    if select == location1:
                        return ["1",63,8,"Back In Black",7]
                    if select == location2:
                        return ["2",64,8,"About a Girl",7]
                    if select == location3:
                        return ["3",42,4,"About a Girl",10]
                    break
                elif event.key == pygame.K_F1:
                    main()
                elif event.key == pygame.K_UP:
                    if select == location1:
                        g = 0
                        select = location3
                    elif select == location2:
                        g = 0
                        select = location1
                    else:
                        g = 0
                        select = location2
                elif event.key == pygame.K_DOWN:
                    if select == location1:
                        g = 0
                        select = location2
                    elif select == location2:
                        g = 0
                        select = location3
                    else:
                        g = 0
                        select = location1
        
        screen.fill((0,0,0))
        
        songs = font.render("SONGS",4,(255,255,255))
        
        title1 = font.render("Back In Black",4,(255,255,255))
        title2 = font.render("About a Girl",4,(255,255,255))
        title3 = font.render("WIP",4,(255,255,255))
        
        location1 = (500,200,250,80)
        location2 = (500,350,250,80)
        location3 = (500,500,250,80)
        
        screen.blit(songs,(500,50,150,150))
        
        pygame.draw.rect(screen,(0,g,0),select)
        
        screen.blit(title1,location1)
        screen.blit(title2,location2)
        screen.blit(title3,location3)
        
        if g < 152:
            g += 3
        
        pygame.display.flip()

def start():
    
    screen = pygame.display.set_mode([1280,700])
    pygame.display.set_caption("Adjust window to be center of screen, then click anywhere or press any key")
    font = pygame.font.Font("Graphics/poophead.ttf", 30)
    done = False
    
    back1, back2 = pygame.image.load("Graphics/start1.png"), pygame.image.load("Graphics/start2.png")
    switchTick = 0
    
    back = back1
    
    while not(done):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        
        if switchTick < 5:
            switchTick += 1
        else:
            switchTick = 0
            if back == back1:
                back = back2
            else:
                back = back1
        
        screen.blit(back, pygame.Rect(0,0,0,0))
        
        pygame.display.flip()

def play(song, diff, bpm, maxBeat, name, speed):
    
    # Variables
    
    k1, k2, k3, k4, k5 = False, False, False, False, False
    show_hit1,show_hit2,show_hit3,show_hit4,show_hit5 = 0,0,0,0,0
    track1, track2, track3, track4, track5 = [], [], [], [], []
    track0 = []
    tracks = [track1, track2, track3, track4, track5]
    strumUp, strumDown = False, False
    strum = (strumUp or strumDown)
    
    locx, locy = 400, 600
    
    box_k1, box_k2, box_k3 = pygame.Rect(locx,locy,100,60), pygame.Rect(locx+100,locy,100,60), pygame.Rect(locx+200,locy,100,60)
    box_k4, box_k5, box_k0 = pygame.Rect(locx+300,locy,100,60), pygame.Rect(locx+400,locy,100,60), pygame.Rect(locx,locy,500,60)
    box_keys = pygame.Rect(locx,locy+10,500,34)
    
    barTick, beatTick, barCount, beatCount = 0, 0, 0, 0
    delay = 5*(bpm/60)
    
    toBePlayed, streaks = [], []
    notes, notesHit, noteStreak, score, newScore = 0, 0, 0, 0, 0
    lastHit = False
    streaks.append(noteStreak)
    highest = max(streaks)
    
    s = open("Audio/song"+str(song)+"_"+str(diff)+".txt","r")
    
    bar = []
    for line in s:
        bar.append(line)
        
    add = False
    
    # Images

    back = pygame.image.load("Graphics/back.jpg")
    
    held1, held2, held3 = pygame.image.load("Graphics/keys_held/held_1.png"), pygame.image.load("Graphics/keys_held/held_2.png"), pygame.image.load("Graphics/keys_held/held_3.png")
    held4, held5, held0 = pygame.image.load("Graphics/keys_held/held_4.png"), pygame.image.load("Graphics/keys_held/held_5.png"), pygame.image.load("Graphics/frets_blank.png")
    
    hit1, hit2, hit3 = pygame.image.load("Graphics/keys_hit/hit_1.png"), pygame.image.load("Graphics/keys_hit/hit_2.png"), pygame.image.load("Graphics/keys_hit/hit_3.png")
    hit4, hit5 = pygame.image.load("Graphics/keys_hit/hit_4.png"), pygame.image.load("Graphics/keys_hit/hit_5.png")
    
    note1, note2, note3 = pygame.image.load("Graphics/notes/reg_1.png"), pygame.image.load("Graphics/notes/reg_2.png"), pygame.image.load("Graphics/notes/reg_3.png")
    note4, note5 = pygame.image.load("Graphics/notes/reg_4.png"), pygame.image.load("Graphics/notes/reg_5.png")
    
    ham1, ham2, ham3 = pygame.image.load("Graphics/hams/ham_1.png"), pygame.image.load("Graphics/hams/ham_2.png"), pygame.image.load("Graphics/hams/ham_3.png")
    ham4, ham5 = pygame.image.load("Graphics/hams/ham_4.png"), pygame.image.load("Graphics/hams/ham_5.png")
    
    beatInd = pygame.image.load("Graphics/bar_indicator.png")
    
    setback = pygame.font.Font("Graphics/setbackt.ttf", 30)
    font = pygame.font.Font("Graphics/poophead.ttf", 30)
    
    r,g,b = 0,0,0
    
    # Audio

    pygame.display.set_caption("Playing "+name+"            Press F10 to toggle Dev mode")
    
    pygame.mixer.music.load("Audio/"+name+".ogg")
    
    pygame.mixer.music.play(0, 1.0)
    pygame.mixer.music.set_volume(1.0)
        
    paused = False
    
    # Necessary Stuff
    
    screen = pygame.display.set_mode([1280,700])
    dev = False
    
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
                elif event.key == pygame.K_RETURN:
                    pygame.mixer.music.pause()
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                                break
                            if event.type == pygame.KEYDOWN:
                                paused = not(paused)
                                pygame.mixer.music.unpause()
                elif event.key == pygame.K_F10:
                    dev = not(dev)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LALT:
                    k5 = False
                    
        if noteStreak <= 74:
            if r > 0:
                r -= 2
                if r < 0:
                    r = 0
            if g > 0:
                g -= 1
                if g < 0:
                    g = 0
            if b > 0:
                b -= 3
                if b < 0:
                    b = 0
            screen.fill((r,g,b))
        else:
            if r < 8:
                r += 1
            if g < 71:
                g += 1
            if b < 81:
                b += 1
            screen.fill((r,g,b))
            
        for i0 in track0:
            i0[1] += speed
            screen.blit(beatInd,pygame.Rect(i0[0],i0[1],i0[2],i0[3]))
            
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
        
        if keys[pygame.K_F5]:
            k5 = True
        else:
            k5 = False
        
        if dev:
            pygame.draw.rect(screen, (153,0,0), box_keys)
        
        screen.blit(held0,box_k0)
            
        # Display if frets are being held
        
        if k1:
            screen.blit(held1,box_k1)
        
        if k2:
            screen.blit(held2,box_k2)
        
        if k3:
            screen.blit(held3,box_k3)
        
        if k4:
            screen.blit(held4,box_k4)
        
        if k5:
            screen.blit(held5,box_k5)
        
        strum = (strumUp or strumDown)
        
        # Add notes from file to memory
        
        if barCount < len(bar):
            
            currentBar = bar[barCount]
            currentBar = currentBar.split("|")
            
            currentBar = currentBar[1:len(currentBar):2]
            currentBeat = currentBar[beatCount]
                
            if beatTick < 4:
                beatTick += 1
            else:
                add = True
                beatTick = 0
                if beatCount < maxBeat - 1:
                    beatCount += 1
                else:
                    beatCount = 0
    
            if barTick < 5 * (maxBeat) - 1:
                barTick += 1
            else:
                barCount += 1
                barTick = 0
            
        else:
            pygame.mixer.music.stop()
            songEnd(score,highest,name,notesHit,notes,song,diff,bpm,maxBeat,speed)
        
        if beatCount == 0 and beatTick == 0:
            track0.append([400,0,10,10])
        
        if ("-" not in currentBeat) and add:
            if "1" in currentBeat:
                track1.append([400,0,100,60,0])
                notes += 1
            if "2" in currentBeat:
                track2.append([500,0,100,60,0])
                notes += 1
            if "3" in currentBeat:
                track3.append([600,0,100,60,0])
                notes += 1
            if "4" in currentBeat:
                track4.append([700,0,100,60,0])
                notes += 1
            if "5" in currentBeat:
                track5.append([800,0,100,60,0])
                notes += 1
            if "q" in currentBeat:
                track1.append([400,0,100,60,1])
                notes += 1
            if "w" in currentBeat:
                track2.append([500,0,100,60,1])
                notes += 1
            if "e" in currentBeat:
                track3.append([600,0,100,60,1])
                notes += 1
            if "r" in currentBeat:
                track4.append([700,0,100,60,1])
                notes += 1
            if "t" in currentBeat:
                track5.append([800,0,100,60,1])
                notes += 1
        
        add = False
        
        # Draw text

        streaks.append(noteStreak)
        highest = max(streaks)
        
        textScore = font.render("SCORE: "+str(score),4,(255,255,255))
        textStreak = font.render("STREAK: "+str(noteStreak),4,(255,255,255))
        
        screen.blit(textScore, (50,370,50,100))
        screen.blit(textStreak, (50,420,50,100))
        
        if dev:
            textBeat = font.render("BEAT #"+str(barCount),4,(255,255,255))
            textHigh = font.render("HIGHEST: "+str(highest),4,(255,255,255))
            textNotes = font.render("NOTES: "+str(notes),1,(255,255,255))
            screen.blit(textBeat, (50,320,50,100))
            screen.blit(textHigh, (50,470,50,100))
            screen.blit(textNotes, (50,520,50,100))
        
        # Draw notes on track
        
        if noteStreak <= 74:
            for i1 in track1:
                i1[1] += speed
                if i1[4] == 0:
                    screen.blit(note1,pygame.Rect(i1[0],i1[1],i1[2],i1[3]))
                else:
                    screen.blit(ham1,pygame.Rect(i1[0],i1[1],i1[2],i1[3]))
            for i2 in track2:
                i2[1] += speed
                if i2[4] == 0:
                    screen.blit(note2,pygame.Rect(i2[0],i2[1],i2[2],i2[3]))
                else:
                    screen.blit(ham2,pygame.Rect(i2[0],i2[1],i2[2],i2[3]))
            for i3 in track3:
                i3[1] += speed
                if i3[4] == 0:
                    screen.blit(note3,pygame.Rect(i3[0],i3[1],i3[2],i3[3]))
                else:
                    screen.blit(ham3,pygame.Rect(i3[0],i3[1],i3[2],i3[3]))
            for i4 in track4:
                i4[1] += speed
                if i4[4] == 0:
                    screen.blit(note4,pygame.Rect(i4[0],i4[1],i4[2],i4[3]))
                else:
                    screen.blit(ham4,pygame.Rect(i4[0],i4[1],i4[2],i4[3]))
            for i5 in track5:
                i5[1] += speed
                if i5[4] == 0:
                    screen.blit(note5,pygame.Rect(i5[0],i5[1],i5[2],i5[3]))
                else:
                    screen.blit(ham5,pygame.Rect(i5[0],i5[1],i5[2],i5[3]))
        else:
            for track in tracks:
                for i in track:
                    i[1] += speed
                    if i[4] == 0:
                        screen.blit(note4,pygame.Rect(i[0],i[1],i[2],i[3]))
                    else:
                        screen.blit(ham4,pygame.Rect(i[0],i[1],i[2],i[3]))
        
        # Detect if note is supposed to be played, and remove if played correctly
        
        chord = 0
        
        if noteStreak == 0:
            lastHit = False
        else:
            lastHit = True
        
        for ind in track0:
            if ind[1] >= 700:
                track0.remove(ind)
                ind = None
        
        for track in tracks:
            for note in track:
                rect = pygame.Rect(note[0],note[1],note[2],note[3])
                if rect.colliderect(box_keys):
                    toBePlayed.append(note)
                    track.remove(note)
        if len(toBePlayed) > 0:
            note = toBePlayed[0]
            rect = pygame.Rect(note[0],note[1],note[2],note[3])
            if not(rect.colliderect(box_keys)):
                toBePlayed = []
                note = None
                noteStreak = 0
            else:
                chord = [note]
                for other in toBePlayed:
                    if other[0] != note[0] and other[1] == note[1]:
                        chord.append(other)
                if len(chord) == 1:
                    if dev:
                        toBePlayed.remove(note)
                        noteStreak += 1
                        newScore = 50
                    else:
                        if note[4] == 1 and (k1 or k2 or k3 or k4 or k5):
                            if note[0] == 400:
                                if k1:
                                    if lastHit:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    elif strum:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                            elif note[0] == 500:
                                if k2:
                                    if lastHit:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    elif strum:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                            elif note[0] == 600:
                                if k3:
                                    if lastHit:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    elif strum:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                            elif note[0] == 700:
                                if k4:
                                    if lastHit:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    elif strum:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                            elif note[0] == 800:
                                if k5:
                                    if lastHit:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    elif strum:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                        elif note[4] == 0:
                            if strum:
                                if note[0] == 400:
                                    if k1 and not(k2 or k3 or k4 or k5):
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                                elif note[0] == 500:
                                    if k2 and not(k3 or k4 or k5):
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                                elif note[0] == 600:
                                    if k3 and not(k4 or k5):
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                                elif note[0] == 700:
                                    if k4 and not(k5):
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                                elif note[0] == 800:
                                    if k5:
                                        toBePlayed.remove(note)
                                        noteStreak += 1
                                        newScore = 50
                                    else:
                                        noteStreak = 0
                                else:
                                    noteStreak = 0
                elif len(chord) == 2:
                    c1, c2 = chord[0], chord[1]  
                    if c1[0] > c2[0]:
                        c1, c2 = c2, c1
                    if dev:
                        toBePlayed.remove(c1)
                        toBePlayed.remove(c2)
                        noteStreak += 2
                        newScore = 100 
                    else:
                        if strum:
                            if c1[0] == 400:
                                if c2[0] == 500:
                                    if (k1 and k2) and not(k3 or k4 or k5):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100   
                                    else:
                                        noteStreak = 0
                                elif c2[0] == 600:
                                    if (k1 and k3) and not(k2 or k4 or k5):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                                elif c2[0] == 700:
                                    if (k1 and k4) and not(k2 or k3 or k5):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                                else:
                                    if (k1 and k5) and not(k2 or k3 or k4):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                            elif c1[0] == 500:
                                if c2[0] == 600:
                                    if (k2 and k3) and not(k1 or k4 or k5):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                                elif c2[0] == 700:
                                    if (k2 and k4) and not(k1 or k3 or k5):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                                else:
                                    if (k2 and k5) and not(k1 or k3 or k4):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                            elif c1[0] == 600:
                                if c2[0] == 700:
                                    if (k3 and k4) and not(k1 or k2 or k5):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                                else:
                                    if (k3 and k5) and not(k1 or k2 or k4):
                                        toBePlayed.remove(c1)
                                        toBePlayed.remove(c2)
                                        noteStreak += 2
                                        newScore = 100
                                    else:
                                        noteStreak = 0
                            elif c1[0] == 700:
                                if (k4 and k5) and not(k1 or k2 or k3):
                                    toBePlayed.remove(c1)
                                    toBePlayed.remove(c2)
                                    noteStreak += 2
                                    newScore = 100
                                else:
                                    noteStreak = 0
                            else:
                                noteStreak = 0
        else:
            if strum:
                noteStreak = 0
        
        if newScore > 0:
            if newScore == 50:
                notesHit += 1
                if note[0] == 400:
                    show_hit1 = 1
                if note[0] == 500:
                    show_hit2 = 1
                if note[0] == 600:
                    show_hit3 = 1
                if note[0] == 700:
                    show_hit4 = 1
                if note[0] == 800:
                    show_hit5 = 1
                score += 50
                if noteStreak > 9:
                    score += 50
                    if noteStreak > 19:
                        score += 50
                        if noteStreak > 29:
                            score += 50
                            if noteStreak > 74:
                                score += 200
            elif newScore == 100:
                notesHit += 2
                if c1[0] == 400:
                    show_hit1 = 1
                if c1[0] == 500:
                    show_hit2 = 1
                if c1[0] == 600:
                    show_hit3 = 1
                if c1[0] == 700:
                    show_hit4 = 1
                if c2[0] == 500:
                    show_hit2 = 1
                if c2[0] == 600:
                    show_hit3 = 1
                if c2[0] == 700:
                    show_hit4 = 1
                if c2[0] == 800:
                    show_hit5 = 1
                score += 100
                if noteStreak > 9:
                    score += 100
                    if noteStreak > 19:
                        score += 100
                        if noteStreak > 29:
                            score += 100
                            if noteStreak > 74:
                                score += 400
            newScore = 0

        if show_hit1 > 0:
            if show_hit1 < 6:
                screen.blit(hit1,(box_k1.left,box_k1.top-10))
                show_hit1 += 1
            else:
                show_hit1 = 0
        if show_hit2 > 0:
            if show_hit2 < 6:
                screen.blit(hit2,(box_k2.left,box_k2.top-10))
                show_hit2 += 1
            else:
                show_hit2 = 0
        if show_hit3 > 0:
            if show_hit3 < 6:
                screen.blit(hit3,(box_k3.left,box_k3.top-10))
                show_hit3 += 1
            else:
                show_hit3 = 0
        if show_hit4 > 0:
            if show_hit4 < 6:
                screen.blit(hit4,(box_k4.left,box_k4.top-10))
                show_hit4 += 1
            else:
                show_hit4 = 0
        if show_hit5 > 0:
            if show_hit5 < 6:
                screen.blit(hit5,(box_k5.left,box_k5.top-10))
                show_hit5 += 1
            else:
                show_hit5 = 0
        
        for i in toBePlayed:
            if i[1]+i[3] != 616:
                i[1] += speed
            if noteStreak <= 74:
                if i[0] == 400:
                    if i[4] == 0:
                        p = note1
                    else:
                        p = ham1
                elif i[0] == 500:
                    if i[4] == 0:
                        p = note2
                    else:
                        p = ham2
                elif i[0] == 600:
                    if i[4] == 0:
                        p = note3
                    else:
                        p = ham3
                elif i[0] == 700:
                    if i[4] == 0:
                        p = note4
                    else:
                        p = ham4
                else:
                    if i[4] == 0:
                        p = note5
                    else:
                        p = ham5
            else:
                if i[4] == 0:
                    p = note4
                else:
                    p = ham4
            screen.blit(p,pygame.Rect(i[0],i[1],i[2],i[3]))
        
        # Reset strumming

        strumUp, strumDown = False, False
        
        pygame.display.flip()
        
        clock.tick(bpm)

def songEnd(score,highest,name,notesHit,notes,song,diff,bpm,maxBeat,speed):

    if diff == 1:
        diff2 = "Intermediate"
    else:
        diff2 = "Expert"
    notePercent = 100*notesHit/notes
    img = pygame.image.load("Graphics/End Screen.jpg")
    fontTitle = pygame.font.Font("Graphics/28 Days Later.ttf", 30)
    fontOptions = pygame.font.Font("Graphics/setbackt.ttf", 30)
    fontText = pygame.font.Font("Graphics/poophead.ttf", 30)

    # Necessary Stuff
    
    screen = pygame.display.set_mode([1280,700])
    menu = (770,300,350,80)
    select = menu
    g = 0
    done = False
    
    while not(done):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    if select == menu:
                        main()
                    if select == retry:
                        play(song, diff, bpm, maxBeat, name, speed)
                    break
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if select == menu:
                        g = 0
                        select = retry
                    else:
                        g = 0
                        select = menu

        screen.blit(img,(0,0))

        songTitle = fontTitle.render(str(name),4,(255,255,255))
        songDiff = fontText.render(str(diff2),4,(255,255,255))
        backMenu = fontOptions.render("Back to Title Screen",4,(255,255,255))
        restart = fontOptions.render("Retry Song",4,(255,255,255))
        
        percent = fontText.render(str(notePercent)+" Percent Notes Hit",4,(0,75,0))
        streak = fontText.render("Highest Streak: "+str(highest),4,(0,75,0))

        title = (780,180,250,80)
        dif = (780,220,250,80)
        menu = (770,300,350,80)
        retry = (770,400,350,80)

        hit = (200,300,250,80)
        high = (200,400,250,80)
        
        pygame.draw.rect(screen,(0,g,0),select)

        screen.blit(songTitle,title)
        screen.blit(songDiff,dif)
        screen.blit(backMenu,menu)
        screen.blit(restart,retry)

        screen.blit(percent,hit)
        screen.blit(streak,high)

        if g < 152:
            g += 3
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit(0)

def main():
    diffSong = diffSelect()
    song = songSelect()
    numSong, bpm, maxBeat, nameSong, speedSong = song[0], song[1], song[2], song[3], song[4]
    play(numSong,diffSong,bpm,maxBeat,nameSong,speedSong)

# Main

start()
main()

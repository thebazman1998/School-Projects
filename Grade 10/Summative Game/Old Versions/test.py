
barTick = 0
beatTick = 0
go = True

s = open("Audio/song1.txt","r")

bar = []
for bars in s:
    bar.append(bars)

while go:
    
    beatTick += 1
    
    if barTick < 20:
        if beatTick == 8:
            beatTick = 0
            barTick += 1
    else:
        go = False
    
    currentBar = bar[barTick]
    currentBar = currentBar.split("|")
    currentBar = currentBar[1:len(currentBar):2]
    
    currentBeat = currentBar[beatTick]
    
    if "-" not in currentBeat:
        print str(barTick) + str(beatTick) + " " + currentBeat
import pygame, sys
pygame.init()

def instructions():
    
    backImg = pygame.image.load('Graphics/Background_Pause.jpg')
    backImg = pygame.transform.scale(backImg, (1280, 700))
    back = pygame.Rect(0, 0, 700, 1280)
    
    blankImg = pygame.image.load('Graphics/Instructions/Instructions_Template.png')
    blankImg = pygame.transform.scale(blankImg, (426,500))
    blank = pygame.Rect(427,87, 500,426)
    
    size = [1280, 700]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("INSTRUCTIONS")
    
    page = 1
    
    while page <= 8:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                page += 1
        
        screen.blit(backImg, back)
        screen.blit(blankImg, blank)
        
        if page == 9:
            break
        
        txtImg = pygame.image.load('Graphics/Instructions/page-'+str(page)+'.gif')
        txtImg = pygame.transform.scale(txtImg, (426,500))
        
        screen.blit(txtImg,blank)
        
        pygame.display.flip()
        
instructions()
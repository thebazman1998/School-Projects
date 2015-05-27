'''
Created on May 10, 2014

@author: basil
'''
def win(winner):
    z = 0
    if winner == 1:
        while z < 29:
            img = 'Graphics/Player 1 Wins/Player 1 Wins'+str(z)
            img = pygame.transform.scale(img, (1280, 700))
            screen.blit(img, pygame.Rect(0, 0, 1, 1))
            z += 1
    if winner == 2:
        while z < 29:
            img = 'Graphics/Player 2 Wins/Player 2 Wins'+str(z)
            img = pygame.transform.scale(img, (1280, 700))
            screen.blit(img, pygame.Rect(0, 0, 1, 1))
            z += 1
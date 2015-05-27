import pygame
import random

# Initialize pygame
pygame.init()

# Define colors in RGB
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Define pi
pi = 3.141592653

# Set screen size
size = [900, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bp_U2_Assignment1b")

# Loop until the user clicks close
done = False
clock = pygame.time.Clock()

for a in range(0, 10):
    red = random.randint(32, 255)
    green = random.randint(32, 255)
    blue = random.randint(32, 255)
    
    color = (red, green, blue)
    pygame.draw.circle(screen, color, [random.randint(0, 900), random.randint(0, 600)], 40)

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Redifines done as True to exit loop
            

        
        
        
    pygame.display.flip()





pygame.quit()
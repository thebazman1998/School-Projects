import pygame
import random

# Draws num amount of congruent circles (radius = 40) in random positions filled with random colors
def draw_circles(num):
    for i in range(0, num):
        red = random.randint(32, 255)
        green = random.randint(32, 255)
        blue = random.randint(32, 255)
        
        color = (red, green, blue)
        
        pygame.draw.circle(screen, color, [random.randint(0, 900), random.randint(0, 600)], 40)    

def cover_with_circles():
    y = 0
    x = 0
    
    for i in range(0, 5):
        for a in range(0, 3):
            red = random.randint(32, 255)
            green = random.randint(32, 255)
            blue = random.randint(32, 255)
            
            color = (red, green, blue)
            
            pygame.draw.circle(screen, color [x, 0], 40)
            
            x += 80
        
        x = 0
        y += 80

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

pygame.display.set_caption("Bp_U2_Assignment2")

# Loop until the user clicks close
done = False
clock = pygame.time.Clock()

cover_with_circles()

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Redifines done as True to exit loop
    pygame.display.flip()
pygame.quit()
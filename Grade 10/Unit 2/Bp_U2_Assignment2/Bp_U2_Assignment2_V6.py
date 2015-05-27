"""
Name: Basil
Class: ICS201-01
Date: 26/03/14
Unit 2 Assignment 2
"""

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

def cover_with(shape):
    if shape == "circle":
        y = 40
        x = 40
        
        for i in range(0, 10):
            for a in range(0, 20):
                red = random.randint(32, 255)
                green = random.randint(32, 255)
                blue = random.randint(32, 255)
                
                color = (red, green, blue)
                
                pygame.draw.circle(screen, color, [x, y], 40)
                
                x += 80
                
            x = 40
            y += 80
                
    elif shape == "triangle":
        p1x = 40
        p1y = 0
        p2x = 0
        p2y = 80
        p3x = 80
        p3y = 80
        
        for i in range(0, 10):
            for a in range(0, 20):
                red = random.randint(32, 255)
                green = random.randint(32, 255)
                blue = random.randint(32, 255)
                
                color = (red, green, blue)
                
                pygame.draw.polygon(screen, color, ([p1x, p1y], [p2x, p2y], [p3x, p3y]))
                
                p1x += 80
                p2x += 80
                p3x += 80
            
            p1x = 40
            p2x = 0
            p3x = 80
            p1y += 80
            p2y += 80
            p3y += 80
            
            for a in range(0, 20):
                red = random.randint(32, 255)
                green = random.randint(32, 255)
                blue = random.randint(32, 255)
                
                color = (red, green, blue)
                
                pygame.draw.polygon(screen, color, ([p1x, p1y], [p2x, p2y], [p3x, p3y]))

def draw_arrow():
    pygame.draw.line(screen, (156, 102, 31), [40, 300], [700, 300], 15)
    
    pygame.draw.line(screen, (200, 200, 200), [650, 300], [750, 350], 20)
    pygame.draw.line(screen, (200, 200, 200), [600, 300], [700, 350], 20)
    pygame.draw.line(screen, (200, 200, 200), [550, 300], [650, 350], 20)
    pygame.draw.line(screen, (200, 200, 200), [650, 300], [750, 250], 20)
    pygame.draw.line(screen, (200, 200, 200), [600, 300], [700, 250], 20)
    pygame.draw.line(screen, (200, 200, 200), [550, 300], [650, 250], 20)
    
    pygame.draw.polygon(screen, (139, 134, 130), ([15, 300], [75, 325], [75, 275]))

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

# Draw functions go under this comment

# Draw functions go above this comment
# Loop until the user clicks close
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Redifines done as True to exit loop
    pygame.display.flip()
pygame.quit()
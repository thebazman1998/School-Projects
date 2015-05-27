"""
Name: Basil
Class: ICS201
Date: 04/0214
Assignment 5
"""

import pygame
import random

pygame.init()

def draw_background():
    screen.fill((77, 255, 255))
    pygame.draw.rect(screen, (0, 153, 0), ((0, 400), (900, 600)))
    for a in range(0, random.randint(0, 2)):
        draw_cloud(random.randint(0, 900), random.randint(0, 100))

def randcolors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_house(x, y):
    # Find coordinates for house based on x and y
    
    # House body
    house_box_tl = (x, y + 50)
    house_box_br = (200, 175)
    house_roof_t = (x + 100, y)
    house_roof_l = (x, y + 50)
    house_roof_r = (x + 200, y + 50)
    
    # Door
    door_tl = (x + 30, y + 130)
    door_br = (45, 95)
    knob = (x + 70, y + 172)
    
    # Window
    window_outer_tl = (x + 115, y + 130)
    window_outer_br = (50, 50)
    window_inner_tl = (x + 120, y + 135)
    window_inner_br = (40, 40)
    window_cross_xx = (x + 115, y + 155)
    window_cross_xy = (x + 163, y + 155)
    window_cross_yx = (x + 140, y + 135)
    window_cross_yy = (x + 140, y + 177)
    
    # Draw house
    color = randcolors()
    pygame.draw.rect(screen, color, (house_box_tl, house_box_br))
    color = randcolors()
    pygame.draw.polygon(screen, color, (house_roof_l, house_roof_t, house_roof_r))
    color = randcolors()
    pygame.draw.rect(screen, color, (door_tl, door_br))
    pygame.draw.rect(screen, (0, 0, 0), (window_outer_tl, window_outer_br))
    pygame.draw.rect(screen, (255, 255, 255), (window_inner_tl, window_inner_br))
    pygame.draw.line(screen, (0, 0, 0), window_cross_xx, window_cross_xy, 5)
    pygame.draw.line(screen, (0, 0, 0), window_cross_yx, window_cross_yy, 5)
    pygame.draw.circle(screen, (0, 0, 0), knob, 5)

def draw_tree(x, y, r):
    tree_leaves_color = (random.randint(20, 150), 255, 0)
    tree_leaves_x = x + r
    tree_leaves_y = y + r
    tree_leaves_r = r
    
    tree_trunk_tl = (x + r - 20, y + r)
    tree_trunk_br = (40, 200)
    
    pygame.draw.rect(screen, (128, 96, 3), (tree_trunk_tl, tree_trunk_br))
    pygame.draw.circle(screen, tree_leaves_color, (tree_leaves_x, tree_leaves_y), tree_leaves_r)

def draw_cloud(x, y):
    for i in range(0, 10):
        cloud_pos_x = random.randint(x, x + 100)
        cloud_pos_y = random.randint(y, y + 100)
        cloud_r = random.randint(20, 50)
        pygame.draw.circle(screen, (255, 255, 255), (cloud_pos_x, cloud_pos_y), cloud_r)
    
def draw_onscreen():
    draw_background()
    draw_house(random.randint(0, 50), 175)
    draw_house(random.randint(275, 325), 175)
    draw_house(random.randint(550, 600), 175)
    draw_tree(random.randint(150, 200), 150, random.randint(50, 100))
    draw_tree(random.randint(425, 450), 150, random.randint(50, 100))
    draw_tree(random.randint(750, 850), 150, random.randint(50, 100))

# Set screen size
size = [900, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bp_U2_Assignment5")




done = False
clock = pygame.time.Clock()

# Call draw methods under this comment
draw_onscreen()
# Call draw methods above this comment

while not done:
    pygame.display.flip()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Redefines done as True to exit loop
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                draw_onscreen()
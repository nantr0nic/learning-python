# Going to make this an iteration of "first-game" 
# Circle color palette maker thing
# Mousewheel should be RANDOM colors, perhaps L/R click should make brighter/dimmer?
# Spacebar will "leave" or "print" the circle in place and output RGB code

import pygame
import random
pygame.init ()

# Window
winx = 1280 # window X widgth
winy = 720 # window Y height
#win is a surface!
win = pygame.display.set_mode((winx,winy)) # makes the window
pygame.display.set_caption("Circle palette maker") # captions the window

# Game clock 
clock = pygame.time.Clock()
dt = 0

# Circle position and size/radius
object_pos = pygame.math.Vector2(win.get_width() / 2, win.get_height() / 2)
c_x = object_pos.x # circle x position 
c_y = object_pos.y # circle y position
c_radius = 20
c_vel = 175 

# Circle color variables
c_R = 25
c_G = 45
c_B = 75

# Function to randomly change circle color
def change_circle_color():
    global c_R, c_G, c_B
    c_R = max(5, min(c_R + random.randint(-25, 25), 255))
    c_G = max(5, min(c_G + random.randint(-25, 25), 255))
    c_B = max(5, min(c_B + random.randint(-25, 25), 255))
    return print("Circle color changed")

### Main game loop ###
run = True
while run:
    # Limits FPS to 60 - dt is delta time in seconds since last frame, used for
    # framerate-independent physics.
    dt = clock.tick(75) / 1000
   # pygame.time.delay(75) # delays 

    # Event-check loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEWHEEL:
            change_circle_color()
            print("Mouse")

    keys = pygame.key.get_pressed()

# Buttons being pushed and moving the circle + boundaries
    if keys[pygame.K_LEFT] and c_x > c_radius :
        c_x -= (c_vel * dt)
        change_circle_color()
    if keys[pygame.K_RIGHT] and c_x < winx - c_radius:
        c_x += (c_vel * dt)
        change_circle_color()
    if keys[pygame.K_UP] and c_y > c_radius :
        c_y -= (c_vel * dt)
    if keys[pygame.K_DOWN] and c_y < winy - c_radius:
        c_y += (c_vel * dt)

# Quit keys
    if keys[pygame.K_LCTRL] and keys[pygame.K_q]: 
        run = False

# vvvv Most of the drawing stuff vvvv

    win.fill((0, 0, 0)) # Background black

    pygame.draw.circle(win, (c_R, c_G, c_B), (c_x, c_y), c_radius) # drawing the main circle 


    pygame.display.flip() # updates the screen

pygame.quit
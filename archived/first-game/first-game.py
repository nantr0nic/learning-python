import pygame
import random

pygame.init()

# Window
winx = 1280  # window X widgth
winy = 720  # window Y height
# win is a surface!
win = pygame.display.set_mode((winx, winy))  # makes the window
pygame.display.set_caption("Pygame Works!")  # captions the window

# Game clock
clock = pygame.time.Clock()
dt = 0

# Circle position and size/radius
object_pos = pygame.math.Vector2(win.get_width() / 2, win.get_height() / 2)
c_x = object_pos.x  # circle x position
c_y = object_pos.y  # circle y position
c_radius = 15

# Circle velocity dictionaries
speedDic = {
    "slow": 10,
    "medium": 25,
    "fast": 62,
}
c_vel = speedDic["slow"]
speed = "slow"

# Circle color variables
c_R = 25
c_G = 45
c_B = 75


# Function to change circle color
def change_circle_color():
    global c_R, c_G, c_B
    c_R = max(5, min(c_R + random.randint(-25, 25), 255))
    c_G = max(5, min(c_G + random.randint(-25, 25), 255))
    c_B = max(5, min(c_B + random.randint(-25, 25), 255))
    return print("Circle color changed")


### Main game loop ###
run = True
while run:
    pygame.time.delay(0)  # delays

    # Event-check loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEWHEEL:
            change_circle_color()
            print("Mouse")

    keys = pygame.key.get_pressed()

    # Buttons being pushed and moving the circle + boundaries
    # Because the circle's velocity can change this is no longer
    #   an effective way to make boundaries
    if keys[pygame.K_LEFT] and c_x > c_vel:
        c_x -= c_vel
        change_circle_color()
        print(str(c_x) + " / " + str(c_y))
    if keys[pygame.K_RIGHT] and c_x < winx - c_vel:
        c_x += c_vel
        change_circle_color()
        print(str(c_x) + " / " + str(c_y))
    if keys[pygame.K_UP] and c_y > c_vel:
        c_y -= c_vel
        print(str(c_x) + " / " + str(c_y))
    if keys[pygame.K_DOWN] and c_y < winy - c_vel:
        c_y += c_vel
        print(str(c_x) + " / " + str(c_y))

    # Change speed when hit spacebar
    #   it sometimes doesn't change when hit spacebar...
    #   goes too fast need to slow it down
    if keys[pygame.K_SPACE]:
        if speed == "slow":
            speed = "medium"
            c_vel = speedDic["medium"]
            print("Going from slow to medium!")
        elif speed == "medium":
            speed = "fast"
            c_vel = speedDic["fast"]
            print("Going from medium to fast!")
        elif speed == "fast":
            speed = "slow"
            c_vel = speedDic["slow"]
            print("Going from fast to slow!")

    # Quit keys
    if keys[pygame.K_LCTRL] and keys[pygame.K_q]:
        run = False

    win.fill((0, 0, 0))  # background filled with 0

    pygame.draw.circle(
        win, (c_R, c_G, c_B), (c_x, c_y), c_radius
    )  # drawing the main circle

    pygame.display.flip()  # updates the screen

    # Limits FPS to 60 - dt is delta time in seconds since last frame, used for
    # framerate-independent physics.
    dt = clock.tick(75) / 1000


pygame.quit

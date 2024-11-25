import pygame
from pygame.sprite import Group

from circle import Circle
import cirpal_functions as cf

# Display/game clock settings
clock = pygame.time.Clock()
dt = 0


def run_cirpal():
    pygame.init()

    # Set window dimensions and create window screen + caption
    winx = 1280  # window X widgth
    winy = 720  # window Y height
    win = pygame.display.set_mode((winx, winy))  # makes the window
    pygame.display.set_caption("Circle palette maker")  # captions the window

    circle_group = Group()
    circle = Circle(win)

    while True:
        cf.check_events(circle, win, circle_group)

        win.fill((0, 0, 0))
        for circles in circle_group.sprites():
            circles.draw_circle(win)
        circle.draw_circle(win)

        pygame.display.flip()
        clock.tick(75)


run_cirpal()

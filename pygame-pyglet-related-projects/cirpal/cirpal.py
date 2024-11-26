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
        # Draw all circles first
        for circles in circle_group.sprites():
            circles.draw_circle(win)
        circle.draw_circle(win)

        # Check for hover and draw RGB values
        mouse_pos = pygame.mouse.get_pos()
        for circles in circle_group.sprites():
            if circles.contains_point(mouse_pos):
                circles.draw_rgb(win)
        if circle.contains_point(mouse_pos):
            circle.draw_rgb(win)

        pygame.display.flip()
        clock.tick(75)


run_cirpal()

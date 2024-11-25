import pygame
from circle import Circle


def check_events(circle, win, circle_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Key down events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circle.moving_x = -1
            elif event.key == pygame.K_RIGHT:
                circle.moving_x = 1
            elif event.key == pygame.K_UP:
                circle.moving_y = -1
            elif event.key == pygame.K_DOWN:
                circle.moving_y = 1
            elif event.key == pygame.K_SPACE:
                # Capture the current state and create a new fixed circle
                new_state = circle.capture_state()
                new_circle = Circle.create_from_state(win, new_state)
                circle_group.add(new_circle)
                # Remove the current moving circle from the group
                circle_group.remove(circle)

        # Key up events
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                circle.moving_x = 0
            elif event.key == pygame.K_RIGHT:
                circle.moving_x = 0
            elif event.key == pygame.K_UP:
                circle.moving_y = 0
            elif event.key == pygame.K_DOWN:
                circle.moving_y = 0

        elif event.type == pygame.MOUSEWHEEL:
            circle.change_color()

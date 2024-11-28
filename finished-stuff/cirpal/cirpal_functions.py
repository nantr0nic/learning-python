import pygame
from circle import Circle

# Add global vairiables for tracking dragged circle
selected_circle = None
dragging = False


def check_events(circle, win, circle_group):
    global selected_circle, dragging

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Mouse events for dragging circles
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                # Check all stamped circles for collision
                for stamped_circle in circle_group.sprites():
                    if stamped_circle.contains_point(mouse_pos):
                        selected_circle = stamped_circle
                        dragging = True
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left click release
                selected_circle = None
                dragging = False
                
        elif event.type == pygame.MOUSEMOTION:
            if dragging and selected_circle:
                selected_circle.move_to(pygame.mouse.get_pos())

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

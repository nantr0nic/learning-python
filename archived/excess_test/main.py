import pygame
from pygame.sprite import Group

import functions as func
from player import Player


def run_cc():
    clock = pygame.time.Clock()
    pygame.init()

    # Make window
    winx = 1280
    winy = 720
    win = pygame.display.set_mode((winx, winy))  # makes the window
    pygame.display.set_caption("Circle Cirvivors")  # captions the window

    player = Player(win)
    projectiles = Group()

    # Setup EVENT on timer for shooting projectiles. (Check events in functions file)
    SHOOT_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SHOOT_EVENT, 1)  

    # Main game loop
    while True:
        # Check for events
        func.check_events(player, projectiles, SHOOT_EVENT)

        # Draw black background
        win.fill((0, 0, 0))

        # Draw / update functions/methods.
        player.update(win)
        func.update_state(win, projectiles)

        # Refresh stuff
        pygame.display.flip()
        # 75 FPS
        clock.tick(150)  
        print(f"Bullets #: {len(projectiles)}")


run_cc()

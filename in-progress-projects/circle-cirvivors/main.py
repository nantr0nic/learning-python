import pygame
from pygame.sprite import Group

import functions as func
from player import Player


def run_cc():
    clock = pygame.time.Clock()
    # dt = 0
    pygame.init()

    # Make window
    winx = 1280
    winy = 720
    win = pygame.display.set_mode((winx, winy))  # makes the window
    pygame.display.set_caption("Circle Cirvivors")  # captions the window

    player = Player(win)
    projectiles = Group()
    enemies = Group()

    # Setup EVENT on timer for shooting projectiles. (Check events in functions file)
    SHOOT_EVENT = pygame.USEREVENT + 1
    SPAWN_EVENT = pygame.USEREVENT + 2
    initial_spawn_interval = 1000  # milliseconds
    spawn_interval_decrement = 50  # milliseconds
    decrement_interval = 2000  # 5 seconds in milliseconds
    current_spawn_interval = initial_spawn_interval
    last_decrement_time = 0
    pygame.time.set_timer(SHOOT_EVENT, 250)
    pygame.time.set_timer(SPAWN_EVENT, current_spawn_interval)

    speed = 5

    # Main game loop
    while True:
        current_time = pygame.time.get_ticks()
        # Check for events
        func.check_events(
            player, projectiles, enemies, speed, SHOOT_EVENT, SPAWN_EVENT
        )

        # Draw black background
        win.fill((0, 0, 0))

        # Draw / update functions/methods.
        player.update(win)
        func.update_state(win, projectiles, enemies, player)

        # Refresh stuff
        pygame.display.flip()

        # 75 FPS
        clock.tick(75)
        if current_time - last_decrement_time >= decrement_interval:
            current_spawn_interval = max(current_spawn_interval - spawn_interval_decrement, 100)
            pygame.time.set_timer(SPAWN_EVENT, current_spawn_interval)
            last_decrement_time = current_time
            print(f"Current spawn: {current_spawn_interval}")
        # debug: print(f"Bullets #: {len(projectiles)}")


run_cc()

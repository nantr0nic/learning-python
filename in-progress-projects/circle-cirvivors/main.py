import pygame
from pygame.sprite import Group

import functions as func
import settings as s
from player import Player
from enemies import spawn_timer


def run_cc():
    clock = pygame.time.Clock()
    # dt = 0
    pygame.init()

    # Make window
    win = pygame.display.set_mode(
        (s.window_width, s.window_height)
    )  # makes the window
    pygame.display.set_caption("Circle Cirvivors")  # captions the window

    player = Player(win)
    projectiles = Group()
    enemies = Group()

    # EVENTS for projectiles shooting and enemy spawning. (Check events in functions file)
    SHOOT_EVENT = pygame.USEREVENT + 1
    SPAWN_EVENT = pygame.USEREVENT + 2
    ROUND_TIMER = pygame.USEREVENT + 3
    pygame.time.set_timer(SHOOT_EVENT, 250)
    pygame.time.set_timer(SPAWN_EVENT, s.current_spawn_interval)
    pygame.time.set_timer(ROUND_TIMER, 1000)

    # Main game loop
    while True:
        current_time = pygame.time.get_ticks()
        # Check for events
        func.check_events(
            win,
            player,
            projectiles,
            enemies,
            SHOOT_EVENT,
            SPAWN_EVENT,
            ROUND_TIMER,
        )

        # Draw black background
        win.fill((0, 0, 0))

        # Draw / update functions/methods.
        player.update(win)
        func.update_state(win, projectiles, enemies, player)

        # Draw / begin round countdown
        func.round_countdown(win)

        func.draw_healthbar(win)

        # Refresh stuff
        pygame.display.flip()

        # 80 FPS
        clock.tick(80)

        # Spawn frequency timer
        spawn_timer(current_time, SPAWN_EVENT)

        # debug: print(f"Bullets #: {len(projectiles)}")


run_cc()

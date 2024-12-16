import pygame
import random
import time
# from pygame.sprite import Group

import functions as func
from player import Player
from bullets import Bullets

clock = pygame.time.Clock()
dt = 0

def run_cc():
    pygame.init()
    
    # Make window
    winx = 1280
    winy = 720
    win = pygame.display.set_mode((winx, winy))  # makes the window
    pygame.display.set_caption("Circle Cirvivors")  # captions the window

    player = Player(win)
    bullets = Bullets(win, player)
    
    # Main game loop
    while True:
        # Check for events
        func.check_events(player, bullets, win)
        
        # Draw black background
        win.fill((0, 0, 0))        
        
        player.draw_player(win)
            
        bullets.update(win)

        
        
        # Refresh stuff
        pygame.display.flip()
        clock.tick(75)
        

run_cc()
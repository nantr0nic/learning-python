import pygame
import random
import math
from projectiles import Projectile

def check_events(player, projectiles, SHOOT_EVENT):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moving_x = -1
            elif event.key == pygame.K_RIGHT:
                player.moving_x = 1              
            elif event.key == pygame.K_UP:
                player.moving_y = -1
            elif event.key == pygame.K_DOWN:
                player.moving_y = 1
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_x = 0
            elif event.key == pygame.K_RIGHT:
                player.moving_x = 0
            elif event.key == pygame.K_UP:
                player.moving_y = 0
            elif event.key == pygame.K_DOWN:
                player.moving_y = 0    
                
        elif event.type == SHOOT_EVENT:
                shoot_projectiles(player, projectiles)
                
def shoot_projectiles(player, projectiles):
    # Shooting is continuous. Keeping function classless.
    for i in range(2):
        angle = random.normalvariate(0, 2 * math.pi) # random angle in radians
        speed = random.uniform(1, 5) # random speed
        
    projectiles.add(Projectile(player.x, player.y, angle, speed))
    return projectiles

def update_state(surface, projectiles):
    # update state of projectiles
    projectiles.update()
    projectiles.draw(surface)
    
        
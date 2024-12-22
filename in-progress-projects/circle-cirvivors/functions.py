import pygame
import random
import math
from projectiles import Projectile
from enemies import Enemy


def check_events(player, projectiles, enemies, speed, SHOOT_EVENT, SPAWN_EVENT):
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
            elif event.key == pygame.K_q:
                pygame.quit()

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
        elif event.type == SPAWN_EVENT:
            draw_enemies(
                player, enemies, random.uniform(0.2, 1.5), random.uniform(5, 25)
            )


def shoot_projectiles(player, projectiles):
    # Shooting is continuous. Keeping function classless.
    for i in range(2):
        angle = random.uniform(0, 2 * math.pi)  # random angle in radians
        speed = 2

    projectiles.add(Projectile(player.x, player.y, angle, speed))
    return projectiles


def draw_enemies(player, enemies, speed, size):
    enemies.add(
        Enemy(random.randint(0, 1280), random.randint(-25, -1), speed, size)
    )
    enemies.add(
        Enemy(random.randint(0, 1280), random.randint(725, 750), speed, size)
    )
    enemies.add(
        Enemy(random.randint(-25, -1), random.randint(0, 720), speed, size)
    )
    enemies.add(
        Enemy(random.randint(1295, 1305), random.randint(0, 720), speed, size)
    )
    return enemies


def update_state(surface, projectiles, enemies, player):
    # update state of projectiles
    projectiles.update()
    projectiles.draw(surface)
    # update state of enemies
    enemies.update(player)
    enemies.draw(surface)
    # remove projectiles passing the edge of the window
    for projectile in projectiles.copy():
        if (
            projectile.rect.right < 0
            or projectile.rect.left > surface.get_width()
            or projectile.rect.bottom < 0
            or projectile.rect.top > surface.get_height()
        ):
            projectiles.remove(projectile)

    pygame.sprite.groupcollide(projectiles, enemies, False, True)
    
    

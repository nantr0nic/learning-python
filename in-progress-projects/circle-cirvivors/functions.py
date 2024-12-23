import pygame
import random
import math

from projectiles import Projectile
from enemies import Enemy
import settings as s


def check_events(
    surface, player, projectiles, enemies, SHOOT_EVENT, SPAWN_EVENT, ROUND_TIMER
):
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
            spawn_enemies(
                surface,
                enemies,
                s.enemy_speed,
                s.enemy_size,
            )
        elif event.type == ROUND_TIMER:
            if s.round_time > 0:
                round_countdown(surface)
                s.round_time -= 1
            elif s.round_time <= 0:
                round_countdown(surface)
            if s.round_time == 15:
                s.timer_color = [255, 155, 0]  # orange
            elif s.round_time == 5:
                s.timer_color = [255, 0, 0]  # red


def shoot_projectiles(player, projectiles):
    # Shooting is continuous in a circular direction.
    for i in range(2):
        angle = random.uniform(0, 2 * math.pi)  # random angle in radians

    projectiles.add(
        Projectile(
            player.x, player.y, angle, s.projectile_speed, s.projectile_size
        )
    )
    return projectiles


def spawn_enemies(surface, enemies, speed, size):
    # REFACTOR using surface edges rather than hard set numbers
    spawn_above = (
        random.randint(0, surface.get_width()),
        random.randint(-25, 0),
    )
    spawn_below = (
        random.randint(0, surface.get_width()),
        surface.get_height() + random.randint(0, 25),
    )
    spawn_left = (
        random.randint(-25, 0),
        random.randint(0, surface.get_height()),
    )
    spawn_right = (
        surface.get_width() + random.randint(0, 25),
        random.randint(0, surface.get_height()),
    )
    spawn_location_list = [spawn_above, spawn_below, spawn_left, spawn_right]
    spawn_location = random.choice(spawn_location_list)
    enemies.add(Enemy(spawn_location[0], spawn_location[1], speed, size))
    return enemies


def update_state(surface, projectiles, enemies, player):
    # update state of projectiles
    projectiles.update()
    projectiles.draw(surface)
    # update state of enemies
    enemies.update(player)
    enemies.draw(surface)
    # remove projectiles from Group that pass the edge of the window
    for projectile in projectiles.copy():
        if (
            projectile.rect.right < 0
            or projectile.rect.left > surface.get_width()
            or projectile.rect.bottom < 0
            or projectile.rect.top > surface.get_height()
        ):
            projectiles.remove(projectile)
    # Detect projectile vs enemy collision + remove enemy
    pygame.sprite.groupcollide(projectiles, enemies, False, True)
    # Detect square vs player collisions
    if pygame.sprite.spritecollideany(player, enemies):
        s.player_health -= 1
        s.healthbar_width = (s.player_health / 100) * surface.get_width()
        print(f"Player health: {s.player_health}")


def round_countdown(surface):
    font = pygame.font.SysFont(None, 45)
    text = font.render(
        f"{s.round_time}",
        True,
        (s.timer_color[0], s.timer_color[1], s.timer_color[2]),
    )
    text_rect = text.get_rect()
    text_rect.centerx = surface.get_width() / 2
    text_rect.top = 5
    surface.blit(text, text_rect)


def draw_healthbar(surface):
    healthbar_width = s.healthbar_width
    healthbar_rect = pygame.Rect(
        0, (surface.get_height() - 20), healthbar_width, 10
    )
    pygame.draw.rect(
        surface,
        (s.health_color[0], s.health_color[1], s.health_color[2]),
        healthbar_rect,
    )
    if s.player_health <= 55:
        s.health_color = [255, 155, 0]
    if s.player_health <= 30:
        s.health_color = [255, 0, 0]

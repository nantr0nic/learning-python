# Class for enemies.

import pygame
from pygame.sprite import Sprite
import random


class Enemy(Sprite):
    def __init__(self, x, y, speed, size):
        """Basic attributes."""
        super(Enemy, self).__init__()
        self.speed = speed
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.rect_draw = pygame.Rect(0, 0, self.size, self.size)
        pygame.draw.rect(self.image, (255, 255, 255), self.rect_draw)
        self.rect = self.image.get_rect(center=(x, y))
        self.x = self.rect.centerx
        self.y = self.rect.centery

    def update(self, player):
        # use floats for x,y
        self.current_pos = pygame.math.Vector2(self.x, self.y)
        self.player_pos = pygame.math.Vector2(player.x, player.y)
        self.current_pos.move_towards_ip(self.player_pos, self.speed)
        self.x = self.current_pos.x
        self.y = self.current_pos.y
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

import pygame
import math
import random
from pygame.sprite import Sprite


class Projectile(Sprite):
    """Class for projectiles. Will be instantiated for various projectiles the player emits."""

    def __init__(self, x, y, angle, speed):
        """Initialize -- x and y origin at player position."""
        super(Projectile, self).__init__()
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.radius = 5

    def update_movement(self):
        """Update movement of each individual projectile (in group)."""
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, surface):
        """Draw projectile. So far just circles."""
        pygame.draw.circle(
            surface, (255, 0, 0), (int(self.x), int(self.y)), self.radius
        )

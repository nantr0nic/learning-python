import pygame
import math
import random
from pygame.sprite import Sprite


class Projectile(Sprite):
    """Class for projectiles. Will be instantiated for various projectiles the player emits."""

    def __init__(self, x, y, angle, speed):
        """Initialize -- x and y origin at player position."""
        super(Projectile, self).__init__()
        self.angle = angle
        self.speed = speed
        self.radius = 5
        self.r = random.randint(100,255)
        self.g = random.randint(25,100)
        self.b = random.randint(0,255)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (self.r, self.g, self.b), (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        

    def update(self):
        """Update movement of each individual projectile (in group)."""
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def draw(self, surface):
        """Draw projectile. So far just circles."""
        surface.blit(self.image, self.rect)
        

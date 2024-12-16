import pygame
import math
from pygame.sprite import Sprite
import random
import time

class Bullets(Sprite):
    def __init__(self, surface, player):
        super(Bullets, self).__init__()
        self.surface = surface
        self.pos = pygame.math.Vector2(player.x, player.y)
        self.angle = math.atan2(surface.get_height() / 2 - player.y, player.x - surface.get_width() / 2)
        self.last_draw_time = pygame.time.get_ticks()
        
        """
    def direction(self, degrees):
        rads = math.radians(degrees)
        self.x = math.cos(rads)
        self.y = math.sin(rads)
        return self.x, self.y
        """
    
    def draw(self, surface):
        # angle = math.atan2(surface.get_height() / 2 - self.pos.y, self.pos.x - surface.get_width() / 2)
        dx = self.pos.x + math.cos(self.angle) * random.randint(25,200)
        dy = self.pos.y + math.sin(self.angle) * random.randint(25,200)
        pygame.draw.circle(surface, (255, 255, 255), (int(dx), int(dy)), 5)
        
    def update(self, surface):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_draw_time >= 500:
            self.draw(surface)
            self.last_draw_time = current_time
        self.vel_x = 5 * random.uniform(-10, 10)
        self.vel_y = 5 * random.uniform(-10, 10)
        self.pos.x += self.vel_x
        self.pos.y += self.vel_y
        
        
        
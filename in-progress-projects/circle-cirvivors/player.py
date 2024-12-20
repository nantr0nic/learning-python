import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, surface):
        """Define player attributes."""
        super(Player, self).__init__()
        self.surface = surface
        # player_pos default is center of screen.
        player_pos = pygame.math.Vector2(
            surface.get_width() / 2, surface.get_height() / 2
        )
        self.x = player_pos.x
        self.y = player_pos.y
        # Player is a circle by default. Radius = size.
        self.radius = 20
        self.r = 140
        self.g = 210
        self.b = 205
        # Movement flags
        # For x-axis -1 is left and 1 is right
        self.moving_x = 0
        # For y-axis -1 is up and 1 is down
        self.moving_y = 0

    def draw_player(self, surface):
        """Draw the player."""
        pygame.draw.circle(
            surface, (self.r, self.g, self.b), (self.x, self.y), self.radius
        )
        # Movement
        if self.moving_x == -1:
            self.x -= 5
        elif self.moving_x == 1:
            self.x += 5
        if self.moving_y == -1:
            self.y -= 5
        elif self.moving_y == 1:
            self.y += 5

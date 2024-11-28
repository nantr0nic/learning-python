import pygame
import pygame.font
from pygame.sprite import Sprite
import random


class Circle(Sprite):
    def __init__(self, win):
        """Define circle attributes like position, radius, color."""
        super(Circle, self).__init__()
        self.surface = win
        object_pos = pygame.math.Vector2(win.get_width() / 2, win.get_height() / 2)
        self.x = object_pos.x
        self.y = object_pos.y
        self.radius = 20
        # (Random) starting colors
        self.r = random.randint(5, 150)
        self.g = random.randint(5, 255)
        self.b = random.randint(5, 255)
        # Movement flags
        # For x-axis -1 is left and 1 is right
        self.moving_x = 0
        # For y-axis -1 is up and 1 is down
        self.moving_y = 0

    def change_color(self):
        """Change the color of the circle."""
        self.r = max(5, min(self.r + random.randint(-25, 25), 255))
        self.g = max(5, min(self.g + random.randint(-25, 25), 255))
        self.b = max(5, min(self.b + random.randint(-25, 25), 255))

    def draw_circle(self, win):
        """Draw the circle."""
        pygame.draw.circle(win, (self.r, self.g, self.b), (self.x, self.y), self.radius)
        # Movement
        if self.moving_x == -1:
            self.x -= 5
        elif self.moving_x == 1:
            self.x += 5
        if self.moving_y == -1:
            self.y -= 5
        elif self.moving_y == 1:
            self.y += 5

    def stamp_circle(self, win):
        """Stamp the circle as it is."""
        pygame.draw.circle(win, (self.r, self.g, self.b), (self.x, self.y), self.radius)
        print("stamp")

    def capture_state(self):
        """Capture and return the current state of the circle."""
        return {"x": self.x, "y": self.y, "r": self.r, "g": self.g, "b": self.b}

    def contains_point(self, point):
        """Check if a point (x,y) is inside the circle."""
        dx = point[0] - self.x
        dy = point[1] - self.y
        return (dx * dx + dy * dy) <= (self.radius * self.radius)

    def move_to(self, pos):
        """Move circle to a specific position."""
        self.x = pos[0]
        self.y = pos[1]

    @staticmethod
    def create_from_state(win, state):
        """Create a new Circle instance from the given state."""
        circle = Circle(win)
        circle.x = state["x"]
        circle.y = state["y"]
        circle.r = state["r"]
        circle.g = state["g"]
        circle.b = state["b"]
        return circle

    def draw_rgb(self, win):
        """Draw the RGB values of the circle."""
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render(f"RGB: ({self.r}, {self.g}, {self.b})", True, (255, 255, 255))
        # Position text above the circle
        text_rect = self.text.get_rect()
        text_rect.centerx = self.x
        text_rect.bottom = self.y - self.radius - 5
        win.blit(self.text, text_rect)

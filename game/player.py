import pygame
from game.settings import GRAVITY, LIFT

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 30)
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = LIFT

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
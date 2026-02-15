"""
Player (Helicopter) class
"""
import pygame
from src.settings import *


class Helicopter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_speed = 0
        self.flying = False
        self.radius = PLAYER_RADIUS
        
        # Load and scale helicopter image
        try:
            image = pygame.image.load(HELICOPTER_IMAGE)
            self.image = pygame.transform.scale(image, HELICOPTER_SIZE)
        except pygame.error:
            # If image not found, use None (will draw circle only)
            self.image = None
    
    def reset(self, y=None):
        """Reset helicopter to starting position"""
        self.x = PLAYER_START_X
        if y is not None:
            self.y = y
        else:
            self.y = PLAYER_START_Y
        self.y_speed = 0
        self.flying = False
    
    def set_flying(self, flying):
        """Set flying state"""
        self.flying = flying
    
    def update(self):
        """Update helicopter position"""
        if self.flying:
            self.y_speed += GRAVITY
        else:
            self.y_speed -= GRAVITY
        self.y -= self.y_speed
    
    def draw(self, window):
        """Draw helicopter on window"""
        # Draw circle hitbox
        circle = pygame.draw.circle(window, BLACK, (int(self.x), int(self.y)), self.radius)
        
        # Draw helicopter image if available
        if self.image:
            window.blit(self.image, (self.x - 40, self.y - 30))
        
        return circle
    
    def get_rect(self):
        """Get collision rectangle for the helicopter"""
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

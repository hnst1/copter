"""
Terrain generation and management
"""
import random
import pygame
from src.settings import *


class Terrain:
    def __init__(self, window):
        self.window = window
        self.rects = []
        self.total_rects = WIN_WIDTH // RECT_WIDTH
        self.spacer = TERRAIN_VARIATION
        self.speed = INITIAL_MAP_SPEED
        self.score = 0
        self.speed_level = 0  # Track current speed level
        self.next_speed_threshold = SPEED_INCREASE_RATE  # First increase at 50 points
    
    def generate_new(self):
        """Generate new terrain"""
        self.rects = []
        top_height = random.randint(0, 300)
        
        for i in range(self.total_rects):
            top_height = random.randint(
                max(0, top_height - self.spacer),
                min(300, top_height + self.spacer)
            )
            
            # Create top and bottom rectangles
            top_rect = (i * RECT_WIDTH, 0, RECT_WIDTH, top_height)
            bot_rect = (i * RECT_WIDTH, top_height + TERRAIN_GAP, RECT_WIDTH, WIN_HEIGHT)
            
            self.rects.append(top_rect)
            self.rects.append(bot_rect)
        
        # Return a good starting Y position for player
        return top_height + 150
    
    def reset(self):
        """Reset terrain"""
        self.spacer = TERRAIN_VARIATION
        self.speed = INITIAL_MAP_SPEED
        self.score = 0
        self.speed_level = 0
        self.next_speed_threshold = SPEED_INCREASE_RATE
        return self.generate_new()
    
    def update(self):
        """Move terrain and generate new segments"""
        for i in range(len(self.rects)):
            rect = self.rects[i]
            self.rects[i] = (rect[0] - self.speed, rect[1], RECT_WIDTH, rect[3])
        
        # Keep removing off-screen rectangles and generating new ones
        # Use while loop to handle high speeds where multiple pairs go off-screen per frame
        while len(self.rects) > 0 and self.rects[0][0] + RECT_WIDTH < 0:
            # Remove leftmost pair
            self.rects.pop(0)
            self.rects.pop(0)
            self.score += 1
        
        # Keep generating new pairs until the screen is filled
        # This prevents gaps when moving at high speeds
        while len(self.rects) > 0 and self.rects[-2][0] < WIN_WIDTH:
            # Generate new pair on the right
            last_top_height = self.rects[-2][3]
            new_top_height = random.randint(
                max(0, last_top_height - self.spacer),
                min(300, last_top_height + self.spacer)
            )
            
            last_x = self.rects[-2][0]
            self.rects.append((last_x + RECT_WIDTH, 0, RECT_WIDTH, new_top_height))
            self.rects.append((last_x + RECT_WIDTH, new_top_height + TERRAIN_GAP, RECT_WIDTH, WIN_HEIGHT))
    
    def draw(self):
        """Draw terrain on window"""
        for rect in self.rects:
            pygame.draw.rect(self.window, GREEN, rect)
        
        # Draw border
        pygame.draw.rect(self.window, BLACK, [0, 0, WIN_WIDTH, WIN_HEIGHT], 12)
    
    def check_collision(self, player_rect):
        """Check if player collides with terrain"""
        for rect in self.rects:
            terrain_rect = pygame.Rect(rect)
            if player_rect.colliderect(terrain_rect):
                return True
        return False
    
    def update_difficulty(self):
        """Update speed and spacer based on score with progressive thresholds"""
        # Check if we've reached the next speed threshold
        if self.score >= self.next_speed_threshold:
            self.speed_level += 1
            # Next threshold increases progressively: 50, 100, 150, 200, etc.
            self.next_speed_threshold += SPEED_INCREASE_RATE * (self.speed_level + 1)
        
        # Calculate speed based on speed level
        self.speed = INITIAL_MAP_SPEED + self.speed_level
        
        # Spacer still increases linearly with score
        self.spacer = TERRAIN_VARIATION + self.score // SPACER_INCREASE_RATE
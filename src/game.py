"""
Main game class and game loop
"""
import pygame
from src.settings import *
from src.player import Helicopter
from src.terrain import Terrain
from src.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Copter')
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_NAME, FONT_SIZE)
        
        # Game objects
        self.player = Helicopter(PLAYER_START_X, PLAYER_START_Y)
        self.terrain = Terrain(self.window)
        self.menu = Menu(self.window)
        
        # Game state
        self.state = "MENU"  # MENU, SETTINGS, PLAYING, GAME_OVER
        self.running = True
        self.high_score = 0
        self.game_started = False
    
    def reset_game(self):
        """Reset game to initial state"""
        player_start_y = self.terrain.reset()
        self.player.reset(player_start_y)
        self.game_started = False
    
    def draw_score(self):
        """Draw score with white text and black outline for visibility"""
        score = self.terrain.score
        
        # Draw score at top
        self._draw_text_with_outline(
            f'Score: {score}',
            (20, 15),
            WHITE,
            BLACK
        )
        
        # Draw high score at bottom
        self._draw_text_with_outline(
            f'High Score: {self.high_score}',
            (20, WIN_HEIGHT - 35),
            WHITE,
            BLACK
        )
        
        # If game hasn't started, show instruction
        if not self.game_started:
            instruction = "Press SPACE to start"
            text = self.font.render(instruction, True, WHITE)
            # Add black background for better visibility
            padding = 10
            bg_rect = text.get_rect(center=(WIN_WIDTH // 2, 30))
            bg_rect.inflate_ip(padding * 2, padding)
            pygame.draw.rect(self.window, BLACK, bg_rect)
            pygame.draw.rect(self.window, WHITE, bg_rect, 2)
            self.window.blit(text, text.get_rect(center=(WIN_WIDTH // 2, 30)))
    
    def _draw_text_with_outline(self, text, pos, color, outline_color):
        """Draw text with outline for better visibility"""
        # Draw outline
        for dx, dy in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            outline_surface = self.font.render(text, True, outline_color)
            self.window.blit(outline_surface, (pos[0] + dx, pos[1] + dy))
        
        # Draw main text
        text_surface = self.font.render(text, True, color)
        self.window.blit(text_surface, pos)
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == "MENU":
                action = self.menu.handle_main_menu_event(event)
                if action == "PLAY":
                    self.state = "PLAYING"
                    self.reset_game()
                elif action == "SETTINGS":
                    self.state = "SETTINGS"
                elif action == "QUIT":
                    self.running = False
            
            elif self.state == "SETTINGS":
                action = self.menu.handle_settings_event(event)
                if action == "BACK":
                    self.state = "MENU"
            
            elif self.state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.set_flying(True)
                        if not self.game_started:
                            self.game_started = True
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.player.set_flying(False)
            
            elif self.state == "GAME_OVER":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Restart game
                        self.state = "PLAYING"
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        # Return to menu
                        self.state = "MENU"
    
    def update(self):
        """Update game state"""
        if self.state == "PLAYING" and self.game_started:
            # Update player
            self.player.update()
            
            # Update terrain
            self.terrain.update()
            self.terrain.update_difficulty()
            
            # Apply difficulty multiplier and cap at maximum speed
            difficulty_mult = self.menu.get_difficulty_multiplier()
            self.terrain.speed = min(self.terrain.speed * difficulty_mult, MAX_SPEED)
            
            # Check collision
            player_rect = self.player.get_rect()
            if self.terrain.check_collision(player_rect):
                self.state = "GAME_OVER"
                if self.terrain.score > self.high_score:
                    self.high_score = self.terrain.score
    
    def draw(self):
        """Draw current game state"""
        if self.state == "MENU":
            self.menu.draw_main_menu()
        
        elif self.state == "SETTINGS":
            self.menu.draw_settings_menu()
        
        elif self.state == "PLAYING":
            self.window.fill(BLACK)
            self.terrain.draw()
            self.player.draw(self.window)
            self.draw_score()
            pygame.display.flip()
        
        elif self.state == "GAME_OVER":
            # Keep last frame visible
            self.terrain.draw()
            self.player.draw(self.window)
            self.menu.draw_game_over(self.terrain.score, self.high_score)
            pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
        
        pygame.quit()
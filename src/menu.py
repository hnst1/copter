"""
Menu system for the game
"""
import pygame
from src.settings import *


class Button:
    def __init__(self, x, y, width, height, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = DARK_GREEN
        self.hover_color = GREEN
        self.text_color = WHITE
        self.hovered = False
    
    def draw(self, window):
        """Draw button"""
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(window, color, self.rect)
        pygame.draw.rect(window, WHITE, self.rect, 3)
        
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        window.blit(text_surface, text_rect)
    
    def check_hover(self, pos):
        """Check if mouse is hovering over button"""
        self.hovered = self.rect.collidepoint(pos)
        return self.hovered
    
    def is_clicked(self, pos):
        """Check if button is clicked"""
        return self.rect.collidepoint(pos)


class Menu:
    def __init__(self, window):
        self.window = window
        self.title_font = pygame.font.Font(FONT_NAME, TITLE_FONT_SIZE)
        self.menu_font = pygame.font.Font(FONT_NAME, MENU_FONT_SIZE)
        self.font = pygame.font.Font(FONT_NAME, FONT_SIZE)
        
        # Main menu buttons
        button_width = 300
        button_height = 60
        button_x = WIN_WIDTH // 2 - button_width // 2
        
        self.play_button = Button(button_x, 250, button_width, button_height, "Play", self.menu_font)
        self.settings_button = Button(button_x, 330, button_width, button_height, "Settings", self.menu_font)
        self.quit_button = Button(button_x, 410, button_width, button_height, "Quit", self.menu_font)
        
        # Settings menu buttons
        self.back_button = Button(button_x, 450, button_width, button_height, "Back", self.menu_font)
        
        # Settings values
        self.difficulty = "Normal"  # Easy, Normal, Hard
        self.difficulties = ["Easy", "Normal", "Hard"]
        self.difficulty_index = 1
    
    def draw_main_menu(self):
        """Draw main menu"""
        self.window.fill(BLACK)
        
        # Draw title
        title = self.title_font.render("COPTER", True, GREEN)
        title_rect = title.get_rect(center=(WIN_WIDTH // 2, 150))
        self.window.blit(title, title_rect)
        
        # Draw buttons
        self.play_button.draw(self.window)
        self.settings_button.draw(self.window)
        self.quit_button.draw(self.window)
        
        pygame.display.flip()
    
    def draw_settings_menu(self):
        """Draw settings menu"""
        self.window.fill(BLACK)
        
        # Draw title
        title = self.menu_font.render("Settings", True, GREEN)
        title_rect = title.get_rect(center=(WIN_WIDTH // 2, 100))
        self.window.blit(title, title_rect)
        
        # Draw difficulty setting
        diff_text = self.font.render("Difficulty:", True, WHITE)
        self.window.blit(diff_text, (WIN_WIDTH // 2 - 150, 250))
        
        diff_value = self.menu_font.render(self.difficulty, True, GREEN)
        diff_value_rect = diff_value.get_rect(center=(WIN_WIDTH // 2, 300))
        self.window.blit(diff_value, diff_value_rect)
        
        # Draw arrows for difficulty selection
        left_arrow = self.menu_font.render("<", True, WHITE)
        right_arrow = self.menu_font.render(">", True, WHITE)
        self.window.blit(left_arrow, (WIN_WIDTH // 2 - 150, 280))
        self.window.blit(right_arrow, (WIN_WIDTH // 2 + 120, 280))
        
        # Instructions
        instructions = self.font.render("Use arrow keys or click arrows to change difficulty", True, GRAY)
        inst_rect = instructions.get_rect(center=(WIN_WIDTH // 2, 370))
        self.window.blit(instructions, inst_rect)
        
        self.back_button.draw(self.window)
        
        pygame.display.flip()
    
    def draw_game_over(self, score, high_score):
        """Draw game over overlay"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.window.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.title_font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIN_WIDTH // 2, 200))
        self.window.blit(game_over_text, game_over_rect)
        
        # Score
        score_text = self.menu_font.render(f"Score: {score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIN_WIDTH // 2, 280))
        self.window.blit(score_text, score_rect)
        
        high_score_text = self.menu_font.render(f"High Score: {high_score}", True, GREEN)
        high_rect = high_score_text.get_rect(center=(WIN_WIDTH // 2, 340))
        self.window.blit(high_score_text, high_rect)
        
        # Instructions
        restart_text = self.font.render("Press ENTER to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIN_WIDTH // 2, 420))
        self.window.blit(restart_text, restart_rect)
        
        menu_text = self.font.render("Press ESC for main menu", True, WHITE)
        menu_rect = menu_text.get_rect(center=(WIN_WIDTH // 2, 450))
        self.window.blit(menu_text, menu_rect)
    
    def handle_main_menu_event(self, event):
        """Handle main menu events, returns action"""
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            self.play_button.check_hover(pos)
            self.settings_button.check_hover(pos)
            self.quit_button.check_hover(pos)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.play_button.is_clicked(pos):
                return "PLAY"
            elif self.settings_button.is_clicked(pos):
                return "SETTINGS"
            elif self.quit_button.is_clicked(pos):
                return "QUIT"
        
        return None
    
    def handle_settings_event(self, event):
        """Handle settings menu events"""
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            self.back_button.check_hover(pos)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.back_button.is_clicked(pos):
                return "BACK"
            
            # Check arrow clicks
            if 280 < pos[1] < 330:
                if WIN_WIDTH // 2 - 150 < pos[0] < WIN_WIDTH // 2 - 100:
                    self.change_difficulty(-1)
                elif WIN_WIDTH // 2 + 100 < pos[0] < WIN_WIDTH // 2 + 150:
                    self.change_difficulty(1)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.change_difficulty(-1)
            elif event.key == pygame.K_RIGHT:
                self.change_difficulty(1)
        
        return None
    
    def change_difficulty(self, direction):
        """Change difficulty setting"""
        self.difficulty_index = (self.difficulty_index + direction) % len(self.difficulties)
        self.difficulty = self.difficulties[self.difficulty_index]
    
    def get_difficulty_multiplier(self):
        """Get speed multiplier based on difficulty"""
        if self.difficulty == "Easy":
            return 0.7
        elif self.difficulty == "Normal":
            return 1.0
        else:  # Hard
            return 1.5

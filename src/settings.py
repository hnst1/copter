"""
Game settings and configuration constants
"""
import pygame

# Window settings
WIN_WIDTH = 1000
WIN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 180, 0)

# Player settings
PLAYER_START_X = 100
PLAYER_START_Y = 300
PLAYER_RADIUS = 20
GRAVITY = 0.3

# Terrain settings
RECT_WIDTH = 10
TERRAIN_GAP = 300  # Gap between top and bottom terrain
TERRAIN_VARIATION = 10  # Initial spacer value

# Game settings
INITIAL_MAP_SPEED = 2
SPEED_INCREASE_RATE = 50  # Base interval for speed increases (progressive: 50, 100, 150, 200...)
SPACER_INCREASE_RATE = 100  # Score points needed to increase terrain variation
MAX_SPEED = 40  # Maximum terrain speed to keep game playable

# Font settings
FONT_NAME = 'freesansbold.ttf'
FONT_SIZE = 20
MENU_FONT_SIZE = 40
TITLE_FONT_SIZE = 60

# Asset paths
HELICOPTER_IMAGE = 'assets/helicopter.png'
HELICOPTER_SIZE = (60, 60)
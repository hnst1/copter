# Copter Game - Quick Start Guide

## Setup Instructions

### 1. Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### 2. Installation Steps

```bash
# Navigate to the project directory
cd copter

# Install dependencies
pip install -r requirements.txt

# Add your helicopter image
# Place helicopter.png in the assets/ folder
```

### 3. Run the Game

```bash
python main.py
```

## File Structure Overview

### Core Files
- **main.py** - Entry point, run this to start the game
- **requirements.txt** - Python dependencies

### Source Code (`src/` folder)
- **game.py** - Main game loop, state management, and orchestration
- **player.py** - Helicopter class with movement and collision detection
- **terrain.py** - Procedural terrain generation and scrolling
- **menu.py** - Menu system (main menu, settings, game over screen)
- **settings.py** - All configurable constants and parameters

### Assets (`assets/` folder)
- **helicopter.png**
  - Place your helicopter image here
  - Game will work without it (shows black circle instead)

## Troubleshooting

### "No module named pygame"
```bash
pip install pygame
```

### "Cannot find helicopter.png"
- Game will still run (shows black circle)
- Add the image to `assets/helicopter.png` to see the sprite

### Game runs too fast/slow
- Adjust `FPS` in `src/settings.py` (default: 60)

### Terrain too hard/easy
- Use Settings menu in-game to change difficulty
- Or modify `INITIAL_MAP_SPEED` in `src/settings.py`

## Next Steps

### Suggested Enhancements
1. Add sound effects and background music
2. Implement particle effects for collisions
3. Add different terrain themes (lava, ice, space)
4. Create power-ups (shields, slow-motion)
5. Add multiplayer support
6. Implement online leaderboard
7. Add achievements system

### Learning Resources
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Game Development Tutorial](https://realpython.com/pygame-a-primer/)

## Contact & Support

For questions or improvements, feel free to modify the code!
The project is well-documented and uses clear, readable code structure.

Happy flying! 🚁

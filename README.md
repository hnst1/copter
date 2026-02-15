# Copter Game

A 2D helicopter navigation game built with Python and Pygame.

## Overview

Navigate a helicopter through dynamically generated terrain that increases in difficulty as you progress. Use precise timing and control to achieve the highest score possible.

## Features

- **Dynamic Terrain Generation**: Procedurally generated caves that create unique gameplay each time
- **Progressive Difficulty**: Speed and terrain variation increase as your score climbs
- **Main Menu**: Clean interface with play, settings, and quit options
- **Settings Menu**: Adjust difficulty (Easy, Normal, Hard)
- **High Score Tracking**: Keep track of your best runs
- **Pause Before Start**: Game waits for your first input before beginning
- **Game Over Options**: Restart or return to main menu

## Project Structure

```
copter_game/
├── main.py                 # Entry point
├── assets/
│   └── helicopter.png      # Helicopter sprite
└── src/
    ├── __init__.py         # Package initialization
    ├── game.py             # Main game loop and state management
    ├── player.py           # Helicopter class
    ├── terrain.py          # Terrain generation and collision
    ├── menu.py             # Menu system
    └── settings.py         # Game configuration constants
```

## Controls

- **SPACEBAR**: Fly up (hold to ascend, release to descend)
- **ENTER**: Restart game (when game over)
- **ESC**: Return to main menu (when game over)
- **ARROW KEYS**: Navigate settings menu
- **MOUSE**: Click menu buttons

## Installation

1. Ensure you have Python 3.7+ installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Place your `helicopter.png` image in the `assets/` folder
4. Run the game:
   ```bash
   python main.py
   ```

## Gameplay Tips

- The helicopter constantly falls when not actively flying
- Timing is key - tap spacebar rhythmically rather than holding continuously
- Watch the terrain ahead to plan your movements
- Easy difficulty is great for learning, Normal provides balanced challenge, Hard is for experts
- The terrain gap stays constant, but variation increases with score

## Difficulty Levels

- **Easy**: 70% speed - More time to react
- **Normal**: 100% speed - Standard challenge
- **Hard**: 150% speed - Expert mode for skilled players

## Customization

All game parameters can be adjusted in `src/settings.py`:
- Window dimensions
- Player speed and gravity
- Terrain generation parameters
- Colors and visual settings
- Difficulty scaling rates

## Development

Built with:
- Python 3
- Pygame 2.x

## License

Open source - feel free to modify and improve!

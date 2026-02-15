# Copter Game - Architecture Overview

## Component Interaction Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                           main.py                               │
│                    (Entry Point - starts game)                  │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                         game.py                                 │
│                   (Game State Manager)                          │
│                                                                 │
│  States: MENU → SETTINGS → PLAYING → GAME_OVER                 │
│                                                                 │
│  Responsibilities:                                              │
│  • Main game loop (update, draw, handle events)                 │
│  • State transitions                                            │
│  • High score tracking                                          │
│  • Coordinates all other components                             │
└───────┬──────────────┬──────────────┬─────────────┬────────────┘
        │              │              │             │
        ▼              ▼              ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌─────────────┐ ┌─────────────┐
│  player.py   │ │  terrain.py  │ │   menu.py   │ │settings.py  │
│              │ │              │ │             │ │             │
│ Helicopter   │ │   Terrain    │ │    Menu     │ │ Constants   │
│   Class      │ │    Class     │ │   System    │ │ & Config    │
└──────────────┘ └──────────────┘ └─────────────┘ └─────────────┘
```

## File Responsibilities

### main.py
```python
Purpose: Entry point
- Creates Game instance
- Starts game loop
```

### src/game.py (GAME STATE MANAGER)
```python
Manages:
- Game states (menu, playing, game over)
- Event handling for all states
- Coordinating updates and rendering
- High score persistence
- Collision detection coordination

Key Methods:
- run()           # Main game loop
- handle_events() # Process pygame events
- update()        # Update game state
- draw()          # Render current state
- reset_game()    # Initialize new game
```

### src/player.py (HELICOPTER)
```python
Manages:
- Helicopter position and movement
- Flying physics (gravity, speed)
- Image rendering
- Collision rectangle

Key Methods:
- update()        # Apply physics
- draw()          # Render helicopter
- set_flying()    # Control flying state
- reset()         # Return to start position
```

### src/terrain.py (TERRAIN SYSTEM)
```python
Manages:
- Procedural terrain generation
- Terrain scrolling
- Difficulty progression
- Score tracking
- Collision detection

Key Methods:
- generate_new()      # Create new terrain
- update()            # Scroll and regenerate
- draw()              # Render terrain
- check_collision()   # Detect hits
- update_difficulty() # Scale speed/variation
```

### src/menu.py (UI SYSTEM)
```python
Manages:
- Main menu
- Settings menu
- Game over screen
- Buttons and UI elements
- Difficulty settings

Key Methods:
- draw_main_menu()
- draw_settings_menu()
- draw_game_over()
- handle_main_menu_event()
- handle_settings_event()
```

### src/settings.py (CONFIGURATION)
```python
Contains:
- Window dimensions
- Colors
- Physics constants
- Terrain parameters
- File paths
- All tweakable values
```

## Data Flow

### Game Start Flow
```
User runs main.py
    ↓
Game.__init__() creates all objects
    ↓
Game state = "MENU"
    ↓
Menu displays
    ↓
User clicks "Play"
    ↓
Game.reset_game() called
    ↓
Terrain generates new map
    ↓
Player positioned at safe starting location
    ↓
Game state = "PLAYING"
    ↓
Game waits for spacebar (game_started = False)
```

### Game Loop Flow (60 FPS)
```
┌─────────────────────────────────────┐
│ While running:                      │
│                                     │
│  1. Clock.tick(60)                  │
│     ↓                               │
│  2. handle_events()                 │
│     • Check keyboard/mouse input    │
│     • Update flying state           │
│     • Handle menu clicks            │
│     ↓                               │
│  3. update()                        │
│     • Player.update() (if started)  │
│     • Terrain.update() (if started) │
│     • Terrain.update_difficulty()   │
│     • Check collisions              │
│     ↓                               │
│  4. draw()                          │
│     • Clear screen                  │
│     • Terrain.draw()                │
│     • Player.draw()                 │
│     • Draw score/UI                 │
│     • pygame.display.flip()         │
│     ↓                               │
│  (repeat)                           │
└─────────────────────────────────────┘
```

### Collision Detection Flow
```
Each frame (in game.update()):
    ↓
Get player rectangle (player.get_rect())
    ↓
Pass to terrain.check_collision(player_rect)
    ↓
Terrain loops through all rectangles
    ↓
If collision detected:
    ↓
Game state changes to "GAME_OVER"
    ↓
Update high score if needed
    ↓
Draw game over overlay
    ↓
Wait for Enter (restart) or ESC (menu)
```

## State Machine

```
     ┌──────────┐
     │   MENU   │ ← (ESC from game over)
     └────┬─────┘
          │ (Click Play)
          ↓
     ┌──────────┐
     │ PLAYING  │
     └────┬─────┘
          │ (Collision)
          ↓
     ┌──────────┐
     │GAME_OVER │
     └────┬─────┘
          │ (Enter)
          └──→ PLAYING

     MENU ←→ SETTINGS (Click Settings/Back)
```

## Key Design Patterns

### 1. Separation of Concerns
- Each class has ONE clear responsibility
- Game class orchestrates, doesn't implement details
- Easy to test and modify individual components

### 2. Object-Oriented Design
- Encapsulation: Each object manages its own state
- Clear interfaces: Public methods define how objects interact
- Inheritance possible: Easy to create new player types

### 3. Configuration Externalization
- All magic numbers in settings.py
- No hardcoded values in logic
- Easy to balance and tune

### 4. State Pattern
- Game uses explicit states
- Clear state transitions
- Easy to add new states (e.g., PAUSED)

## Adding New Features - Examples

### Example 1: Add Pause Feature
1. Add PAUSED state to game.py
2. Add pause button handling in handle_events()
3. Skip update() when paused
4. Draw pause overlay

### Example 2: Add Power-up
1. Create src/powerup.py with Powerup class
2. Import in game.py
3. Generate power-ups in terrain.py
4. Check collision in game.py
5. Apply effect to player

### Example 3: Add Sound
1. Add sound files to assets/
2. Load sounds in game.__init__()
3. Play sounds on events (collision, score, etc.)

## Performance Considerations

- Terrain only regenerates when needed (off-screen)
- Fixed timestep (60 FPS)
- Efficient collision detection (only check visible rectangles)
- Minimal object creation per frame
- Pre-loaded assets (fonts, images)

## Testing Strategy

Suggested test areas:
1. **Player Physics**: Test gravity, flying mechanics
2. **Collision Detection**: Test edge cases
3. **Terrain Generation**: Ensure no impossible gaps
4. **Score Tracking**: Verify accurate counting
5. **State Transitions**: Test all menu flows
6. **Difficulty Scaling**: Verify speed/spacer increases

## Conclusion

This architecture provides:
✅ Clean separation of concerns
✅ Easy to understand and modify
✅ Testable components
✅ Scalable for new features
✅ Professional code organization

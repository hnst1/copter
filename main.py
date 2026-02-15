"""
Copter Game - Main Entry Point

A helicopter navigation game where you fly through dynamically generated terrain.
Use SPACEBAR to control the helicopter's altitude and avoid obstacles.
"""
from src.game import Game


def main():
    """Initialize and run the game"""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

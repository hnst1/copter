import pygame

from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.player import Player

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            Player.flap()

    if event.type == pygame.MOUSEBUTTONDOWN:
        Player.flap()

def run():
    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    clock = pygame.time.Clock()
    player = Player(100, SCREEN_HEIGHT // 2)

    running = True

    while running:
        clock.tick(FPS)
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type in (
                pygame.KEYDOWN,
                pygame.MOUSEBUTTONDOWN
            ):
                player.flap()

        player.update()
        player.draw(screen)
        pygame.display.flip()
    pygame.quit()
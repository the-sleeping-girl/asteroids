import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    game_clock = pygame.time.Clock()
    dt = 0
    player_user = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        player_user.update(dt)
        player_user.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        # print(f"FPS: {game_clock.get_fps():.2f}")




if __name__ == "__main__":
    main()

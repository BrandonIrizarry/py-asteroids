import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    exit_game_loop = False

    while exit_game_loop == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game_loop = True

        for u in updatable:
            u.update(dt)

        # Render the game.
        screen.fill((0,0,0))

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if a.collides_with(player):
                print("Game over!")
                exit_game_loop = True

            for s in shots:
                if s.collides_with(a):
                    s.kill()
                    a.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()

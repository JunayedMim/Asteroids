import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #print(f"{dt}")
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    #Objects
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    asteroidfield = AsteroidField()
    
    #Game loop
    while True:
        dt = clock.tick(60) / 1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide_with(player) is True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        



if __name__ == "__main__":
    main()

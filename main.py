import pygame
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys

def main():
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adding containers to player
    Player.containers = (updatable,drawable)

    # Adding containers to asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    # Adding containers to asteroid field
    AsteroidField.containers = (updatable)
    
    # Adding containers to shots
    Shot.containers = (shots,updatable, drawable)

    # Initializing the pygame modules
    pygame.init()

    # Defining the game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # Starting a clock object to introduce fps into the game
    clock = pygame.time.Clock()
    dt = 0
    
    # initializing player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroid_field = AsteroidField()
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                sys.exit(0)

        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.update()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Adding containers to player
    Player.containers = (updatable,drawable)

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
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.update()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

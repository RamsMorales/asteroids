import pygame
from constants import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initializing the pygame modules
    pygame.init()

    # Defining the game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # Starting a clock object to introduce fps into the game
    clock = pygame.time.Clock()
    dt = 0
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.update()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

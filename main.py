# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



def main():
    # initialize pygame
    pygame.init() # this is a function that initializes all the modules required for Pygame
    # create a window with a width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # CREATE GAME LOOP
    running = True
    while running:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

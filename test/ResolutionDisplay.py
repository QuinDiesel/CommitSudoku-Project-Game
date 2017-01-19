'''Euromast, Copyright 2017, CommitSudoku'''

import pygame

# Kleuken
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Bright_red = (204,0,0)
Yellow = (255,255,0)
Blue = (0,0,255)
Green = (0,255,0)
Bright_green = (0,204,0)

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False


def program():
    width = 640
    height = 480
    screen_size = (width, height) #gebonden resolutie

    pygame.init() #startgame

    screen = pygame.display.set_mode(screen_size)  # pygame code om scherm aan te roepen

    while not process_events():

        screen.fill((wit)) #kleur display
        pygame.display.flip()



program()
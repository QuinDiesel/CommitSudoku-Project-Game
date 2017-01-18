'''Euromast, Copyright 2017, CommitSudoku'''

import pygame
import menu


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False


def program():
    width = 800
    height = 600
    screen_size = (width, height) #gebonden resolutie

    pygame.init() #startgame

    screen = pygame.display.set_mode(screen_size)  # pygame code om scherm aan te roepen

    while not process_events():

        screen.fill((255,255,255)) #kleur display

        pygame.display.flip()


program()

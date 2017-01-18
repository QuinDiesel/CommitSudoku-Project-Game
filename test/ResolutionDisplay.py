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

        screen.blit(menu.title, (240, 0))
        screen.blit(menu.a1, (0, 50))
        screen.blit(menu.a2, (0, 70))
        screen.blit(menu.a3, (0, 90))
        screen.blit(menu.a4, (0, 110))
        screen.blit(menu.a5, (0, 130))
        screen.blit(menu.a6, (0, 150))
        screen.blit(menu.a7, (0, 170))
        screen.blit(menu.a8, (0, 190))
        screen.blit(menu.a9, (0, 210))

        pygame.display.flip()


program()

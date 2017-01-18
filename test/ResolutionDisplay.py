'''Euromast, Copyright 2017, CommitSudoku'''

import pygame


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False

class Game():
    def __init__(self):
        width = 640
        height = 480
        screen_size = (width, height) #gebonden resolutie

        pygame.init() #startgame

        screen = pygame.display.set_mode(screen_size)#pygame code om scherm aan te roepen
        name = pygame.display.set_caption('Euromast')
        while not process_events():

            screen.fill((255,255,255)) #kleur display
            pygame.display.flip()

    def Buttons(self):


def program():
    game = Game()


program()
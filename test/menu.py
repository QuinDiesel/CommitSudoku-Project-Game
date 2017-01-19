import pygame

# Start de fonts!
pygame.font.init()

# Welk font willen we gaan gebruiken
important = pygame.font.SysFont("Comic sans", 30)
text = pygame.font.SysFont(None, 24)

# Alle spelregels opgedeeld in variabelen
title = important.render('Game Rules', True, (0, 0, 0))
a1 = text.render('2 - 4 players', True, (0, 0, 0))
a2 = text.render('50 seconds per turn', True, (0, 0, 0))
a3 = text.render('Each round, the player is given a multiple choice question', True, (0, 0, 0))
a4 = text.render('The questions are separated into 4 categories', True, (0, 0, 0))
a5 = text.render('Blue = sports, Green = geography, red = entertainment, yellow = history', True, (0, 0, 0))
a6 = text.render('Each player rolls the dice and the player with the highest number chooses a category first', True,
                 (0, 0, 0))
a7 = text.render(
    'The remaining players choose a category from the remaining categories (only one player per category at the start of the game)',
    True, (0, 0, 0))
a8 = text.render(
    'The player who threw the highest number will start the game first. After the first player, the game continues clockwise with the next player',
    True, (0, 0, 0))
a9 = text.render(
    'Players put their characters on the wooden part of the playing board in front of their chosen category.', True,
    (0, 0, 0))

# Als we de spelregels naar ResolutionDisplay.py willen zetten, voeg deze code toe.
'''
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
'''

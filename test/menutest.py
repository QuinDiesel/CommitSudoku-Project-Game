import pygame

pygame.font.init()

important = pygame.font.SysFont(None, 30)
text = pygame.font.SysFont(None, 24)


# screen =


def displayRules():
    from ResolutionDisplay import screen

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

    screen.blit(title, (240, 0))
    screen.blit(a1, (0, 50))
    screen.blit(a2, (0, 70))
    screen.blit(a3, (0, 90))
    screen.blit(a4, (0, 110))
    screen.blit(a5, (0, 130))
    screen.blit(a6, (0, 150))
    screen.blit(a7, (0, 170))
    screen.blit(a8, (0, 190))
    screen.blit(a9, (0, 210))

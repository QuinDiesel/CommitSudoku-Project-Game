import pygame

# init fonts
pygame.font.init()

# Welk font willen we gaan gebruiken
myfont = pygame.font.SysFont("Monospace", 20)

textsurface = myfont.render('Hier zijn de spelregels', True, (0, 0, 0))

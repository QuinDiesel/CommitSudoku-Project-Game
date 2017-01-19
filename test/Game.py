import pygame, sys
from pygame.locals import *

# Setup voor de verschillende categorieën
sports = 0
geography = 1
entertainment = 2
history = 3
start = 4

# Alle tegels tekenen en toevoegen aan een tilemap
tilemap = [
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [entertainment, history, sports, geography],
    [start, start, start, start]
]

# Setup voor de kleuren
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Link de kleuren aan de 4 categorieën
colours = {
    entertainment: red,
    history: yellow,
    sports: blue,
    geography: green,
    start: black
}

# Dimensies van de map
tilesize = 200
mapwidth = 4
mapheight = 16

# Test display plaatsen
pygame.init()
surface = pygame.display.set_mode((800, 600))

while True:
    # Pak alle user events (quit e.d.)
    for event in pygame.event.get():
        # Check of de user wil stoppen
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Loop door alle reien om de map te tekenen
    for row in range(mapheight):
        for column in range(mapwidth):
            # Teken een vierkantje met kleur
            pygame.draw.rect(surface, colours[tilemap[row][column]], (column * tilesize, row * 38, tilesize, tilesize))

    pygame.display.update()

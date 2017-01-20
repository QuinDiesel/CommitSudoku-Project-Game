import pygame, sys
from pygame.locals import *


class Game:
    def startGame(self):
        # Setup voor de verschillende categorieën
        sports = 0
        geography = 1
        entertainment = 2
        history = 3
        start = 4

        # Setup voor de afbeeldingen per categorie
        textures = {
            entertainment: pygame.image.load("img/Rood Vakje.jpg"),
            history: pygame.image.load("img/Geel Vakje.jpg"),
            sports: pygame.image.load("img/Blauw Vakje.jpg"),
            geography: pygame.image.load("img/Groen Vakje.jpg"),
            start: pygame.image.load("img/QuitButton.png")
        }

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

        # Dimensies van de map
        tilesize = 40
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
                    surface.blit(textures[tilemap[row][column]], (column * 200, row * tilesize))

            pygame.display.update()

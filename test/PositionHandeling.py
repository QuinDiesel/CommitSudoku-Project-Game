import pygame

pygame.init()

def color():
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (255,0,0)
    blue = (0,0,255)
    yellow = (255,255,0)

def Game():
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption("TESTLOCATIE")

    pygame.display.update()

    gameExit = False

    while not gameExit: #while loop om kruisje te gebruiken
        for event in pygame.event.get():
             #print(event) #haal hashtag weg om position te zien
            if event.type == pygame.QUIT:
                gameExit = True

    pygame.quit()
    quit()

Game()

import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TESTLOCATIE")
pygame.display.update()

gameExit = False

lead_x = 300  # startlocatie
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()

while not gameExit:  # while loop om de game te laten runnen
    for event in pygame.event.get():
        # print(event) #haal hashtag weg om position te zien
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:  # pijltjes richting instellen
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    lead_x += lead_x_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()

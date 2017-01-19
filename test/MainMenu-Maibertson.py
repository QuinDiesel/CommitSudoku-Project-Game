import pygame
import math

pygame.init()

# kleuren

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Bright_red = (204,0,0)
Yellow = (255,255,0)
Blue = (0,0,255)
Green = (0,255,0)
Bright_green = (0,204,0)

# Buttons
StartButton = pygame.image.load('img/StartButton.png')
StartButtonGray = pygame.image.load('img/StartButtonGray.png')
QuitButton = pygame.image.load('img/QuitButton.png')
QuitButtonGray = pygame.image.load('img/QuitButtonGray.png')
InstructionButton = pygame.image.load('img/ButtonInstructionWhite.png')
InstructionButtonGray = pygame.image.load('img/ButtonInstructionGray.png')

# Background
BG = pygame.image.load('img/BackDropv2.png')

# Display

gameDisplay = pygame.display.set_mode((800,600))

# GameName
pygame.display.set_caption('EuroMast v.0.0.2')


def Button(x, y, function):
    mouse = pygame.mouse.get_pos()
    if x + 100 > mouse[0] > x and y + 50 > mouse[1] > y:
        if function == "start":
            gameDisplay.blit(StartButton, (x, y))
            #if function == 'start':

        else:
            gameDisplay.blit(QuitButton, (x, y))
    else:
        if function == "start":
            gameDisplay.blit(StartButtonGray, (x, y))
            #if function == 'start':
                #gameDisplay.blit(InstructionButtonGray,(x,y))
        else:
            gameDisplay.blit(QuitButtonGray, (x, y))

def Button_2(x, y, instruc):
    mouse = pygame.mouse.get_pos()
    if x + 250 > mouse[0] > x and y + 50 > mouse[1] > y:
        gameDisplay.blit(InstructionButton, (x,y))
    else:
        gameDisplay.blit(InstructionButtonGray, (x,y))


pygame.display.update()

# GameIntro
def game_intro():
        into = True

while game_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
        gameDisplay.blit(BG,(0,0))



        Button(280,300,'start')
        Button(430,300,'quit')
        Button_2(280,350,'learn')
        #Button_2(280,350,'learn')

        pygame.display.update()



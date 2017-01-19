import pygame
import math

pygame.init()

pygame.mixer.music.load("music_intro.ogg")
pygame.mixer.music.play(-1,0.0)

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
StartButton = pygame.image.load('img/StartButtonWhite.png')
StartButtonGray = pygame.image.load('img/StartButtonGray.png')
QuitButton = pygame.image.load('img/QuitButtonWhite.png')
QuitButtonGray = pygame.image.load('img/QuitButtonGray.png')
InstructionButton = pygame.image.load('img/ButtonInstructionWhite.png')
InstructionButtonGray = pygame.image.load('img/ButtonInstructionGray.png')
InstructionRuleList = pygame.image.load('img/InstructionsView.jpg')

# Background
BG = pygame.image.load('img/BackDropv2.png')

# Display

gameDisplay = pygame.display.set_mode((800,600))

# GameName
pygame.display.set_caption('EuroMast v.0.1.5')

def click():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

def Instruction():
     gameDisplay.blit(InstructionRuleList, (0, 0))



def Button(x, y, function,):
    mouse = pygame.mouse.get_pos()
    if x + 100 > mouse[0] > x and y + 50 > mouse[1] > y:
        if function == "start":
            gameDisplay.blit(StartButton, (x, y))

        else:
            gameDisplay.blit(QuitButton, (x, y))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                quit()
    else:
        if function == "start":
            gameDisplay.blit(StartButtonGray, (x, y))

        else:
            gameDisplay.blit(QuitButtonGray, (x, y))

def Button_2(x, y, instruc,action = None):
    mouse = pygame.mouse.get_pos()
    #click = pygame.mouse.get_pressed()
    if x + 250 > mouse[0] > x and y + 50 > mouse[1] > y:
        gameDisplay.blit(InstructionButton, (x,y))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Instruction()

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




        Button(280,220,'start')
        Button(430,220,'quit')
        Button_2(280,273,'learn','instruction')
        #Button_2(280,350,'learn')




        pygame.display.update()
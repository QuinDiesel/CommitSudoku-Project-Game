import pygame
import random


# Initialize shit
pygame.init()
screen_width = 400
screen_height = 400

gameDisplay = pygame.display.set_mode((screen_width, screen_height))

# Load in the dice
diceOne = pygame.image.load("img/dice/Dice1Wit.png")
diceTwo = pygame.image.load("img/dice/Dice2Wit.png")
diceThree = pygame.image.load("img/dice/Dice3Wit.png")
diceFour = pygame.image.load("img/dice/Dice4Wit.png")
diceFive = pygame.image.load("img/dice/Dice5Wit.png")
diceSix = pygame.image.load("img/dice/Dice6Wit.png")


def diceRoll():
    dice = random.randint(1, 6)

    if dice == 1:
        gameDisplay.blit(diceOne, (0, 0))
    elif dice == 2:
        gameDisplay.blit(diceTwo, (0, 0))
    elif dice == 3:
        gameDisplay.blit(diceThree, (0, 0))
    elif dice == 4:
        gameDisplay.blit(diceFour, (0, 0))
    elif dice == 5:
        gameDisplay.blit(diceFive, (0, 0))
    elif dice == 6:
        gameDisplay.blit(diceSix, (0, 0))

    return dice

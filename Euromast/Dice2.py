import pygame
import random
import Game


# Load in the dice
diceOne = pygame.image.load("img/Dice1Wit.png")
diceTwo = pygame.image.load("img/Dice2Wit.png")
diceThree = pygame.image.load("img/Dice3Wit.png")
diceFour = pygame.image.load("img/Dice4Wit.png")
diceFive = pygame.image.load("img/Dice5Wit.png")
diceSix = pygame.image.load("img/Dice6Wit.png")


def diceRoll():
    dice = random.randint(1, 6)
    print(dice)

    return dice

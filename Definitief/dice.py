import pygame
import random

#Cijfers 1 & 2 gedobbeld = 1 stap in de gekozen richting
#Cijfers 3 & 4 gedobbeld = 2 stapen in de gekozen richting
#Cijfers 5 & 6 gedobbeld = 3 stappen in de gekozen richting


#Initialize all imported pygame modules
pygame.init()
screen_width = 400
screen_height = 400
dice_number = 1
first_dice = 0


pygame.display.set_caption("Dice rol")
gameDisplay = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
already_roll = False

#Import Images for Dice 1 - 6
diceOne = pygame.image.load("Dice1Wit.png")
diceTwo = pygame.image.load("Dice2Wit.png")
diceThree = pygame.image.load("Dice3Wit.png")
diceFour = pygame.image.load("Dice4Wit.png")
diceFive = pygame.image.load("Dice5Wit.png")
diceSix = pygame.image.load("Dice6Wit.png")

#Colors
white = 255, 255, 255
black = 0, 0, 0


def roll_a_dice():
    """
    # One dice are randomly rolled and have their values returned.
    >>> roll_dice()
    0
    >>> roll_dice()
    1
    >>> roll_dice()
    6
    """

    dice = random.randrange(1,7);
    return dice

def display_dice(first):
    display_first(first)

#Determines which first dice is used
def display_first(first):
    if(first == 1):
        gameDisplay.blit(diceOne, (screen_width/4, 0))
    elif(first == 2):
        gameDisplay.blit(diceTwo, (screen_width/4, 0))
    elif(first == 3):
        gameDisplay.blit(diceThree, (screen_width/4, 0))
    elif(first == 4):
        gameDisplay.blit(diceFour, (screen_width/4, 0))
    elif(first == 5):
        gameDisplay.blit(diceFive, (screen_width/4, 0))
    elif(first == 6):
        gameDisplay.blit(diceSix, (screen_width/4, 0))

#Tells user how to roll
def rollMessage(text):
    font = pygame.font.SysFont("monospace", 15)

    #Render the text
    produceText = font.render(text, 1, (black))
    gameDisplay.blit(produceText, (screen_width/8, screen_height/5))

#Produce roll results in text
"""
def rollMessageResult(text):
    font = pygame.font.SysFont("monospace", 15)

    #Render the text, 1 = aliasing
    produceText = font.render(text, 1, black)
    gameDisplay.blit(produceText, (screen_width/8, screen_height/2))
"""

#Our roll will display message with our roll converted to text
def before_roll():
    rollMessage("Please hit space to roll your dice")

"""
def our_roll():
    #Completed roll message, cast int to string and output the message
    text = "You have completed your roll " + str(first_dice) + "."
    print(text)
    rollMessageResult(text)
"""

#We don't want our roll value before the first roll occurs
rollOccur = False
while already_roll == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            already_roll = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_dice = roll_a_dice()
                rollOccur = True

    gameDisplay.fill(white)
    before_roll()
    display_dice(first_dice)

    #If the roll is requested, our_roll will be execute
    #if(rollOccur):
        #our_roll()
    pygame.display.update()
    clock.tick(30)

# Once the loop exits, the program will quit.
# Loop will exit when the 'Exit' button on the window is clicked.This bit of code just ensures you can actually
# click that and exit.
pygame.quit()
quit()






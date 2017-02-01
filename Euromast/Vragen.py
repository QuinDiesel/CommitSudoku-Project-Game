import pygame
import random
correct = False

# Set up a button class for later usage
class Button:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.surface = w * h

    def buttonHover(self):
        mouse = pygame.mouse.get_pos()

        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            return True

    def keyboard(self):
        keyb = pygame.key.get()

def vragen():
    gameDisplay = pygame.display.set_mode((800, 600))


    bg = pygame.image.load('img/Wolken.png')
    P1 = pygame.image.load('img/B1.png')
    P2 = pygame.image.load('img/B2.png')
    P3 = pygame.image.load('img/R2.png')
    P4 = pygame.image.load('img/R1.png')
    P5 = pygame.image.load('img/Y1.png')
    P6 = pygame.image.load('img/Y2.png')
    P7 = pygame.image.load('img/G1.png')
    P8 = pygame.image.load('img/G2.png')

    question = random.choice([P1, P2, P3, P4, P5, P5, P6, P7, P8])

    wboximg = pygame.image.load('img/wbox.png')
    xboximg = pygame.image.load('img/xbox.png')

    BackButtonImg = pygame.image.load('img/BackButton.png')
    BackButtonGrayImg = pygame.image.load('img/BackButtonGray.png')

    # Create instances of the button
    buttonA = Button(200, 232, 47, 42, wboximg)
    buttonAx = Button(200, 232, 47, 42, xboximg)
    buttonB = Button(200, 274, 47, 42, wboximg)
    buttonBx = Button(200, 274, 47, 42, xboximg)
    buttonC = Button(200, 316, 47, 42, wboximg)
    buttonCx = Button(200, 316, 47, 42, xboximg)
    buttonD = Button(200, 357, 47, 42, wboximg)
    buttonDx = Button(200, 357, 47, 42, xboximg)

    phase = "vraag"
    loop = 1

    while True:
        pygame.mouse.get_pos()
        # Check if user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((0, 0, 0))

        if phase == "vraag":
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(question, (200, 150))

            gameDisplay.blit(buttonD.img, (buttonD.x, buttonD.y))
            gameDisplay.blit(buttonC.img, (buttonC.x, buttonC.y))
            gameDisplay.blit(buttonB.img, (buttonB.x, buttonB.y))
            gameDisplay.blit(buttonA.img, (buttonA.x, buttonA.y))

            choice = ''

            if Button.buttonHover(buttonD):
                gameDisplay.blit(xboximg, (200, 357))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    choice = 'D'

            elif Button.buttonHover(buttonC):
                gameDisplay.blit(xboximg, (200, 316))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    choice = 'C'

            elif Button.buttonHover(buttonB):
                gameDisplay.blit(xboximg, (200, 274))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    choice = 'B'

            elif Button.buttonHover(buttonA):
                gameDisplay.blit(xboximg, (200, 232))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    choice = 'A'

            if choice == 'A':
                global correct
                correct = True
                return True
            elif choice == 'B' or choice == 'C' or choice == 'D':
                correct = False
                return False

            pygame.display.flip()

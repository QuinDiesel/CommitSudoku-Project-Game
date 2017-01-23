import pygame


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


def start_program():
    # Imports
    import Definitief.Game
    import Definitief.Instructions
    import Definitief.Rules

    # Initialize pygame and music
    pygame.init()
    pygame.mixer.music.load('music.ogg')
    pygame.mixer.music.play(-1, 0.0)

    # Load in the images
    startButtonImg = pygame.image.load('../img/StartButtonWhite.png')
    startButtonGrayImg = pygame.image.load('img/StartButtonGray.png')
    quitButtonImg = pygame.image.load('img/QuitButtonWhite.png')
    quitButtonGrayImg = pygame.image.load('img/QuitButtonGray.png')
    backGroundImg = pygame.image.load('img/BackDrop.png')
    buttonInstructionImg = pygame.image.load('img/ButtonInstructionWhite.png')
    buttonInstructionGrayImg = pygame.image.load('img/ButtonInstructionGray.png')
    buttonGameRulesImg = pygame.image.load('img/GameRulesWhite.png')
    buttonGameRulesGrayImg = pygame.image.load('img/GameRulesGray.png')

    # Set up a display with title
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('EuroMast v0.2.0.420')

    # Create instances of the button
    quitButton = Button(430, 220, 100, 50, quitButtonImg)
    quitButtonGray = Button(430, 220, 100, 50, quitButtonGrayImg)
    startButton = Button(280, 220, 100, 50, startButtonImg)
    startButtonGray = Button(280, 220, 100, 50, startButtonGrayImg)
    gameRulesButton = Button(280, 326, 250, 50, buttonGameRulesImg)
    gameRulesButtonGray = Button(280, 326, 250, 50, buttonGameRulesGrayImg)
    buttonInstruction = Button(280, 273, 250, 50, buttonInstructionImg)
    buttonInstructionGray = Button(280, 273, 250, 50, buttonInstructionGrayImg)

    # Initialize game loop
    phase = "menu"
    loop = True

    while loop:
        # Check if user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((0, 0, 0))

        if phase == "menu":
            gameDisplay.blit(backGroundImg, (0, 0))

            # Display the created buttons
            gameDisplay.blit(quitButtonGray.img, (quitButton.x, quitButton.y))
            gameDisplay.blit(startButtonGray.img, (startButton.x, startButton.y))
            gameDisplay.blit(gameRulesButtonGray.img, (gameRulesButton.x, gameRulesButton.y))
            gameDisplay.blit(buttonInstructionGray.img, (buttonInstruction.x, buttonInstruction.y))

            # Check if mouse hovers over button
            if Button.buttonHover(quitButtonGray):
                gameDisplay.blit(quitButton.img, (quitButton.x, quitButton.y))

                # Check if the quit button has been pressed for exit functionality
                if Button.buttonHover(quitButton):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pygame.quit()
                        quit()

            elif Button.buttonHover(startButtonGray):
                gameDisplay.blit(startButton.img, (startButton.x, startButton.y))

                if Button.buttonHover(startButton):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        phase = "game"

            elif Button.buttonHover(gameRulesButtonGray):
                gameDisplay.blit(gameRulesButton.img, (gameRulesButton.x, gameRulesButton.y))

                if Button.buttonHover(gameRulesButton):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        phase = "rules"

            elif Button.buttonHover(buttonInstructionGray):
                gameDisplay.blit(buttonInstruction.img, (buttonInstruction.x, buttonInstruction.y))

                if Button.buttonHover(buttonInstruction):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        phase = "instructions"

        elif phase == "game":
            Definitief.Game.startGame()
        elif phase == "rules":
            Definitief.Rules.startRules()
        elif phase == "instructions":
            Definitief.Instructions.startInstructions()

        pygame.display.flip()

start_program()

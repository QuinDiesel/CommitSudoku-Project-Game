import pygame
import sys
import time

def program():
    width = 800
    height = 600
    size = (width, height)

    #Start Pygame
    pygame.init()

    #Scherm Resolutie
    screen = pygame.display.set_mode(size)

    background_color = (255, 255, 255)
    screen.fill(background_color)
    pygame.display.set_caption('Menu')

    # Flip the screen
    pygame.display.flip()

    
    pygame.mixer.init()
    pygame.mixer.music.load('filename.wav')
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT and pygame.K_F4:
                    sys.exit()





#Start Program
program()


















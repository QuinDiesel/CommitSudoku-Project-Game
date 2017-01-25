import pygame

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

def zandloper():
    pygame.init()
    size = [800, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("zandloper(timer)")
    clock = pygame.time.Clock()
    image = pygame.image.load("zandloper8bit2.png").convert()
    img_rect = image.get_rect()
    angle = 0
    #----#
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
        # hoek
        angle += 1
        if angle >= 360:
            angle = 0
        rot_image = pygame.transform.rotate(image, angle)
        rot_im_rect = rot_image.get_rect()
        rot_im_rect.center = img_rect.center
        screen.fill(BLACK)
        screen.blit(rot_image, rot_im_rect)
        pygame.display.flip()
        #rotate speed
        clock.tick(20)

pygame.quit()
zandloper()
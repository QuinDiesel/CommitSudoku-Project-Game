import pygame
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('timer', 30)
event = pygame.USEREVENT
while True:
    for e in pygame.event.get():
        if e.type == pygame.event:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'time\s up'
        if e.type == pygame.QUIT:
            quit()
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (255, 255, 255)), (700, 30))
        pygame.display.flip()
        clock.tick(60)
        continue
    quit()
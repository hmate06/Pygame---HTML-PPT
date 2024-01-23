import pygame # pygame importalasa


pygame.init()
screen = pygame.display.set_mode((800, 600)) # kepernyo/jatekter merete
pygame.display.set_caption("Alapok") # megjeleno ablak neeve


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
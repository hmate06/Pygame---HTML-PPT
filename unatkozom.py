import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("TYUKNIGATYUKNIGATYUKNIGATYUKNIGATYUKNIGATYUKNIGA")

rc_1 = random.randint(0, 255)
rc_2 = random.randint(0, 255)
rc_3 = random.randint(0, 255)
ran_c = (rc_1, rc_2, rc_3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed():
                rc_1 = random.randint(0, 255)
                rc_2 = random.randint(0, 255)
                rc_3 = random.randint(0, 255)
                ran_c = (rc_1, rc_2, rc_3)
    screen.fill(ran_c)
    pygame.display.update()

pygame.quit()
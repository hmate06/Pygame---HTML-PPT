import pygame

PIROS = (255, 0, 0) # --- hatter szinezese const-val
KEK = (0,0,255)
SZIN = (54, 183, 93)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alapok")
hatter_szine = SZIN # --- hatter szinezese const-val


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # hatter szinenek megvaltoztatasa billentyuk lenyomasaval
            if event.key == pygame.K_r: # "r" betu lenyomasa
                hatter_szine = PIROS# piros lesz a hatter
            elif event.key == pygame.K_b: 
                hatter_szine = KEK

    # screen.fill(hatter_szine) --- hatter szinezese const-val
    screen.fill(hatter_szine)
    # screen.fill((R, G, B)) --- hatter szinezese RGB koddal
    pygame.display.update()

pygame.quit()
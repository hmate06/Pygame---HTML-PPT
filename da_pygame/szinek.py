import pygame

# háttérszínhez a constansok meghatározása
PIROS = (255, 0, 0)
KEK = (0,0,255)
SZIN = (54, 183, 93)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Színek")

# hatter_szine = SZIN --- háttér színezése constanssal

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Billentyű lenyomásra háttérszín megváltozása
        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_r: # "r" billentyű lenyomása - piros lesz a háttér
                hatter_szine = PIROS

            elif event.key == pygame.K_t: # "t" billentyű lenyomása - kék lesz a háttér
                hatter_szine = KEK

    # --- háttér színezése constanssal
    screen.fill(SZIN)
    # screen.fill((R, G, B)) --- háttér színezése RGB kóddal

    pygame.display.update()

pygame.quit()

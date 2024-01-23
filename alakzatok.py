import pygame

B = (0,0,0)
W = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alapok")
bgc = B
# pygame.draw.kor(hova rajzolja, szin, (kozeppont_koordinatai), sugar) --- kor kotelezo parameterei

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(bgc) # tipp: a hatter szinezese az alakzat rajzolasa elott legyen kulomben takrani fogja
    pygame.draw.circle(screen, W, (400, 300), 100) # kor rajzolsa
    pygame.draw.rect(screen, (255, 0, 0), (30, 30, 150, 75)) # 4szog: (hovarajzolja, szin, (pozicio es meret))
    
    """
    egyeb alakzatok:
    elipszis: ellipse(hova, szin, (pozicio es meret))
    sokszog: polygon(hova, szin, [(csucsok)(koordinatai)])
    """
    
    pygame.display.update()

pygame.quit()
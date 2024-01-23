import pygame

PIROS = (255, 0, 0)
KEK = (0, 0, 255)
SZIN = (54, 183, 93)
FEHER = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alapok")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # A háttér színezése az alakzat rajzolása előtt legyen különben takarni fogja
    screen.fill(SZIN)

    # kör rajzolása
    pygame.draw.circle(screen, FEHER, (400, 300), 100)
                    # (felület, szín, (középpontjának_koordinátái), kör_sugara) - kör kötelező paraméterei

    # négyszögek rajzolása
    pygame.draw.rect(screen, (255, 0, 0), (30, 30, 150, 75))
                    # (felület, szín, (pozíciója és mérete)) - négyzet kötelező paraméterei

    # egyéb alakzatok:
    # - elipszis: ellipse(felület, szín, (pozíciója és mérete))
    # pygame.draw.ellipse(screen, KEK, (50, 50, 200, 75))

    # - sokszög: polygon(felület, szín, [(csúcsok_koordinátája), (), ()])
    # pygame.draw.polygon(screen, KEK, [(120, 90), (120,200), (200, 90)])

    pygame.display.update()

pygame.quit()

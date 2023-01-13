import pygame

pygame.init()
pygame.font.init()

size = (1000, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
screen.fill("#9f4100")

font = pygame.font.Font("PressStart2P.ttf", 30)

score_point_player1 = font.render("0", True, (0, 255, 0))
score_point_player1_rect = score_point_player1.get_rect()
score_point_player1_rect.center = (350, 30)

score_point_player2 = font.render("0", True, (0, 0, 255))
score_point_player2_rect = score_point_player2.get_rect()
score_point_player2_rect.center = (650, 30)

player1 = pygame.image.load("player1.png")
player1 = pygame.transform.scale(player1, (50, 50))
player2 = pygame.image.load("player2.png")
player2 = pygame.transform.scale(player2, (50, 50))
player2 = pygame.transform.rotate(player2, 180)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.polygon(screen, "#c29f2e",
                        [(110, 300), (160, 300), (160, 500), (110, 500), (110, 480), (140, 480), (140, 320),
                         (110, 320)])
    pygame.draw.polygon(screen, "#c29f2e",
                        [(890, 300), (840, 300), (840, 500), (890, 500), (890, 480), (860, 480), (860, 320),
                         (890, 320)])

    pygame.draw.rect(screen, "#c29f2e", (480, 155, 40, 100))
    pygame.draw.rect(screen, "#c29f2e", (480, 545, 40, 100))
    pygame.draw.rect(screen, "#c29f2e", (255, 380, 100, 40))
    pygame.draw.rect(screen, "#c29f2e", (645, 380, 100, 40))

    pygame.draw.rect(screen, "#c29f2e", (0, 50, 1000, 700), 25)
    screen.blit(player1, (50, 380))
    screen.blit(player2, (910, 380))
    screen.blit(score_point_player1, score_point_player1_rect)
    screen.blit(score_point_player2, score_point_player2_rect)
    pygame.display.flip()

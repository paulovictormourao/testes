import pygame
from pygame.locals import *
from sys import exit
import math


def draw_walls(space1, space2, aux1, space3, space4, space5, aux2):

    # Vertical central Rects
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space1, score_h + border, rects_w1, rects_h1))
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space1, (sc_height - border - rects_h1), rects_w1, rects_h1))

    # Four "Ls"
    # Up L
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space2, field_middle_x - 5*border, rects_h1, rects_w1))
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space2 + aux1, field_middle_x - 4 * border, rects_w2, rects_w1))
    # Below L
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space2, field_middle_x + 4*border, rects_h1, rects_w1))
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space2 + aux1, field_middle_x + 3 * border, rects_w2, rects_w1))

    # 2 Rects in the side
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space3 - 2.5 * aux2, score_h + 4 * rects_w1, rects_h1, rects_w1))
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space3 - 2.5 * aux2, sc_height - 4 * rects_w1 - border, rects_h1, rects_w1))

    # Big side rect
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space4 - 2.5 * aux2, field_middle_x - rects_w1, rects_h1, 2 * rects_w1))

    # " ] " Symbol
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space3 - aux2, field_middle_x - symbol_h / 2, rects_w1, symbol_h))
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space5 - aux2, field_middle_x - symbol_h / 2, rects_w1, rects_w1))
    pygame.draw.rect(screen, yellow, (sc_width / 2 + space5 - aux2, field_middle_x + symbol_h / 2 - rects_w1, rects_w1, rects_w1))


pygame.init()
pygame.font.init()

# Colors
red = (120, 0, 0)
yellow = (207, 181, 59)

# Screen
sc_width = 1180
sc_height = 760
screen = pygame.display.set_mode((sc_width, sc_height))
border = 26
score_h = 120
screen.fill(red)
pygame.display.set_caption("Breakout Game")
font = pygame.font.Font("PressStart2P.ttf", 60)

# Dimensions
rects_h1 = 2.5 * border
rects_w1 = border
rects_w2 = border * 0.9
field_middle_x = (sc_height + score_h) / 2
symbol_h = 3 * rects_h1

# Score (player 1)
score_point_player1 = font.render("0", True, (0, 255, 0))
score_point_player1_rect = score_point_player1.get_rect()
score_point_player1_rect.center = (sc_width/4, 50)
# Score (player 2)
score_point_player2 = font.render("0", True, (0, 0, 255))
score_point_player2_rect = score_point_player2.get_rect()
score_point_player2_rect.center = (3 * sc_width/4, 50)

# Load images
player1 = pygame.image.load("player1.png")
player1 = pygame.transform.scale(player1, (50, 50))
player2 = pygame.image.load("player2.png")
player2 = pygame.transform.scale(player2, (50, 50))
player2 = pygame.transform.rotate(player2, 180)

xp1 = 50
yp1 = field_middle_x - 25
xp2 = sc_width - 100
yp2 = field_middle_x - 25
radius = 25*(2**0.5)
ang = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_UP]:
        xp1 += math.sin(math.radians(ang+90))
        yp1 += math.cos(math.radians(ang+90))

    elif pygame.key.get_pressed()[K_LEFT]:
        ang += 1

    elif pygame.key.get_pressed()[K_RIGHT]:
        ang += -1
    pygame.key.get_pressed()[K_LEFT]

    player1 = pygame.image.load("player1.png")
    player1 = pygame.transform.scale(player1, (50, 50))
    player1 = pygame.transform.rotate(player1, ang)
    player2 = pygame.image.load("player2.png")
    player2 = pygame.transform.scale(player2, (50, 50))
    screen.blit(player1, (xp1, yp1))
    screen.blit(player2, (xp2, yp2))
    screen.blit(score_point_player1, score_point_player1_rect)
    screen.blit(score_point_player2, score_point_player2_rect)

    # Draw
    # Border horizontal
    pygame.draw.rect(screen, yellow, (0, score_h, sc_width, border))
    pygame.draw.rect(screen, yellow, (0, sc_height - border, sc_width, border))
    # Border vertical
    pygame.draw.rect(screen, yellow, (0, score_h, border, sc_height))
    pygame.draw.rect(screen, yellow, (sc_width - border, score_h, border, sc_height))

    # Left
    draw_walls(-border, -4*border - rects_h1, 0, -15*border, -13*border, -16*border, 0)

    # Right
    draw_walls(0, 4*border, rects_h1 - rects_w2 + 1, 15 * border, 13 * border, 16 * border, rects_w1)

    pygame.display.flip()
    pygame.display.update()
    screen.fill(red)

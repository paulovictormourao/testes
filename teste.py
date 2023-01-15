import pygame
import math
from draw_screen import draw_object

pygame.init()
pygame.font.init()

# Screen
sc_width = 1000
sc_height = 750
screen = pygame.display.set_mode((sc_width, sc_height))
border = 25
screen.fill("#9f4100")
pygame.display.set_caption("Breakout Game")
font = pygame.font.Font("PressStart2P.ttf", 40)

# Score (player 1)
score_point_player1 = font.render("0", True, (0, 255, 0))
score_point_player1_rect = score_point_player1.get_rect()
score_point_player1_rect.center = (sc_width / 4, 25)
# Score (player 2)
score_point_player2 = font.render("0", True, (0, 0, 255))
score_point_player2_rect = score_point_player2.get_rect()
score_point_player2_rect.center = (3 * sc_width / 4, 25)

# Load images
player1 = pygame.sprite.Sprite()
player2 = pygame.sprite.Sprite()


def load_images(sprite, ang, xp, yp, image):
    sprite.image = pygame.image.load(image)
    sprite.image = pygame.transform.scale(sprite.image, (50, 50))
    sprite.image = pygame.transform.rotate(sprite.image, ang)
    cor_x = sprite.image.get_rect(center=(xp + 25, yp + 25))
    sprite.rect = cor_x
    return cor_x


xp1 = 50
yp1 = 380
shoot_p1_x = 0
shoot_p1_y = 0
shoot_p1 = pygame.draw.rect(screen, "#c29f2e", (xp1 + 50 + shoot_p1_x, yp1 + 25 + shoot_p1_y, 5, 5))
shoot_p1_angle = 0
fire = 10

xp2 = sc_width - 100
yp2 = 380
radius = 25 * (2 ** 0.5)
shoot_p2_x = 0
shoot_p2_y = 0
shoot_p2 = pygame.draw.rect(screen, "#c29f2e", (xp2 + 50 + shoot_p2_x, yp1 + 25 + shoot_p2_y, 5, 5))
shoot_p2_angle = 0

ang_left = 0
ang_right = 0

clock = pygame.time.Clock()
per_1 = False
per_2 = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    blue = (0, 0, 255)

    player1_cor = load_images(player1, ang_left, xp1, yp1, "player1.png")
    player2_cor = load_images(player2, ang_right, xp2, yp2, "player2.png")
    player2.image = pygame.transform.rotate(player2.image, 180)

    # collision player 1 with objects
    collision_1 = (
        25 + xp1 + 25 * math.sin(math.radians(ang_left + 90)), yp1 + 25 * math.cos(math.radians(ang_left + 90)), 5,
        50)
    if draw_object(screen, collision_1):
        per_1 = True
    else:
        per_1 = False

    # collision player 2 with objects
    collision_2 = (
        25 + xp2 - 25 * math.sin(math.radians(ang_right + 90)), yp2 - 25 * math.cos(math.radians(ang_right + 90)), 5,
        50)
    if draw_object(screen, collision_2):
        per_2 = True
    else:
        per_2 = False

    # Controls
    if keys[pygame.K_w] and per_1:
        xp1 += math.sin(math.radians(ang_left + 90))
        yp1 += math.cos(math.radians(ang_left + 90))

    elif keys[pygame.K_a]:
        ang_left += 1

    elif keys[pygame.K_d]:
        ang_left += -1

    elif keys[pygame.K_q]:
        shoot_p1_x = xp1
        shoot_p1_y = yp1
        shoot_p1_angle = ang_left

    shoot_p1 = pygame.draw.rect(screen, "#c29f2e", (shoot_p1_x + 25, 21 + shoot_p1_y, 8, 8))
    shoot_p1_x += math.sin(math.radians(shoot_p1_angle + 90))
    shoot_p1_y += math.cos(math.radians(shoot_p1_angle + 90))

    if keys[pygame.K_UP] and per_2:
        xp2 += math.sin(math.radians(ang_right - 90))
        yp2 += math.cos(math.radians(ang_right - 90))

    elif keys[pygame.K_LEFT]:
        ang_right += 1

    elif keys[pygame.K_RIGHT]:
        ang_right += -1

    elif keys[pygame.K_SEMICOLON]:
        shoot_p2_x = xp2
        shoot_p2_y = yp2
        shoot_p2_angle = ang_right
        fire /= 10

    shoot_p2 = pygame.draw.rect(screen, "#c29f2e", (shoot_p2_x + 25, shoot_p2_y + 21, 8, 8))
    shoot_p2_x += math.sin(math.radians(shoot_p2_angle - 90))
    shoot_p2_y += math.cos(math.radians(shoot_p2_angle - 90))

    screen.blit(player1.image, player1_cor)
    screen.blit(player2.image, player2_cor)

    screen.blit(score_point_player1, score_point_player1_rect)
    screen.blit(score_point_player2, score_point_player2_rect)

    draw_object(screen, player1.rect)

    pygame.display.flip()
    screen.fill("#9f4100")
    clock.tick(80)

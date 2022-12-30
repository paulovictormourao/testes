import pygame

pygame.init()
pygame.font.init()

# Colors
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 165, 0)

SCORE = 0
LIVE = 1

size = (587, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# Draw Edge
font = pygame.font.Font('PressStart2P.ttf', 30)
score_point = font.render('000       000', True, COLOR_WHITE)
score_point_rect = score_point.get_rect()
score_point_rect.center = (300, 130)

score_live = font.render("1        1", True, COLOR_WHITE)
score_live_rect = score_live.get_rect()
score_live_rect.center = (230, 91)

bounce_sound_effect = pygame.mixer.Sound('bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('258020_stack_arcade-bleep-sound.wav')

brick_list = [(x, y) for y in range(160, 259, 14) for x in range(541, 0, -41)]

# draw paddle
weight = 30
height = 10
paddle_x = 275
paddle_y = 700
paddle = pygame.draw.rect(screen, COLOR_BLUE, pygame.Rect(paddle_x, paddle_y, weight, height))

# draw ball
ball_dx = 3
ball_dy = 3
ball_x = 279
ball_y = 467
ball = pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(ball_x, ball_y, 11, 4))


# collision brick
def collision_brick(brick_wall):
    for brick in brick_wall:
        position_x = brick[0]
        position_y = brick[1]

        global score_point
        global SCORE
        global ball_dy
        global start

        if not start:
            return True

        if position_y < ball_y < position_y + 10 and position_x < ball_x + 12 < position_x + 42:
            ball_dy *= -1
            if position_y == 160 or position_y == 174:
                SCORE += 7
                score_point = font.render("000" + '       ' + str(SCORE), True, COLOR_WHITE, COLOR_BLACK)
            elif position_y == 188 or position_y == 202:
                SCORE += 5
                score_point = font.render("000" + '       ' + str(SCORE), True, COLOR_WHITE, COLOR_BLACK)
            elif position_y == 216 or position_y == 230:
                SCORE += 3
                score_point = font.render("000" + '       ' + str(SCORE), True, COLOR_WHITE, COLOR_BLACK)
            elif position_y == 244 or position_y == 258:
                SCORE += 1
                score_point = font.render("000" + '       ' + str(SCORE), True, COLOR_WHITE, COLOR_BLACK)
            if LIVE < 4:
                brick_wall.remove(brick)
                scoring_sound_effect.play()
            return True


def draw_brick(brick_wall):
    paint = COLOR_RED
    for cor in brick_wall:
        if cor[1] == 188 or cor[1] == 202:
            paint = COLOR_ORANGE
        elif cor[1] == 216 or cor[1] == 230:
            paint = COLOR_GREEN
        elif cor[1] == 244 or cor[1] == 258:
            paint = COLOR_YELLOW
        pygame.draw.rect(screen, paint, pygame.Rect(cor[0], cor[1], 37, 10))


count = 0
start = True
game_clock = pygame.time.Clock()
game_loop = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    else:
        paddle_x -= 0

    if keys[pygame.K_RIGHT] and paddle_x < 557:
        paddle_x += 5
    else:
        paddle_x += 0

    # ball collision with right wall
    if ball_x > 565:
        bounce_sound_effect.play()
        ball_dx *= -1
    # ball collision with left wall
    elif ball_x < 20:
        bounce_sound_effect.play()
        ball_dx *= -1
    # ball collision with upper wall
    if ball_y < 80:
        bounce_sound_effect.play()
        ball_dy *= -1

    # ball collision with  paddle
    if 702 >= ball_y >= 700:
        if paddle_y < ball_y + 4:
            if paddle_x < ball_x + 11 < paddle_x + weight + 11:
                bounce_sound_effect.play()
                ball_dy *= -1
                count += 1

    # ball collision with lower wall
    if ball_y > 740:
        ball_x = 279
        ball_y = 467
        LIVE += 1
        score_live = font.render(str(LIVE) + '       ' + "1", True, COLOR_WHITE, COLOR_BLACK)
        count = 0
        ball_dx = 3
        ball_dy = 3
        continue

    screen.fill(COLOR_BLACK)

    # ball collision with brick
    if collision_brick(brick_list):
        if 268 > ball_y > 160:
            start = False
        else:
            start = True

    # draw brick
    draw_brick(brick_list)

    if ball_y < 160:
        weight = 15

    if 5 == count:
        count = 0
        if ball_dx > 0:
            ball_dx += 1
        else:
            ball_dx -= 1
        if ball_dy > 0:
            ball_dy += 1
        else:
            ball_dy -= 1

    if 13 == count:
        count = 0
        if ball_dx > 0:
            ball_dx += 1
        else:
            ball_dx -= 1
        if ball_dy > 0:
            ball_dy += 1
        else:
            ball_dy -= 1

    if LIVE == 4:
        paddle_x = 0
        weight = 600
        if keys[pygame.K_KP_ENTER]:
            SCORE = 0
            LIVE = 1
            ball_x = 279
            ball_y = 467
            ball_dx = 3
            ball_dy = 3
            paddle_x = 275
            weight = 30
            score_live = font.render(str(LIVE) + '       ' + "1", True, COLOR_WHITE, COLOR_BLACK)
            brick_list = [(x, y) for y in range(160, 259, 14) for x in range(541, 0, -41)]
            continue

    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    line_ball_left = pygame.draw.line(screen, (0, 150, 200), (4, 690), (4, 720), width=10)
    line_ball_right = pygame.draw.line(screen, (0, 150, 200), (582, 690), (582, 720), width=10)

    line_left1 = pygame.draw.line(screen, COLOR_WHITE, (4, 0), (4, 159), width=10)
    line_left2 = pygame.draw.line(screen, COLOR_WHITE, (4, 267), (4, 690), width=10)
    line_left3 = pygame.draw.line(screen, COLOR_WHITE, (4, 720), (4, 800), width=10)
    red_left = pygame.draw.line(screen, COLOR_RED, (4, 160), (4, 188), width=10)
    orange_left = pygame.draw.line(screen, COLOR_ORANGE, (4, 188), (4, 216), width=10)
    green_left = pygame.draw.line(screen, COLOR_GREEN, (4, 216), (4, 244), width=10)
    yellow_left = pygame.draw.line(screen, COLOR_YELLOW, (4, 244), (4, 267), width=10)

    line_right1 = pygame.draw.line(screen, COLOR_WHITE, (582, 0), (582, 159), width=10)
    line_right2 = pygame.draw.line(screen, COLOR_WHITE, (582, 267), (582, 690), width=10)
    line_right3 = pygame.draw.line(screen, COLOR_WHITE, (582, 720), (582, 800), width=10)
    red_right = pygame.draw.line(screen, COLOR_RED, (582, 160), (582, 188), width=10)
    orange_right = pygame.draw.line(screen, COLOR_ORANGE, (582, 188), (582, 216), width=10)
    green_right = pygame.draw.line(screen, COLOR_GREEN, (582, 216), (582, 244), width=10)
    yellow_right = pygame.draw.line(screen, COLOR_YELLOW, (582, 244), (582, 267), width=10)

    line_upper = pygame.draw.line(screen, COLOR_WHITE, (0, 60), (585, 60), width=30)

    pygame.draw.rect(screen, COLOR_WHITE, (ball_x, ball_y, 11, 4))
    pygame.draw.rect(screen, COLOR_BLUE, (paddle_x, paddle_y, weight, height))
    screen.blit(score_point, score_point_rect)
    screen.blit(score_live, score_live_rect)

    pygame.display.flip()
    game_clock.tick(70)

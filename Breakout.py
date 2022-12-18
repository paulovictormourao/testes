import turtle

# draw screen
screen = turtle.Screen()
screen.title("Blackout")
screen.bgcolor("black")
screen.setup(width=400, height=600)
screen.tracer(0)
# positions of each brick from wall
position_brick = []
# draw window
window = turtle.Turtle()
window.speed(0)
window.shape("square")
window.width(5)
window.color("white")
window.penup()
window.setpos(-295, 490)
window.pendown()
window.rt(90)
window.fd(1180)
window.lt(90)
window.color("blue")
window.goto(340, -490)
window.color("white")
window.lt(90)
window.fd(1180)
window.penup()
window.hideturtle()


# draw paddle
def draw_paddle(paddle, y, x, dye):
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(dye)
    paddle.shapesize(stretch_wid=0.4, stretch_len=2)
    paddle.penup()
    paddle.goto(x, y)


# draw paddle
paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -300, 0,'blue')

# draw bricks
bricks = turtle.Turtle()
color_list = ["red", "orange", "green", "yellow"]


def create_bricks(dye):
    bricks.penup()
    bricks_copy = bricks.clone()
    bricks_copy.shape("square")
    bricks_copy.shapesize(stretch_wid=0.4, stretch_len=2)
    bricks_copy.color(dye)
    bricks_copy.penup()
    bricks_copy.goto(j, i)
    position_brick.append(bricks_copy.position())
    brick_lane.append(bricks_copy)


brick_lane = []
y_cor = [200, 188, 176, 164, 152, 140, 128, 116]
x_cor = [315, 270, 225, 180, 135, 90, 45, 0, -45, -90, -135, -180, -225, -270]

for i in y_cor:
    color = ""
    if i == 200 or i == 188:
        color = color_list[0]
    elif i == 176 or i == 164:
        color = color_list[1]
    elif i == 152 or i == 140:
        color = color_list[2]
    elif i == 128 or i == 116:
        color = color_list[3]
    for j in x_cor:
        create_bricks(color)


print(position_brick)
print(len(position_brick))
print(brick_lane)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(0.5)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -1
ball.dy = -1

# score
score = 0
score_death = 1


def score_point(head , scoreboard):
    head.clear()
    head.write("{}".format(scoreboard), align="center", font=("Press Start 2P", 30 , "bold"))
    if head == hud_death :
        ball.goto(0, 0)
        ball.dx  *=  -1
    else:
        ball.dx  *=  1


# head-up display
def head(hud, x, y, format):
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(x, y)
    hud.write(format , align="center", font=("Press Start 2P", 45,"bold"))


hud_left = turtle.Turtle()
head(hud_left, -160, 250, "000")

hud_death = turtle.Turtle()
head(hud_death,  140, 350, "1")

hud_ghost = turtle.Turtle()
head(hud_death, -260 , 350, "1")

hud_right = turtle.Turtle()
head(hud_right, 240, 250, "000")


def paddle_right(paddle):
    x = paddle.xcor()
    if x < 315:
        x += 25
    else:
        x = 315
    return paddle.setx(x)


def paddle_left(paddle):
    x = paddle.xcor()
    if x > -270:
        x -= 25
    else:
        x = -270
    return paddle.setx(x)


# keyboard
screen.listen()
screen.onkeypress(lambda: paddle_right(paddle_1), "Right")
screen.onkeypress(lambda: paddle_left(paddle_1), "Left")

while True:
    screen.update()

    # ball movement
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # collision with the right wall
    if ball.xcor() > 335:
        ball.setx(335)
        ball.dx *= -1

    # collision with left wall
    if ball.xcor() < -280:
        ball.setx(-280)
        ball.dx *= -1

    # collision with lower wall
    if ball.ycor() < -370:
        score_death += 1
        score_point(hud_death, score_death)


    def brick_hit():
        ball.sety(position_y - 10)
        ball.dy *= -1
        brick.goto(1000, 1000)
        brick_lane.remove(brick)
        return

    # collision with the brick
    for brick in brick_lane:
        position_x = brick.xcor()
        position_y = brick.ycor()
        if ball.ycor() == position_y and position_x + 26 > ball.xcor() > position_x - 26:
            brick_hit()
            if position_y == 200 or position_y == 188:
                score += 7
                score_point(hud_left,score)
                paddle_1.shapesize(stretch_wid=0.4, stretch_len=1)
            elif position_y == 176 or position_y == 164:
                score += 5
                score_point(hud_left, score)
                paddle_1.shapesize(stretch_wid=0.4, stretch_len=1.5)
            elif position_y == 152 or position_y == 140:
                score += 3
                score_point(hud_left, score)
            elif position_y == 128 or position_y == 116:
                score += 1
                score_point(hud_left, score)

    # collision with the paddle
    if -242 < ball.ycor() < -258 and paddle_1.xcor() + 10 > ball.xcor() > paddle_1.xcor() - 10:
        ball.sety(-258)
        ball.dy *= -1
from turtle import Screen
import paddle
import score
import time
from ball import Ball
screen = Screen()
screen.tracer(0)
s = score.Score()
ball = Ball()
t = paddle.Paddle()
s.update()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong")


screen.listen()
screen.onkey(t.up1, "p")
screen.onkey(t.down1, "l")
screen.onkey(t.up2, "q")
screen.onkey(t.down2, "a")

game = True
while game:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()
    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    # Detect Collision with Paddle
    if ball.distance(t.p1) < 50 and ball.xcor() > 340 or ball.distance(t.p2) < 50 and ball.xcor() < -340:
        ball.bouncex()
    # If Ball passes past the Paddle
    if ball.xcor() > 410:
        ball.initial()
        s.pointl()
    if ball.xcor() < -410:
        ball.initial()
        s.pointr()


screen.exitonclick()


from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x = 10
        self.y = 10
        self.velocity = 0.1

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bouncey(self):
        self.y *= -1

    def bouncex(self):
        self.x *= -1
        self.velocity *= 0.9

    def initial(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.bouncex()

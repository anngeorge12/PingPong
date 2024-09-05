from turtle import Turtle


class Paddle:
    def __init__(self):
        self.p1 = self.creater(370)
        self.p2 = self.creater(-370)

    def creater(self, x):
        p = Turtle()
        p.shape("square")
        p.color("green")
        p.penup()
        p.goto(x, 0)
        p.setheading(90)
        p.shapesize(1, 5)
        return p

    def up1(self):
        self.p1.forward(50)

    def down1(self):
        self.p1.backward(50)

    def up2(self):
        self.p2.forward(50)

    def down2(self):
        self.p2.backward(50)



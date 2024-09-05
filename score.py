from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lsc = 0
        self.rsc = 0
        self.color("white")
        self.penup()
        self.ht()

    def update(self):
        self.clear()
        self.goto(0, 200)
        self.write(self.lsc, move=False, align="right", font=("Courier", 80, "normal"))
        self.write(self.rsc, move=False, align="left", font=("Courier", 80, "normal"))

    def pointl(self):
        self.lsc += 1
        self.update()

    def pointr(self):
        self.rsc += 1
        self.update()


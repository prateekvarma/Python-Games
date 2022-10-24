from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10  # simple variable saying 10 px move to the x-axis
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # this reverses the direction

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)  # place ball at the center
        self.bounce_x()  # change ball's direction to the opposite player

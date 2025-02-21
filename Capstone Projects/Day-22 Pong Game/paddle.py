from turtle import Turtle
class Paddle:
    def __init__(self,x,y,screen):
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.color('LightSteelBlue4')
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x,y)
        self.move_speed = 20  ######
        self.moving_up = False  ######
        self.moving_down = False  ######
        self.screen = screen  ######

    def go_up(self):
        if not self.moving_up:
            self.moving_up = True
            self.move_up()

    def move_up(self):
        if self.moving_up:
            new_y = self.paddle.ycor() + self.move_speed
            self.paddle.goto(self.paddle.xcor(), new_y)
            self.screen.ontimer(self.move_up, 50)

    def stop_up(self):
        self.moving_up = False

    def go_down(self):
        if not self.moving_down:
            self.moving_down = True
            self.move_down()

    def move_down(self):
        if self.moving_down:
            new_y = self.paddle.ycor() - self.move_speed
            self.paddle.goto(self.paddle.xcor(), new_y)
            self.screen.ontimer(self.move_down, 50)

    def stop_down(self):
        self.moving_down = False

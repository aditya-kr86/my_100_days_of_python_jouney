from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color('Red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(x=random_x,y=random_x)
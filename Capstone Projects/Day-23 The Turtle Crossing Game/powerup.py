from turtle import Turtle
import random

class PowerUp(Turtle):
    def __init__(self):
        """Initialize the power-up."""
        super().__init__()
        self.shape('circle')
        self.color('chartreuse')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        """Move the power-up to a random location."""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 250)
        self.goto(random_x, random_y)

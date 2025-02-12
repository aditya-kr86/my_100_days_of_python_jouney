from turtle import Turtle
import random

class Obstacle(Turtle):
    def __init__(self):
        """Initialize the obstacle."""
        super().__init__()
        self.shape('square')
        self.color('gray50')
        self.shapesize(stretch_wid=.5, stretch_len=1)
        self.penup()
        self.refresh()

    def refresh(self):
        """Move the obstacle to a random location."""
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

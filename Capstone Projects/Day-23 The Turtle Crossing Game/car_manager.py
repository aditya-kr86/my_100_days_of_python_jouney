from turtle import Turtle
import random

X_POSITION = 280
COLORS = ['Red', 'goldenrod', 'Green', 'SeaGreen1', 'Blue']

class Car(Turtle):
    def __init__(self):
        """Initialize the car."""
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=.5, stretch_len=1)
        self.penup()
        self.refresh()
    
    def refresh(self):
        """Refresh the car's position and color."""
        self.color(random.choice(COLORS))
        self.goto(X_POSITION, (random.randint(-23, 27)) * 10)

    def move(self, speed):
        """Move the car left by the given speed."""
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())

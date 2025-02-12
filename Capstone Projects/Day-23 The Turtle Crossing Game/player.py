from turtle import Turtle
import time
PLAYER_COLOR = ['Black', 'Blue', 'Green', 'Red', 'Purple','Black', 'Blue', 'Green', 'Red', 'Purple','Black', 'Blue', 'Green', 'Red', 'Purple']

class Timmy(Turtle):
    def __init__(self):
        """Initialize the player."""
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.color_no = 0
        self.color(PLAYER_COLOR[self.color_no])
        self.start_pos = (0, -280)
        self.penup()
        self.goto(self.start_pos)
        self.move_speed = 10
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False

    def reset_position(self):
        """Reset the player's position to the starting point."""
        self.goto(self.start_pos)

    # To move Player Up
    def go_up(self):
        """Start moving the player up."""
        if not self.moving_up:
            self.moving_up = True
            self.move_up()

    def move_up(self):
        """Move the player up by a fixed amount."""
        if self.moving_up:
            new_y = self.ycor() + self.move_speed
            self.goto(self.xcor(), new_y)
            self.screen.ontimer(self.move_up, 50)

    def stop_up(self):
        """Stop moving the player up."""
        self.moving_up = False

    # To move Player Right
    def go_right(self):
        """Start moving the player right."""
        if not self.moving_right:
            self.moving_right = True
            self.move_right()

    def move_right(self):
        """Move the player Right by a fixed amount."""
        if self.moving_right:
            new_x = self.xcor() + self.move_speed
            self.goto(new_x, self.ycor())
            self.screen.ontimer(self.move_right, 50)

    def stop_right(self):
        """Stop moving the player Right."""
        self.moving_right = False

    # To move Player Left
    def go_left(self):
        """Start moving the player up."""
        if not self.moving_left:
            self.moving_left = True
            self.move_left()

    def move_left(self):
        """Move the player left by a fixed amount."""
        if self.moving_left:
            new_x = self.xcor() - self.move_speed
            self.goto(new_x, self.ycor())
            self.screen.ontimer(self.move_left, 50)

    def stop_left(self):
        """Stop moving the player left."""
        self.moving_left = False

    # def level_up(self):
    #     """Animate the player (example of simple color change)."""
    #     self.color_no += 1
    #     self.color(PLAYER_COLOR[self.color_no])

    def animate(self):
        """Animate the player (example of simple color change)."""
        colors = ['Black', 'Blue', 'Green', 'Red', 'Purple']
        for color in colors:
            self.color(color)
            time.sleep(0.1)

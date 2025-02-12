from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Black", 18, "normal")

class Level(Turtle):
    def __init__(self, x, y):
        """Initialize the scoreboard."""
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.level = 1
        self.color("Black")
        self.update_board()

    def update_board(self):
        """Update the scoreboard with the current level."""
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def update_level(self):
        """Increase the level and update the scoreboard."""
        self.level += 1
        self.update_board()

    def game_over(self):
        """Display the game over message."""
        self.goto(-50, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=("Courier", 35, "normal"))

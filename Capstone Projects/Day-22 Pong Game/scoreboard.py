from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Black",18,"normal")

class Scoreboard(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.hideturtle()
        self.score = 0
        self.color("Black")
        self.update_board()

    def update_board(self):
        self.write(arg=f"Score : {self.score}",move= False, align=ALIGNMENT ,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER ! ", align=ALIGNMENT ,font=("Courier",35,"normal"))
        
    def update_score(self):
        self.score += 1   
        self.clear()     
        self.update_board()

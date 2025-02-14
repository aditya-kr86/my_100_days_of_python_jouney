from turtle import Turtle
import os

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("highest_score.txt",mode= "r") as file:
    score_history = int(file.read())

ALIGNMENT = "center"
FONT = ("Courier",18,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        

        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score = 0
        self.high_score = score_history
        self.color("white")
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}" ,move= False, align=ALIGNMENT ,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt",mode= "w") as file:
                file.write(str(self.high_score))
                file.close()
        self.score = 0
        self.update_board()
        
    def update_score(self):
        self.score += 1   
        self.clear()     
        self.update_board()

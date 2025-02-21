from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('AntiqueWhite1')
screen.setup(width=800,height=600)
screen.title("Pong - Aditya Kumar")
screen.tracer(0)

r_paddle = Paddle(380,0,screen)
l_paddle = Paddle(-380,0,screen)
ball = Ball()
l_scoreboard = Scoreboard(-70,260)
r_scoreboard = Scoreboard(70,260)


screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeyrelease(r_paddle.stop_up,"Up")

screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeyrelease(r_paddle.stop_down,"Down")

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeyrelease(l_paddle.stop_up,"w")

screen.onkeypress(l_paddle.go_down,"s")
screen.onkeyrelease(l_paddle.stop_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.15)
    screen.update()
    ball.move()
    
    #### Detect Collision with Wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #### Detect Collision with right Paddle:
    if ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 370:
        ball.bounce_x() 
        r_scoreboard.update_score()
    elif  ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -370:
        ball.bounce_x() 
        l_scoreboard.update_score()
    elif ball.xcor() < -360:
        ball.reset_position()
        r_scoreboard.update_score()
    
    elif ball.xcor() > 360:
        ball.reset_position()
        l_scoreboard.update_score()

    if l_scoreboard.score >= 10 or r_scoreboard.score >=10:
        game_is_on = False
        l_scoreboard.game_over()
  
screen.exitonclick()

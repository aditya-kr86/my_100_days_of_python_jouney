from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Snake Game - ADITYA KUMAR')
screen.tracer(0)  # Stop updating the screen

snake = Snake()

screen.update()  # Update the screen after initial setup

food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    snake.move()
    screen.update()  # Update the screen to reflect the new positions
    time.sleep(0.15)  # Add a small delay to prevent the program from freezing


    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        snake.reset_snake()
        scoreboard.reset()
    
    for segment in snake.all_segment[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            snake.reset_snake()
            scoreboard.reset()
            















screen.exitonclick()

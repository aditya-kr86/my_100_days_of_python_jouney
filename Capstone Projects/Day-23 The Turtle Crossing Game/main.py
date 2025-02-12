from turtle import Screen
from player import Timmy
from scoreboard import Level
from car_manager import Car
from powerup import PowerUp
from obstacle import Obstacle
import time
import pygame
from collections import deque
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Initialize pygame for sound effects
pygame.mixer.init()
collision_sound = pygame.mixer.Sound("collision.wav")
level_up_sound = pygame.mixer.Sound("level_up.wav")
power_up_sound = pygame.mixer.Sound("power_up.wav")

# Constants
INITIAL_SLEEP_TIME = 0.17
INITIAL_CAR_GEN_TIME = 5
LEVEL_UP_SPEED_INCREMENT = 0.02
LEVEL_UP_GEN_DECREMENT = 0.5
CAR_SPEED_INCREMENT = 0.1

# Screen setup
screen = Screen()
screen.title('Turtle Crossing Game - Aditya Kumar')
screen.setup(width=600, height=600)
screen.bgcolor('White')
screen.tracer(0)

# Show instructions
instructions = Level(0, 0)
instructions.clear()
instructions.color('Black')
instructions.write("Use the Up,Left,Right\narrow key to move the turtle.\nAvoid cars and obstacles!", align="center", font=("Courier", 20, "normal"))
screen.update()  # Ensure instructions are drawn on screen
time.sleep(5)  # Delay to allow players to read instructions
instructions.clear()

# Create game objects
tortoise = Timmy()
score = Level(-280, 270)
all_cars = deque()
car_pool = deque()
power_up = PowerUp()
obstacles = [Obstacle() for _ in range(10)]  # Create multiple obstacles

# Control setup
screen.listen()
screen.onkeypress(tortoise.go_up, "Up")
screen.onkeyrelease(tortoise.stop_up, "Up")

screen.onkeypress(tortoise.go_right, "Right")
screen.onkeyrelease(tortoise.stop_right, "Right")

screen.onkeypress(tortoise.go_left, "Left")
screen.onkeyrelease(tortoise.stop_left, "Left")

# Initial settings
sleep_time = INITIAL_SLEEP_TIME
car_gen_time = INITIAL_CAR_GEN_TIME
car_speed = 10

def get_car():
    """Reuse a car from the pool or create a new one."""
    if car_pool:
        car = car_pool.popleft()
        car.refresh()
    else:
        car = Car()
    return car

# Main game loop
i = 0
game_is_on = True
while game_is_on:
    if i % int(car_gen_time) == 0:
        new_car = Car()
        all_cars.append(new_car)

    # Batch processing: moving cars and collision detection
    for car in list(all_cars):
        car.move(car_speed)
        if car.xcor() <= -350:
            all_cars.popleft()
            car_pool.append(car)
        if tortoise.distance(car) < 20:
            game_is_on = False
            score.game_over()
            collision_sound.play()
            break
    # Batch processing: checking collisions with obstacles
    for obstacle in obstacles:
        if obstacle.xcor() == power_up.xcor() and obstacle.ycor() == power_up.ycor():
            power_up.refresh()
        if tortoise.distance(obstacle) < 20:
            game_is_on = False
            score.game_over()
            collision_sound.play()
            break

    # Check if player collects the power-up
    if tortoise.distance(power_up) < 20:
        power_up.refresh()
        score.level += 1
        # tortoise.level_up()
        score.update_board()
        power_up_sound.play()

    # Screen update and sleep management
    if i % 10 == 0:  # Update screen every 10 iterations to reduce flicker
        screen.update()

    time.sleep(sleep_time)
    screen.update()
    if tortoise.ycor() >= 280:
        tortoise.reset_position()
        tortoise.animate()  # Add this line to animate the player
        score.update_level()
        # tortoise.level_up()
        level_up_sound.play()
        sleep_time = max(sleep_time - LEVEL_UP_SPEED_INCREMENT, 0.05)  # Ensure sleep_time doesn't go below 0.05
        car_gen_time = max(car_gen_time - LEVEL_UP_GEN_DECREMENT, 1)   # Ensure car_gen_time doesn't go below 1

    i += 1

screen.exitonclick()

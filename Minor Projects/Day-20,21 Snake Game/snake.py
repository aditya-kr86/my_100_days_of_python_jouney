from turtle import Turtle
SET_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_segment = []
        self.create_snake()
        self.head = self.all_segment[0]

    def create_snake(self):
        for position in SET_POSITION:
            self.add_segment(position)

            
    def add_segment(self,position):
        segment = Turtle('square')
        segment.fillcolor('white')
        segment.penup()
        segment.goto(position)
        self.all_segment.append(segment)
       
    def reset_snake(self):
        for seg in self.all_segment:
            seg.goto(1000,1000)
        self.all_segment.clear()
        self.create_snake()
        self.head = self.all_segment[0]

    ### add anew segment to the snake
    def extend(self):
        self.add_segment(self.all_segment[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def move(self):      # Move the segment forward
        for seg_num in range(len(self.all_segment)-1, 0, -1):
            new_x = self.all_segment[seg_num-1].xcor()
            new_y = self.all_segment[seg_num-1].ycor()
            self.all_segment[seg_num].goto(x=new_x,y=new_y)
        self.head.forward(MOVE_DISTANCE)

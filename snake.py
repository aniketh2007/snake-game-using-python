# Snake's appearence and behaviour its all captured here
from turtle import Turtle
STARTING_POSTIONS = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for positions in STARTING_POSTIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)
        self.head = self.segments[0]

    #Add a new segment to the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.setheading !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.setheading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.setheading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading != LEFT:
            self.head.setheading(RIGHT)
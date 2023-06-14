from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90) # face north
        self.goto(STARTING_POSITION)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        





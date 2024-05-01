from turtle import Turtle
from random import randint

def horizontal(t, x, thickness):
    t.penup()
    t.goto(x, -180)
    t.pendown()
    t.pensize(thickness)
    t.goto(x, 200)
    t.penup()

def setup():
    t = Turtle()
    # create starting line
    t.pensize(5)
    t.penup()
    t.goto(-200, -180)
    t.pendown()
    t.goto(-200, 200)
    
    # create horizonatl lines across the racing using horizontal() func
    
    for a in range(-150, 200, 50):
        horizontal(t, a, 1)


    # finish line setup
    t.penup()
    t.goto(200, -200)
    ypos = 0
    i = 1
    t.shape('square')

    # create checkered finish line
    # taken from 2023 Term 4 Year 9 Booklet project 8.?
    for a in range(3):
        t.penup()
        while ypos <= 180:
            t.setheading(90)
            if i == 0:
                t.fillcolor('black')
                i = 1
            else:
                t.fillcolor('white')
                i = 0
            t.forward(20)
            t.stamp()
            # t.pencolor('white')
            ypos = t.ycor()
        # print(ypos)
        t.penup()
        t.goto(220+(a*20), -200)
        t.pendown()
        if i == 0:
            t.fillcolor('black')
            i = 1
        else:
            t.fillcolor('white')
            i = 0
        ypos = t.ycor()
    t.hideturtle()
    
    # end of setup
    
class ninja:
    def up(self):
        self.turtle.penup()
        self.state = "up"
        
    def down(self):
        self.turtle.pendown()
        self.state = "down"
    
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        self.turtle = Turtle()
        self.turtle.color(self.color)
        self.turtle.shape("turtle")
        self.state = "down"
        self.up()
        # print(self.state)
        
    def move_forward(self, distance):
        self.turtle.forward(distance)
        
    def turn(self, angle):
        self.turtle.right(angle)
        
    def goto(self, coord):
        # make sure to pass a tuple of co-ords in (x, y)
        # do not use as goto(x, y), use as goto((x, y)) or:
        # coord = (x, y)
        # then
        # goto(coord)
        self.turtle.penup()
        self.turtle.goto(coord[0], coord[1])
        if self.state == "down":
            self.down()
        
Leonardo = ninja("Leonardo", "blue")
Donatello = ninja("Donatello", "purple")
Raphael = ninja("Raphael", "red")
Michelangelo = ninja("Michelangelo", "orange")

turtles = [Leonardo, Donatello, Raphael, Michelangelo]

m = 80
# set offset to 0 when using arrow as shape
# offset is used for when the turtle shape is turtle to adjust for the size
offset = -15

for a in turtles:
    a.goto((-200+offset, -200+m))
    m += 85
    


"""Leonardo.goto((-160, 100))
Donatello.goto((-160, 150))
Raphael.goto((-160, 200))
Michelangelo.goto((-160, 250))"""

setup()

win = False

# TODO adjust the win_x to be the x co-ordinate of the finish line to adjust for the turtle size
# when using the arrow as shape in stead of turtle, the end of the arrow is the x co-ordinate of the turtle
# set win_x to 200 when turtle shape is arrow

win_x = 185

while win != True:
    for a in turtles:
        if win == True:
            break
        a.move_forward(randint(10, 40))
        if a.turtle.xcor() >= 185:
            win = True
            # print("winner")
            # print(a.turtle.xcor())


# temporary method to keep window open
# turtle.done() used to work ... 
input("Press any key to close")
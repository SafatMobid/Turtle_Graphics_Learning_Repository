import turtle
from turtle import * 

tom = turtle.Turtle()

#Triangle
tom.color("red")
tom.begin_fill()
tom.left(45)
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(135)
tom.forward(141)
tom.end_fill()

#moves "pen" without drawing on the page
tom.penup()
tom.forward(100)
tom.pendown()

#Square
tom.color("#09A7A2", "cyan") #can use hex value for colors. 
#first value is oultline color, second value is fill color

tom.begin_fill()
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.end_fill()

#move pen
tom.penup()
tom.left(45)
tom.forward(150)
tom.pendown()

#circle
tom.color("yellow", "orange")
tom.begin_fill()
for i in range(360):
    tom.right(1)
    tom.forward(1)
tom.end_fill()



turtle.done()

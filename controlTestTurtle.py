import turtle
from turtle import * #imports everything from turtle module, can use functions from the turtle module directly without needing to prefix them with turtle 
# So instead of writing turtle.forward(100), you can just write forward(100)
#also imports the abilitiy to "listen" from turtle library

testTurtle = turtle.Turtle()

#We need to define what the key press does when we r listening to inputs
def up(): 
    testTurtle.forward(100)

def down():
    testTurtle.back(100)

def left():
    testTurtle.left(30)
    
def right():
    testTurtle.right(30)    

listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')


turtle.done() # Always want to end with this line
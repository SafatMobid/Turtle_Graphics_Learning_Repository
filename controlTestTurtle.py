import turtle
from turtle import * #imports everything from turtle module, can use functions from the turtle module directly without needing to prefix them with turtle 

testTurtle = turtle.Turtle()

# Global value becuase multiple functions need to access and modify their values
left_held = False
right_held = False

#We need to define what the key press does when we r listening to inputs
def up(): 
    testTurtle.forward(100)

def down():
    testTurtle.back(100)

def rotate_left(): #control rotation
    if left_held:
        testTurtle.left(10) #angle it will rotate
        ontimer(rotate_left, 100) #call again after 100ms
    
def rotate_right(): #control rotation
    if right_held:
        testTurtle.right(10)
        ontimer(rotate_right, 100)    

def press_left(): # Function to check if "left key" is held 
    global left_held
    left_held = True # if key is held 
    rotate_left() # runs the function rotate_left()

def release_left(): # Function to check if "left key" that was held is let go
    global left_held 
    left_held = False # if it was let go it stop rotating

#Same things for the right key
def press_right():
    global right_held
    right_held = True
    rotate_right()

def release_right():
    global right_held
    right_held = False

listen()
onkey(up, 'Up')
onkey(down, 'Down')

#left key control
onkeypress(press_left, "Left")
onkeyrelease(release_left, "Left")

#right key control
onkeypress(press_right, "Right")
onkeyrelease(release_right, "Right")

turtle.done() # Always want to end with this line
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)
def turn_left():
    tim.setheading(tim.heading() + 10)
def turn_right():
    tim.setheading(tim.heading() - 10)
def clear_home():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def ecrire():
    tim.write("Steve", True, "center", "Arial")
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="c", fun=clear_home)
screen.onkey(key="p", fun=ecrire)
screen.exitonclick()

import turtle
from turtle import Turtle, Screen
import random


def forme(pim: Turtle, cote: int) -> None:
    angle = 360 / cote
    for _ in range(cote):
        pim.forward(100)
        pim.right(angle)


def tiret(pim: Turtle):
    for _ in range(10):
        pim.forward(10)
        pim.penup()
        pim.forward(10)
        pim.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#liste_forme = [3, 4, 5, 6, 7, 8, 9, 10]
turtle.colormode(255)
#list_color = ["dark goldenrod", "chartreuse", "blue", "olive drab", "dark red", "magenta", "gold", "yellow",
              #"spring green", "medium purple"]
direction = [0, 90, 180, 270]
tim = Turtle()
#tim.shape("arrow")
#tim.pensize(15)
tim.speed(6)
# tim.color("Red")
# for nbre in liste_forme:
#     tim.color(random.choice(list_color))
#     forme(tim, nbre)
""""
for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(direction))
    tim.color(random_color())
"""
def spirograph(size_of_gap):
    i = 1
    for _ in range(int(360/size_of_gap)):
        print(i)
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() +size_of_gap) #changer la l angle de la tortue
        i += 1
spirograph(20)


screen = Screen()
screen.exitonclick()

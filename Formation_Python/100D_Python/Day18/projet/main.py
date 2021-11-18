import turtle

import colorgram, random
from turtle import Turtle, Screen


# colors = colorgram.extract("image.jpg", 30)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb = (r, g, b)
#     rgb_color.append(new_rgb)
# print(rgb_color)
turtle.colormode(255)
my_color = [ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()

tim.speed("fastest")
tim.penup() # supprimer le tracage
tim.hideturtle() # cache la tortue
"""initialisation of our point"""
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

nbre_of_dot = 100
for dot_nbre in range(1, nbre_of_dot+1):
    tim.dot(20, random.choice(my_color)) # creation du point
    tim.forward(50)
    if dot_nbre % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)




screen = Screen()
screen.exitonclick()
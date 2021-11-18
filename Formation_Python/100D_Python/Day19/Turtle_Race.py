from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400) # definir le taille de l ecran
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ") # afficher un pop up
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100) # deplace la tortue aux coordonnees x, y
turtle_liste = []
i = 0
for color in colors:
    turl = Turtle(shape="turtle")
    turl.penup()
    turl.color(color)
    turl.goto(x=-230 , y=-100 + i)
    i += 50
    turtle_liste.append(turl)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in turtle_liste:
        if turtles.xcor() > 230:
            is_race_on = False
            winner_color = turtles.pencolor()
            if winner_color == user_bet:
                print(f"You have won! the {winner_color} Turtle is the Winner")
            else:
                print(f"You have Lost! the {winner_color} Turtle is the Winner")

        distance = random.randint(0, 10)
        turtles.forward(distance)


screen.exitonclick()
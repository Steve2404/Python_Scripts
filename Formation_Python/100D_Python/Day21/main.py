from turtle import Turtle, Screen
import paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle = paddle.Paddle((380, 0))
l_paddle = paddle.Paddle((-380, 0))

ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # on faire rebondit la balle sur les murs
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # test si l utilisateur a manque de frapper la balle
    #ici c est le cote droit
    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point()
    #ici c est le cote gauche
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
    ball.move()

screen.exitonclick()
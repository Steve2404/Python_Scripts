from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # supprime les déplacement de la tortue

# i = 0
# for _ in range(3):
#     tim = Turtle("square")
#     tim.color("white")
#     tim.setposition(x= tim.heading() - i, y=tim.heading())
#     i += 20

snake = Snake()
food = Food()
board = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #is_game_on = False
        board.reset()
        snake.reset()
    # Ici on teste si le la tete a rencontre une partie du corps
    for segment in snake.snake[1:]:
         if snake.head.distance(segment) < 10:
            #is_game_on = False
            board.reset()
            snake.reset()

screen.exitonclick()

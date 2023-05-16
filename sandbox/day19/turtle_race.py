import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color:")

turtles = []

def reached_finishing_line(current_turtle):
    return current_turtle.xcor() > (screen.window_width() / 2) - 20

y_position = 70

for turtle_index in range(0, 6):
    random_turtle = Turtle()
    random_turtle.shape("turtle")
    random_turtle.penup()
    random_turtle.color(colors[turtle_index])
    random_turtle.goto(x=-((screen.window_width() - 20) / 2), y=y_position)
    y_position -= 30
    turtles.append(random_turtle)


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if reached_finishing_line(turtle):
            winning_color = turtle.pencolor()
            winning_turtle = Turtle()
            winning_turtle.shape("turtle")
            winning_turtle.color(winning_color)
            winning_turtle.shape("blank")
            winning_turtle.penup()
            winning_turtle.sety((screen.window_height()/2) - 40)
            size = turtle.turtlesize()
            increase = (3 * num for num in size)
            turtle.turtlesize(*increase)
            turtle.goto(0, 100)
            if winning_color == user_bet:
                winning_turtle.write(f"You win! The {winning_color} turtle is the winner!", move=False, align="center", font=("Arial", 20, "normal"))
            else:
                winning_turtle.write(f"You lose! The {winning_color} turtle is the winner!", move=False, align="center", font=("Arial", 20, "normal"))
            is_race_on = False

screen.exitonclick()

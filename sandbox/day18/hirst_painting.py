import turtle

import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []


def generate_color_pallet():
    colorgram_colors = colorgram.extract('hist_painting.jpg', 6)
    for color in colorgram_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    # added white color to simulate blank spaces
    rgb_colors.append((255, 255, 255))


hist_painting_brush = Turtle(shape="circle", visible=False)

screen = Screen()
screen.setworldcoordinates(-10, -10, screen.window_width(), screen.window_height())

generate_color_pallet()
turtle.colormode(255)
hist_painting_brush.penup()
hist_painting_brush.speed("fastest")


def paint_random_dot_color():
    hist_painting_brush.dot(20, random.choice(rgb_colors))


def move_forward_and_paint():
    paint_random_dot_color()
    hist_painting_brush.forward(70)
    paint_random_dot_color()


def go_up():
    hist_painting_brush.setheading(90)
    hist_painting_brush.forward(70)


def turn_left():
    hist_painting_brush.setheading(180)


def turn_right():
    hist_painting_brush.setheading(0)


while hist_painting_brush.ycor() < screen.window_height():
    while hist_painting_brush.xcor() + 50 < screen.window_width():
        move_forward_and_paint()
    go_up()
    paint_random_dot_color()
    turn_left()
    while hist_painting_brush.xcor() - 50 > 0:
        move_forward_and_paint()
    go_up()
    paint_random_dot_color()
    turn_right()
screen.exitonclick()

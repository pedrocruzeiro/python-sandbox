from turtle import Turtle, Screen
import random


def reset_tim():
    tim.clear()
    tim.reset()
    tim.shape("blank")
    tim.pensize(5)
    tim.speed(5)


def generate_random_tim_color():
    tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def draw_geometric_shapes():
    for i in range(3, 10):
        generate_random_tim_color()
        draw_shape(i)


def choose_random_direction():
    directions = [0, 90, 180, 270]
    return random.choice(directions)


def draw_random_walk(number_of_turns):
    tim.speed("fastest")
    for i in range(number_of_turns):
        generate_random_tim_color()
        tim.forward(20)
        tim.setheading(choose_random_direction())


def dram_random_siprograph(size_of_the_gap):
    tim.speed("fastest")
    for i in range(int(360 / size_of_the_gap)):
        generate_random_tim_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_the_gap)


tim = Turtle()
screen = Screen()
screen.colormode(255)

reset_tim()
draw_geometric_shapes()
reset_tim()
draw_random_walk(200)
reset_tim()
dram_random_siprograph(8)

screen.exitonclick()

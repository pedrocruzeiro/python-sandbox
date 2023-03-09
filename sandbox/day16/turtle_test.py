from turtle import Turtle, Screen

DISTANCE = 100

def polygon(turtle, sides):
    for _ in range(sides):
        turtle.forward(DISTANCE)
        turtle.right(360 / sides)

shapes = { \
    'triangle': lambda turtle: polygon(turtle, 3), \
    'square': lambda turtle: polygon(turtle, 4), \
    'pentagon': lambda turtle: polygon(turtle, 5), \
}

shape = input('Pick a shape: ' + ", ".join(shapes) + ': ')

if shape in shapes:

    yertle = Turtle(shape='turtle')

    shapes[shape](yertle)

    screen = Screen()
    screen.exitonclick()

else:
    print('Bad input!')
import turtle


def create_turtle(x, y, color='green', shape='turtle'):
    t = turtle.Turtle()
    t.shape(shape)
    t.color(color)
    t.penup()
    t.setposition(x, y)
    return t


screen = turtle.Screen()
kornjaca = create_turtle(0, 0)


def move_left():
    current_position = kornjaca.pos()
    kornjaca.goto(current_position[0] - 10, current_position[1])


screen.onkey(move_left, "Left")

screen.listen()
screen.exitonclick()

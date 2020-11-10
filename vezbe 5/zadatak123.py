import turtle


def create_turtle(x, y):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    t.penup()
    t.setposition(x, y)
    return t


screen = turtle.Screen()
turtle1 = create_turtle(150, 150)

screen.exitonclick()

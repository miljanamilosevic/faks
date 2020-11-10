import turtle


def create_turtle(x, y, color='green', shape='turtle'):
    t = turtle.Turtle()
    t.shape(shape)
    t.color(color)
    t.penup()
    t.setposition(x, y)
    return t


def create_turtle1234(width, height):
    turtle1 = create_turtle(-width/2, height/2, color='red')
    turtle2 = create_turtle(width/2, height/2, color='blue')
    turtle3 = create_turtle(width/2, -height/2, color='pink')
    turtle4 = create_turtle(-width/2, -height/2)


screen = turtle.Screen()
create_turtle1234(400, 400)


screen.exitonclick()

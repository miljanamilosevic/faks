import turtle


def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.setup(width, height)
    return screen


prozor = create_screen("Kornjacin prozor", 200, 400)
prozor.exitonclick()

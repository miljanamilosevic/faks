import turtle


def create_screen(file_path):
    f = open(file_path, 'r')
    setup_string = f.read().strip()
    setup = setup_string.split(',')
    print(setup)
    print(setup_string)
    screen = turtle.Screen()
    screen.title(setup[2])
    screen.setup(int(setup[0]), int(setup[1]))
    return screen


screen = create_screen('screen.setup.txt')
screen.exitonclick()

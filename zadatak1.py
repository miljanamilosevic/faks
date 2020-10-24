import turtle
screen = turtle.Screen()
screen.setup(500, 500)

kornjaca = turtle.RawTurtle(screen)
kornjaca.shape('turtle')

for i in range(4):
    kornjaca.forward(150)
    kornjaca.right(90)

screen.exitonclick()
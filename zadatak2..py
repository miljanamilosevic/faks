import turtle
screen = turtle.Screen()
screen.setup(500, 500)

kornjaca = turtle.RawTurtle(screen)
kornjaca.shape('turtle')

kornjaca.forward(200)
kornjaca.right(90)

kornjaca.forward(100)
kornjaca.right(90)

kornjaca.forward(200)
kornjaca.right(90)

kornjaca.forward(100)
kornjaca.right(90)


screen.exitonclick()
import turtle
screen = turtle.Screen()
screen.setup(500, 500)

kornjaca = turtle.RawTurtle(screen)
kornjaca.shape('turtle')

a = eval(input("a: "))
b = eval(input("b: "))

kornjaca.forward(a)
kornjaca.right(90)

kornjaca.forward(b)
kornjaca.right(90)

kornjaca.forward(a)
kornjaca.right(90)

kornjaca.forward(b)
kornjaca.right(90)


screen.exitonclick()
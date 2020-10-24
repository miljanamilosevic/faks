import turtle
screen = turtle.Screen()
screen.setup(500, 500)

kornjaca = turtle.RawTurtle(screen)
kornjaca.shape('turtle')

a = eval(input("a: "))
b = eval(input("b: "))

kornjaca.forward(a)
kornjaca.left(90)
kornjaca.forward(b)
kornjaca.goto(0,0)


screen.exitonclick()
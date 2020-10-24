import turtle
screen = turtle.Screen()
screen.setup(500, 500)

kornjaca = turtle.RawTurtle(screen)
kornjaca.shape('turtle')

a = 150
b = 50
c = (a*a+b*b)**0.5

kornjaca.forward(a)
kornjaca.left(90)
kornjaca.forward(b)
kornjaca.goto(0,0)

screen.exitonclick()

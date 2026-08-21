import colorsys
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

n = 150
h = 0

for i in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    h += 1 / n
    t.forward(i * 1.5)
    t.left(122)
    t.forward(i * 1.5)
    t.right(70)

turtle.done()
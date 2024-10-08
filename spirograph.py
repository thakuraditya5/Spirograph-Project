from turtle import  Screen
import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
n=5
def random_color():
    r= random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r,b,g)
    return random_color

while 0<n< 400:

    timmy.circle(100)
    timmy.color(random_color())
    timmy.setheading(5+n)
    n+=5



screen = Screen()
screen.exitonclick()

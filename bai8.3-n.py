import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red","green","blue","orange","purple","pink","yellow"]

for i in range(12):        
    t.pencolor(random.choice(colors))
    t.circle(100)
    t.right(30)            

turtle.done()

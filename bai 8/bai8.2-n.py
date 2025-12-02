print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import turtle, random

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

colors = ["red","orange","yellow","green","blue","purple","pink"]

for i in range(36):              
    t.pencolor(random.choice(colors))
    t.circle(100)
    t.left(10)                   

turtle.done()

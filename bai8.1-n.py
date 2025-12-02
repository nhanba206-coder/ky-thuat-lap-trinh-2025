print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.pencolor("blue")

for i in range(30):
    for j in range(4):
        t.forward(200)
        t.left(90)
    t.left(12)        

turtle.done()

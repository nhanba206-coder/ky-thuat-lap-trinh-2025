print("sinh vien: nguyen ba nhan")
print("msv: 245752021610141")
import math

pos = [0, 0]

while True:
    s = input()  
    if not s:    
        break

    movement = s.split()
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
print(distance)

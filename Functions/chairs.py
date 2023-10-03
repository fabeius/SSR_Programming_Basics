from turtle import forward, right, left, exitonclick, goto

goto(-150,-150)

def step(size):
    forward(size)
    left(90)
    forward(size)
    right(90)

for size in range(20,70,5):
    step(size)

exitonclick()
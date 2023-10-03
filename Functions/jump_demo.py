from turtle import forward, left, right, exitonclick

def jump(size):
    forward(size)
    left(75)
    forward(size)
    right(150)
    forward(size)
    left(75)

for size in range (10,70,5):    #die size variable wird von 10 bis 70 in 5er Schritten gezählt - demensprechend werden die forward grössen immer verändert/grösser
    jump(size)

exitonclick()


from turtle import forward, left, right, exitonclick

def jump(hight=30):
    left(75)
    forward(hight)
    right(150)
    forward(hight)
    left(75)

for size in range (20,70,5):    #die size variable wird von 10 bis 70 in 5er Schritten gezählt - demensprechend werden die forward grössen immer verändert/grösser
    forward(30)
    jump(size)


exitonclick()
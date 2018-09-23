import turtle
def sqloop():
    window = turtle.Screen()
    window.bgcolor("red")
    

    v = turtle.Turtle()
    v.shape("circle")
    for i in range(4):
        v.forward(100)
        v.right(90)

    window.exitonclick()

sqloop()

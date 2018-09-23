import turtle
def draw_square():
    window =turtle.Screen()
    window.bgcolor("red")

    b = turtle.Turtle()
    b.shape("turtle")
    
    b.speed(2)
    b.color("blue")
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)


    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

    
    window.exitonclick()

draw_square()

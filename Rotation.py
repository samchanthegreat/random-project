import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(400, 400)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(10)
pen.pencolor("green")
i = 0
rc = turtle.Turtle()
rc.pencolor("green")
rc.hideturtle()
rc.shape("circle")
rc.turtlesize(0.2)
rc.goto(0, 5)
cc = turtle.Turtle()
cc.hideturtle()
cc.goto(0, -5)
cc.pencolor("green")
cc.write("made by @samchanthegreat", align="center", font=("Courier New", 10, "normal"))
pen.penup()
pen.goto(0, -120)
pen.pendown()
pen.pensize(15)

while i >= 0:
    pen.clear()
    pen.circle(120)
    i += 1
    pen.clear
    rc.clear()
    rc.write(f"Rotation = {i}", align="center", font=("Courier New", 20, "normal"))



wn.mainloop()

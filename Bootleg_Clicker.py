import turtle
import os

wn = turtle.Screen()
wn.title("bootleg cookie clicker by @samchanthegreat")
wn.bgcolor("black")
wn.setup(400, 400)
os.chdir("C:\\Users\\REZER\\Downloads")
wn.register_shape("cookie.gif")
clicks = 0



pen = turtle.Turtle()
pen.turtlesize(5)
pen.penup()
pen.shape("cookie.gif")
pen.circle(40)
pen.goto(0, 120)

pcc = turtle.Turtle()
pcc.turtlesize(1)

def clicked(x, y):
    global clicks
    clicks += 1
    pcc.clear()
    pcc.color("white")
    pcc.write(f"Cookie amount: {clicks}", align="center", font=("Courier New", 20, "normal"))
    pcc.hideturtle()

pen.onclick(clicked)


wn.mainloop()

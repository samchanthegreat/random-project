import math
import turtle
import os
import time
import random

#game start window
width = 1000
height = 500
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(1000, 500)
os.chdir("C:\\Users\\REZER\\Pictures\\Dom")

#character
wn.register_shape("forward.gif")
wn.register_shape("backward.gif")
wn.register_shape("left.gif")
wn.register_shape("right.gif")
wn.register_shape("enemy.gif")

#Title
tp = turtle.Turtle()
tp.hideturtle()
tp.speed(0)
tp.penup()
tp.fillcolor("red")
tp.color("green")
tp.goto(0, 222)
tp.write("Dom's Adventure by @samchanthegreat", align="center", font=("Courier New", 20, "normal"))

#Scoreboard
score = 0
sp = turtle.Turtle()
sp.hideturtle()
sp.speed(0)
sp.speed(0)
sp.penup()
sp.goto(400, 225)
sp.color("white")
sp.write(f"Score : {score}", align="center", font=("Courier New", 14, "normal"))



#game border
bp = turtle.Turtle()
bp.speed(0)
bp.hideturtle()
bp.pensize(10)
bp.pencolor("green")
bp.penup()
bp.goto(-470, -220)
bp.pendown()
bp.forward(940)
bp.left(90)
bp.forward(440)
bp.left(90)
bp.forward(940)
bp.left(90)
bp.forward(440)

#player control
pc = turtle.Turtle()
pc.speed(0)
pc.turtlesize(2)
pc.shape("backward.gif")
pc.left(90)
pc.penup()
pcspeed = 10
isdead = "no"

#ammo
am = turtle.Turtle()
am.fillcolor("red")
am.penup()
am.color('red')
am.speed(0)
am.hideturtle()
bulletspeed = 30

#npc
npc = turtle.Turtle()
npc.speed(0)
npc.shape("enemy.gif")
npc.penup()
npc.goto(0, 255)

#infoscreen
isc = turtle.Turtle()
isc.hideturtle()
isc.penup()
isc.speed(0)
isc.color("white")
isc.goto(-380, 227)
isc.write("Press [enter] to start!", align="center", font=("Courier New", 10, "normal"))


## dear God, why doesnt xcor works properly.


def left():
    if pc.xcor() <= -450:
        pc.xcor(-450)
    pc.shape("left.gif")
    pc.setheading(180)
    am.setheading(180)
    pc.forward(pcspeed)

def right():
    if pc.xcor() >= 450:
        pc.xcor(450)
    pc.shape("right.gif")
    pc.setheading(0)
    am.setheading(0)
    pc.forward(pcspeed)

def forward():
    if pc.ycor() >= 195:
        pc.ycor(195)
    pc.shape("forward.gif")
    pc.setheading(90)
    am.setheading(90)
    pc.forward(pcspeed)

def backward():
    if pc.ycor() <= -195:
        pc.ycor(-195)
    pc.shape("backward.gif")
    pc.setheading(-90)
    am.setheading(-90)
    pc.forward(pcspeed)

def hit():
    global score
    distance= am.xcor()-npc.xcor() + am.ycor()-npc.ycor()
    if -30<= distance <=30:
        print("hit!")
        sp.clear()
        score += 1
        sp.write(f"Score : {score}", align="center", font=("Courier New", 14, "normal"))
        am.setposition(0, 1000)
        npc. goto(random.randint(-8, 8) *50, random.randint(-4, 4)*50)
    else:
        return False

def shoot():
    ammostate = "ready"
    if ammostate == "ready":
        ammostate = "not ready"
        am.setposition(pc.pos())
        am.showturtle()
        am.pendown()
        am.forward(50)
        time.sleep(0.01)
        am.penup()
        am.clear()
        am.hideturtle()
        hit()
        time.sleep(0.5)
        am.setposition(0, -400)
        ammostate = "ready"

def chaser():
    npc.setheading(npc.towards(pc))
    npc.forward(1)
    kill()
    wn.ontimer(chaser, 1)


def quitapp():
    wn.bye()
def locdebug():
    print({pc.pos()})

def kill():
    global score
    distance = pc.xcor() - npc.xcor() + pc.ycor() - npc.ycor()
    if -10 <= distance <= 10:
        print("kill!")
        am.setposition(0, 1000)
        npc.goto(0, 2000)
        pc.hideturtle()
        tp.clear()
        tp.write("GAME OVER !", align="center", font=("Courier New", 20, "normal"))

    else:
        return False

def start():
    global score
    pc.showturtle()
    npc.goto(0, 255)
    npc.showturtle()
    score = 0
    sp.clear()
    sp.write(f"Score : {score}", align="center", font=("Courier New", 14, "normal"))
    tp.clear()
    tp.write("Dom's Adventure by @samchanthegreat", align="center", font=("Courier New", 20, "normal"))
    chaser()


turtle.listen()
wn.onkey(left, 'a')
wn.onkey(right, 'd')
wn.onkey(forward, 'w')
wn.onkey(backward, 's')
wn.onkey(shoot, "space")
wn.onkey(start, "Return")
wn.onkey(hit, "x")




wn.mainloop()

import time
import turtle
import random

t_d = 0.2
p_s = 0
h_s = 0

w = turtle.Screen()
w.title("Game")
w.bgcolor("white")
w.setup(width=600, height=600)

s = turtle.Turtle()
s.shape("square")
s.color("red")
s.penup()
s.goto(0, 0)
s.direction = "Stop"

s_f = turtle.Turtle()
sps = random.choice("triangle", "circle")
s_f.shape(sps)
s_f.pen()
s_f.goto(0, 100)

p = turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.penup()
p.hideturtle()
p.goto(0, 250)
p.write("Cunt", align="center", font=("Arial", 24, "normal"))

turtle.mainloop()

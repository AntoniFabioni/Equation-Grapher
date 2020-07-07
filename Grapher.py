import numpy as np
import matplotlib as plt
import turtle

t = turtle.Turtle()

# 1 to 10 ramps up speed, but 0 is fastest speed.
t.speed(0)

# domain, range of values displayed is [-width/2, width/2], [-height/2, height/2].
width, height = 400, 400

# How many units are the gridlines spaced apart?
gridSpacing = 10

# Any function y = f(x) will work here.
def f(x):
    return (150 / (1 + np.exp(20 - x / 4)) - 60) - (120 / (1 + np.exp(30 + x / 2)) - 20)

def g(x):
    return (120 / (1 + np.exp(30 - x / 4)) - 60) - (150 / (1 + np.exp(40 + x / 2)) - 40)

def drawAxes():
    t.color('blue')
    t.pensize(3)
    
    t.penup()
    t.goto(-width/2, 0)
    t.pendown()
    t.goto(width/2, 0)

    t.penup()
    t.goto(0, -height/2)
    t.pendown()
    t.goto(0, height/2)

def drawGrid():
    t.color('black')
    t.pensize(1)
    
    adjustment = 0
    while adjustment <= width:
        t.penup()
        t.goto(-width/2, height/2 - adjustment)
        t.pendown()
        t.goto(width/2, height/2 - adjustment)
        adjustment += gridSpacing
    
    adjustment = 0
    while adjustment <= height:
        t.penup()
        t.goto(-width/2 + adjustment, height/2)
        t.pendown()
        t.goto(-width/2 + adjustment, -height/2)
        adjustment += gridSpacing

def drawGraph(f, x1, x2, colour='red'):
    x1 = int(min(x1, x2))
    x2 = int(max(x1, x2))

    t.penup()
    t.pensize(3)
    t.pencolor(colour)
    y = 0
    t.penup

    for x in range(x1, x2 + 1):
        y = f(x)

        if abs(y) <= height / 2:
            t.goto(x, y)
            t.pendown()

drawAxes()
drawGrid()
drawGraph(f, -width / 2, width / 2)
drawGraph(g, -width / 2, width / 2, 'green')

# Wait until click to dismiss the graph.
turtle.exitonclick()
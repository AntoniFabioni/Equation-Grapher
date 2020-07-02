import numpy as np
import matplotlib as plt
import turtle

t = turtle.Turtle()
t.speed(0)

width, height = 400, 400
gridSpacing = 10

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

def f(x):
    return x

drawAxes()
drawGrid()

turtle.exitonclick()
import numpy as np
import matplotlib as plt
import turtle

t = turtle.Turtle()

def drawAxes(width, height):
    t.penup()
    t.goto(-width/2, 0)
    t.pendown()
    t.goto(width/2, 0)

    t.penup()
    t.goto(0, -height/2)
    t.pendown()
    t.goto(0, height/2)

def f(x):
    return x

drawAxes(200,200)
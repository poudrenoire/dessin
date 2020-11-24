# Génère des dessins aléatoirement
import turtle
import random
import time
import Tkinter
import uuid

screen = turtle.Screen()
screen.colormode(255)
turtle.speed(9)

# Générateur de dessins
for _ in range(25):
  turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  turtle.left(random.randint(0,360))
  turtle.forward(random.randint(0,25))
  turtle.right(random.randint(0,360))
  turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  turtle.forward(random.randint(0,100))
  turtle.pensize(random.randint(0,6))
  turtle.tilt(random.randint(0,360))
  turtle.right(random.randint(0,360))
  turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  turtle.circle(random.randint(0,100), random.randint(0,360))
  turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  turtle.forward(random.randint(0,100))
  turtle.pensize(random.randint(0,6))
  turtle.goto(random.randint(-200,200),random.randint(-200,200))
turtle.done()

ts = turtle.getscreen()
ts.getcanvas().postscript(file=str(uuid.uuid4())))

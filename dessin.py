# Génère des dessins aléatoirement
import turtle
import random
import time

screen = turtle.Screen()
screen.colormode(255)

# Génération de 3 nombres au hasard pour usage RVB
col_a = random.randint(0,255)
col_b = random.randint(0,255)
col_c = random.randint(0,255)
turtle.speed(9)

# Générateur de dessins
for _ in range(250):
  turtle.pencolor(col_a, col_b, col_c)
  turtle.left(random.randint(0,360))
  turtle.forward(random.randint(0,25))
  turtle.left(random.randint(0,360))
  turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  turtle.forward(random.randint(0,100))
  turtle.pensize(random.randint(0,10))
  turtle.right(random.randint(0,360))
  turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  turtle.circle(random.randint(0,100), random.randint(0,360))
  turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  turtle.forward(random.randint(0,100))
  turtle.goto(random.randint(0,100),random.randint(0,100))
time.sleep(5)

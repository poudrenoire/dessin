# Génère des dessins aléatoirement
import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

# Génération de 3 nombres au hasard pour usage RVB
col_a = random.randint(0,255)
col_b = random.randint(0,255)
col_c = random.randint(0,255)

# Générateur de dessins
turtle.pencolor(col_a, col_b, col_c)
turtle.forward(50)
sleep()

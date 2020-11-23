# Génère des dessins aléatoirement
import turtle
import random

# Génération de 3 nombres au hasard pour usage RVB
col_a = random.random(1.0,255.0)
col_b = random.randint(1.0,255.0)
col_c = random.randint(1.0,255.0)

# Générateur de dessins
turtle.pencolor(col_a, col_b, col_c)
turtle.forward(50)

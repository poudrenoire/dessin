# Génère des dessins aléatoirement
import turtle
import random

# Génération de 3 nombres au hasard pour usage RVB
col_a = random.randrange(0.0,255.0)
col_b = random.randrange(0.0,255.0)
col_c = random.randrange(0.0,255.0)

# Générateur de dessins
turtle.pencolor(float(col_a), float(col_b), float(col_c))
turtle.forward(50)

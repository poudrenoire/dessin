# Génère des dessins aléatoirement
import turtle

# Génération de 3 nombres au hasard pour usage RVB
col_a = random.randint(1,255)
col_b = random.randint(1,255)
col_c = random.randint(1,255)

# Générateur de dessins
pencolor(col_a, col_b, col_c)
turtle.forward(50)

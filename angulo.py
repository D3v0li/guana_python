'''FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE
NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO'''

import math
angulo = float(input("Digite o angulo que voce deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O angulo de {angulo} tem o Seno de {seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print(f"O angulo de {angulo} tem o Cosseno de {cosseno:.2f}")
tangente = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem a Tangente de {tangente:.2f}")
'''PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO
E MOSTRE NA TELA A SUA PORÇÃO INTEIRA 
import math
numero = float(input("Digite um número: "))
print(f"O valor digitado foi {numero} e sua porção inteira é {math.trunc(numero)}")
'''

numero = float(input("Digite um numero: "))
print(f"O valor digitado foi {numero} e sua parte inteira é {int(numero)}")
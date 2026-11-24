''' FAÇA UM PROGRAMA QUE QUE LEIA O COMPRIMENTO DO CATETO OPOSTO
E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE
O COMPRIMENTO DA HIPOTENUSA'''
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print(f"A hipotenusa vai medir: {hipotenusa:.2f}")
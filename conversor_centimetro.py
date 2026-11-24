'''escreva um programa que leia um valor em metros e exiba-o covertido em centimetros e milimetros'''

medida = float(input("Digite a distância em metros: "))

centimetros = medida * 100
milimetros = medida * 1000

print(f'''
A média convertido em centimetros é {centimetros:.0f} cm
e em milimetros é igual a {milimetros:.0f} mm ''') 
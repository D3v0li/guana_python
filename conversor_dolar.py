'''crie um programa que leia quanto dinheiro uma pessoa tem na carteira em real e mostre quantos doláres ela pode comprar'''

real = float(input("Quantos reais você tem na carteira? R$ "))

dolares = real / 5.90
print(f'''
Você pode comprar {dolares:.2f} US$''')
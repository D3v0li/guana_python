''' Script que pede as 3 notas do aluno e seu nome calcule a mediae  a frequencia
e mostre se aluno foi reprovado, esta de recuperação ou reprovado'''

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
frequencia = float(input("Digite a frequência do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and frequencia >= 75:
    print(f"{nome} Aluno aprovado parabéns!!!")
elif media >= 5 and frequencia >= 75:
    print(f"{nome} Aluno em recuperação você consegue!!!")
else:
    print(f"{nome} Aluno reprovado estude mais um pouco!!!")
    

    

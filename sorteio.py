'''UM PROFESSOR QUER SORTEAR UM DOS SEUS ALUNOS PARA APAGAR O QUADRO
FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DOS ALUNOS E ESCREVENDO O ESCOLHIDO'''
import random
aluno1 = str(input("Digite o nome do aluno 1: "))
aluno2 = str(input("Digite o nome do aluno 2: "))
aluno3 = str(input("Digite o nome do aluno 3: "))
aluno4 = str(input("Digite o nome do aluno 4: "))

lista=[aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi o aluno: {escolhido}")
'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''

nota = int(input("Digite um nota:"))
presença = int(input("Digite um presença:"))
if nota > 6 and presença >= 75:
    print("Aprovado")
else:
     print("Reprovado")
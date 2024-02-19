# Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno Reprovado com média”. Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno

n1 = float(input("Input with the first note: "))
n2 = float(input("Input with the second note: "))
n3 = float(input("Input with the third note: "))
n4 = float(input("Input with the fourth note: "))

MD = (n1 + n2 + n3 + n4)/4

if(MD) > 5: 
    print(f"Aluno Aprovado com média {MD:.2f}")
else:
    print(f"Aluno Reprovado com média {MD:.2f}")
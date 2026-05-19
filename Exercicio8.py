vetor = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
valor = 0
soma = 0

for i in vetor:
    valor = int(input("Digite uma nota: "))
    vetor[i] = valor
    soma += vetor[i]

print(f"Média dos alunos é: {soma / 15}")

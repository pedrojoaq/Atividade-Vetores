vetor = [0,1,2,3,4,5,6,7,8,9]
valor = 0

for i in vetor:
    valor = int(input("Digite um valor: "))
    vetor[i] = valor

maior = vetor[0]
menor = vetor[0]

for j in vetor:
    if maior < j:
        maior = j
    if menor > j:
        menor = j

print(maior)
print(menor)

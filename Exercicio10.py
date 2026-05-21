vetor = [0,1,2,3,4]
valor = 0
media = 0

for i in vetor:
    valor = int(input("Digite um valor: "))
    vetor[i] = valor
    media += vetor[i]

maior = vetor[0]
menor = vetor[0]

for j in vetor:
    if maior < j:
        maior = j
    if menor > j:
        menor = j

print(f"O maior número listado é: {maior} e o menor é: {menor}")
print(f"A média dos valores é: {media / 5}")

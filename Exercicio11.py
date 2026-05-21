vetor = [0,1,2,3,4]
valor = 0
maior = 0
menor = 0
posicaoMaior = 0
posicaoMenor = 0

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

for j in range(0, 5):
    if vetor[j] == maior:
        posicaoMaior = j
    if vetor[j] == menor:
        posicaoMenor = j

print(f"O maior número listado é: {maior} e está na posição {posicaoMaior}")
print(f"O menor número listado é: {menor} e está na posição {posicaoMenor}")

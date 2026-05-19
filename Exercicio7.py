vetor = [0,1,2,3,4,5,6,7,8,9]
valor = 0
contador = 0

for i in vetor:
    valor = int(input("Digite um valor: "))
    vetor[i] = valor

maior = vetor[0]

for j in vetor:
    if maior < j:
        maior = j

for k in range(0,10):
    if vetor[k] == maior:
        contador = k

for l in vetor:
    print(l)
    
print(maior, contador)

vetor = [0,1,2,3,4,5,6,7,8,9]
valor = 0
contador = 0

for i in vetor:
    valor = int(input("Digite um valor: "))
    vetor[i] = valor
    if valor % 2 == 0:
        contador += 1

print(f"O vetor tem {contador} valores pares")
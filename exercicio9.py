vetor = [0,1,2,3,4,5,6,7,8,9]
contadorNegativos = 0
valor = 0 
soma = 0

for i in vetor:
    valor = int(input("Digite um valor: "))
    vetor[i] = valor
    if vetor[i] < 0:
        contadorNegativos += 1
    else:
        soma += vetor[i]

print(f"A quantidade de números negativos é: {contadorNegativos} e a soma dos números positivos é: {soma}")
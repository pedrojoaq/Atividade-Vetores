vetor = [0,1,2,3,4,5,6,7]
valor = 0
primeiraPosicao = 0
segundaPosicao = 0
soma = 0

for i in vetor:
    valor = int(input("Digite um valor: "))
    vetor[i] = valor

primeiraPosicao = int(input("Digite uma posição: "))

while primeiraPosicao < 0 or primeiraPosicao > 7:
    print("Digite uma posição válida!")
    primeiraPosicao = int(input("Digite uma posição: "))

segundaPosicao = int(input("Digite uma posição: "))

while segundaPosicao < 0 or segundaPosicao > 7:
    print("Digite uma posição válida!")
    segundaPosicao = int(input("Digite uma posição: "))

soma = vetor[primeiraPosicao] + vetor[segundaPosicao]

print(soma)

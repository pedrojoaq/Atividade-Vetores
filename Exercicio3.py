conjunto = [0,1,2,3,4,5,6,7,8,9]
quadradoConjunto = [0,1,2,3,4,5,6,7,8,9]
valor = 0
for i in conjunto:
    valor = int(input("Digite um número: "))
    conjunto[i] = valor
    quadradoConjunto[i] = conjunto[i] * conjunto[i]

for j in conjunto:
    print(j, end=" ")
for k in quadradoConjunto:
    print(k, end=" ")
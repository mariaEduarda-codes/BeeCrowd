lista_de_numeros = []
contagem_positivos = 0
soma = 0

for i in range(6):
    numero = float(input())
    if numero > 0:
        contagem_positivos += 1
        soma += numero
    lista_de_numeros.append(numero)

print(f"{contagem_positivos}")
print(f"{round((soma / contagem_positivos), 1)}")

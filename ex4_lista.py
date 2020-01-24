"""
Exercício 6: Reescreva o programa que solicita o usuário uma lista de
números e prints e imprime em tela o maior número e o menor número
quando o usuário digitar a palavra “feito”. Escreva um programa para
armazenar as entradas do usuário em uma lista e use as funções max()
e min() para computar o número máximo e o mínimo depois que o laço
for completo.
"""

lista = []
maior_numero = 0
menor_numero = 0

while True:
    entrada = input("Digite um número: ")
    entrada.upper()
    if entrada.isdigit() == False and entrada != "feito":
        continue
    elif entrada.isdigit():
        entrada = int(entrada)
        lista.append(entrada)
    elif entrada == "feito":
        maior_numero = max(lista)
        menor_numero = min(lista)
        print(f"O maior valor: {maior_numero}")
        print(f"O menor valor: {menor_numero}")
        maior_numero = 0
        menor_numero = 0
        lista = []
        continue


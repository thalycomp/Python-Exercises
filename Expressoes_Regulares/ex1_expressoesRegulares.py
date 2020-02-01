""""

Exercício 2: Escreva um programa que procure por uma linha na forma:
Nova Revisão: 39772
Extraia o número de cada linha usando uma expressão regular e o
método findall(). Compute o valor médio dos números e mostre-o.

Arquivo de entrada: mbox.txt
38444.0323119
Arquivo de entrada: mbox-short.txt
39756.9259259

"""

try:
    entrada = input("> ")
    arquivo = open(entrada)

except:
    print("Erro. Arquivo inválido!")
    exit()

import re

cont=0
ls = []
for linha in arquivo:
    linha = linha.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', linha)

    if len(x) > 0:
        cont+=1
        ls.append(int(*x))

ls = (sum(ls))/cont

print(f'O valor médio: {ls:.7f}')

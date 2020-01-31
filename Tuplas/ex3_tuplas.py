"""

Exercício 3: Escreva um programa que leia um arquivo e mostre
as letras em ordem decrescente de frequência. Seu programa deve
converter todas as entradas para Caixa baixa e apenas contar as
letras de a à z. Não conte espaços, dígitos, pontuações, ou qualquer
coisa que não seja uma letra do alfabeto. Encontre textos simples
de diversas línguas diferentes e veja como a frequência de letras
varia entre os idiomas. Compare seis resultados com as tabelas em
https://wikipedia.org/wiki/Letter_frequencies.

"""
try:
    entrada = input("> ")
    arquivo = open(entrada)

except:
    print("Erro. Arquivo inválido!")
    exit()

import string
aux = []
letras = []
d = dict()
for linha in arquivo:
    linha = linha.translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', " ")).lower().rstrip()

    for letra in linha:
        if letra.isdigit():
            continue
        if letra not in d:
            d[letra] = 1
        else:
            d[letra] += 1
lista = []
for chave, valor in list(d.items()):
    lista.append((valor, chave))

lista.sort(reverse=True)
print(*lista)





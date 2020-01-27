"""

Exercício 1: Faça o download de uma cópia do arquivo www.py4e.com/code3/words.tx
Escreva um programa que leia as palavras em words.txt e as armazena
como chaves em um dicionário. Não importa quais são os valores. Então,
você pode usar o operador in como uma maneira rápida de verificar se
uma string está no dicionário.

"""

arquivo = open("words.txt")
palavras = []
dicionario = dict()
lista = []

for frases in arquivo:
    palavras = frases.split()
    lista.extend(palavras)

for chaves in lista:
    dicionario[chaves] = {}

#teste se string se encontra em dicionário:

print("programs" in dicionario)
"""
Exercício 1: Escreva um loop while que inicia no último caractere da
string e caminha para o primeiro caractere, imprimindo cada letra em
uma linha separada.

COM LAÇO FOR
"""

word = input(">  ")

while len(word) >= letter:
    aux = letter * (-1)
    print(word[aux])
    letter += 1
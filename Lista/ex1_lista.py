"""

Exercício 1: Escreva uma função chamada corte que recebe uma lista e
a modifica, removendo o primeiro e o último elemento, e retorna None.
Depois escreva uma função chamada meio que recebe uma lista e retorna
uma nova lista que contém todos, menos o primeiro e o último elemento.

"""

list = list()

while True:
    entrada = input("Digite um elemento para lista ou [s] para sair qnd lista completa > ")
    if entrada == "s": break
    list.append(entrada)

def corte(lista):
    t = lista[1:]
    t = t[:-1]

def meio(lista):
    lista.pop(0)
    lista.pop(-1)
    return lista

print(f"Lista que retorna None: {corte(list)}")
print(f"Retorna a nova lista sem o primeiro e ultimo elemento: {meio(list)}")
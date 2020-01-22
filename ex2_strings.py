"""
Exercício 3: Encapsule esse código em uma função chamada contagem,
e generalize para que ela aceite a string e a letra como argumentos.

"""
palavra = input("Palavra > ")
letter = input("Letra > ")

def contagem(palavra, letra):
    print(palavra.count(letra))

contagem(palavra, letter)

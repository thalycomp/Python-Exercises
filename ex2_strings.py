"""
Exercício 3: Encapsule esse código em uma função chamada contagem,
e generalize para que ela aceite a string e a letra como argumentos.

"""
try:
    palavra = input("Palavra > ")
    letter = input("Letra > ")

    def contagem(palavra, letter):
        contagem = 0
        for letra in palavra:
            if letra == letter:
                contagem = contagem + 1
        return contagem

    resultado = contagem(palavra, letter)
    print(resultado)

except:
    input("Valor inválido!")
"""

Exercicio 4: Baixe a copia do arquivo www.py4e.com/code3/romeo.txt.
Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por
linha. Para cada linha, separe-a em uma lista de palavras usando a função split.
Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista,
adicione ela. Quando o programa terminar de verificar, ordene e imprima estas
palavras em ordem alfabética.**
Digite o nome do arquivo: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

"""

arquivo = open('romeo.txt')
lista_ordenada = []

for linha in arquivo:
    lista_palavras = linha.split()
    for palavra in lista_palavras:
        if palavra in lista_ordenada:
           continue
        else:
            lista_ordenada.append(palavra)

lista_ordenada.sort()
print(lista_ordenada)

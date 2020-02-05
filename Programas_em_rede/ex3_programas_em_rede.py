"""
Exercício 3: Use urllib para replicar o exercício anterior (1) recu-
perando um documento de uma URL, (2) mostrando até 3000 caracteres
e (3) contando o total destes no documento. Não se preocupe sobre os
cabeçalhos para esse exercício, apenas mostre os 3000 primeiros carac-
teres do contepudo do documento.

http://data.pr4e.org/romeo.txt

"""
import urllib.request

try:
    entrada = input("> ")

    arquivo = urllib.request.urlopen(entrada)

except:
    print("URL não encontrada ou URL não formadata corretamente")
    exit()
cont = 0
print()
for linha in arquivo:
    l = linha.decode()
    for caracteres in l:
        if cont < 3000 :
            print(caracteres, end='')
            if caracteres.isspace(): continue
            cont+=1
print('\n')
print(cont)
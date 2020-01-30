"""
Exercício 2: Esse programa conta a distribuição de horas no dia para
cada uma das mensagens. Você pode retirar a hora da linha com “From”
achando a string de horário e então separando ela em partes usando o
caractere “:” (dois pontos). Uma vez acumuladas as contagens para
cada hora, mostre os valores, um por linha, ordenados por hora como
segue abaixo:
python timeofday.py
Digite o nome do arquivo: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

entrada = input("Digite o nome do arquivo: ")
try:
    arquivo = open(entrada)
except:
    print("Erro. Arquivo inválido!")
    exit()

cont = 0
d = dict()
for linha in arquivo:
    if linha.startswith("From "):
        email = linha[-14:-6]
        (horas, minutos, segundos) = email.split(":")
        if horas not in d:
            d[horas] = 1
        else:
            d[horas] = d[horas] + 1

lista = []
for chave, valor in list(d.items()):
    lista.append((chave, valor))

lista.sort()

for chave, valor in lista:
    print(chave, valor)



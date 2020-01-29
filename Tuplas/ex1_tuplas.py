"""
Exercício 1: Revise um programa anterior como é pedido: Leia e analise
as linhas com “From” e retire os endereços dessas linhas. Conte o
número de mensagens de cada pessoa usando um dicionário. Depois de
todos os dados serem lidos, mostre a pessoa com mais envios criando
uma lista de tuplas (contagem, email) do dicionário. Então, ordene a
lista em ordem reversa e mostre a pessoa na primeira posição.
Linha simples:

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Digite o nome do arquivo: mbox-short.txt
cwen@iupui.edu 5
Digite o nome do arquivo: mbox.txt
zqian@umich.edu 195

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
        inicio = linha[5:]
        final = inicio.find(" ")
        email = inicio[:final]
        if email not in d:
            d[email] = 1
        else:
            d[email] = d[email] + 1

lista = []
for chave, valor in list(d.items()):
    lista.append((valor, chave))

lista.sort(reverse=True)

print(*lista[0])





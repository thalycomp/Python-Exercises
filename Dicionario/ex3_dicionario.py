"""
Exercício 3: Escreva um programa que leia um registro de mensagens,
construa um histograma, utilizando um dicionário, para contar quantas
mensagens chegaram em cada endereço de email e mostre em tela o
dicionário.
Saída para mbox-short
Enter a file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""
try:
    entrada = input("> ")
    arquivo = open(entrada)
except:
    print("Erro. Arquivo não encontrado")
    exit()
d = dict()
for linha in arquivo:
    linha = linha.rstrip()
    if linha.find("From:") == -1:
        continue
    meio = linha.find(":")
    emails = linha[meio+2:]
    if emails not in d:
        d[emails] = 1
    else:
        d[emails] = d[emails] + 1

print(d)

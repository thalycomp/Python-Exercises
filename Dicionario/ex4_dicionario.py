"""
Exercício 4: Adicione linhas de código no programa abaixo para iden-
tificar quem possui mais mensagens no arquivo. Após todo o dado ser
lido e todo o dicionário ser criado, procure no dicionário, utilizando um
laço máximo (Veja o capítulo 5: Laços máximo e mínimo), quem tem o
maior número de mensagens e mostre em tela quantas mensagens essa
pessoa tem.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
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
maximo = 0
max_email = None
for email in d:
    if maximo is 0 or d[email] > maximo:
            maximo = d[email]
            max_email = email

print('Máximo:', max_email, maximo)


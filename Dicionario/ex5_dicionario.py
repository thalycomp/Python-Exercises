"""

Exercício 5: Esse programa grava o domínio de email (ao invés do en-
dereço) de onde a mensagem foi enviada ao invés de quem o email veio (
i.e., o endereço completo da mensagem). No final do programa, mostre
em tela o conteúdo do seu dicionário.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

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
    meio = linha.find("@")
    emails = linha[meio+1:]
    if emails not in d:
        d[emails] = 1
    else:
        d[emails] = d[emails] + 1

print(d)

"""
Exercício 2: Altere seu programa de soquete para que ele conte o
número de caracteres que recebeu e pare de mostrar qualquer texto
depois que mostrar 3000 caracteres. O programa deve recuperar o doc-
umento inteiro e contar o número total de caracteres e mostrar o resul-
tado da contagem no final do documento.

"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    pagina = input("> ")
    pag = pagina.split('/')

    mysock.connect((pag[2], 80))
    cmd = 'GET '+pagina+' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)
except:
    print("URL não encontrada ou URL não formadata corretamente [Use http://]")
    exit()
 
cont = 0
while True:

    data = mysock.recv(512)
    if len(data) < 1:
        break
    data = data.decode()
    for d in data:
        if cont < 3000:
            print(d, end='')
            cont += 1

    #print(data.decode(),end='')

print(f'\n {cont} caracteres')

mysock.close()
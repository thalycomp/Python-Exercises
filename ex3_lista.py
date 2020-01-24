"""
Exercício 5: Escreva um programa que leia uma caixa de email, e quando
você encontrar uma linha que comece com “De”, você vai separar a linha
em palavras usando a função split. Nós estamos interessados em quem
envia a mensagem, que é a segunda palavra na linha que começa com
From.
De stephen.marquard@uct.ac.za Sáb Jan 5 09:14:16 2008
Você vai analisar a linha que começa com From e irá pôr para imprimir
na tela a segunda palavra (para cada linha do tipo), depois o programa
também deverá contar o número de linhas que começam com “De” e
imprimir em tela o valor final desse contador.

"""

entrada = input("Digite o nome do arquivo: ")
try:
    arquivo = open(entrada)
except:
    print("Erro. Arquivo inválido!")
    exit()

cont = 0
for linha in arquivo:
    if linha.startswith("From"):
        palavras = linha.split()
        cont += 1
        print(palavras[1])

print(f"Há {cont} linhas no aquivo {entrada} que tem From como a primeira palavra ")

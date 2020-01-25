"""
Exercício 1: Escreva um programa que leia o arquivo Mbox-short e mostre o con-
teúdo deste (linha por linha), completamente em caixa alta.

"""
try:
    entrada = input("Arquivo > ")
    arquivo = open(entrada)
except:
    print("Erro. Arquivo não encontrado. ")
    exit()

for linha in arquivo:
    linha = linha.rstrip()
    linha = linha.upper()
    print(linha)
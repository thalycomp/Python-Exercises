"""
Exercício 2: Escreva um programa que solicite um arquivo e então leia
ele e procure por linhas da forma:
X-DSPAM-Confidence: 0.8475
Quando encontrar uma linha que inicie com “X-DSPAM-Confidence:”
separe a linha do texto para extrair o número de ponto flutuante que
ela contém. Conte essas linhas e então compute o total de valores de
Confiança de Spam nelas. Quando chegar no fim do arquivo, mostre a
média de Confiança de Spam.

"""
try:
    entrada = input("Arquivo > ")
    arquivo = open(entrada)
except:
    print("Erro. Arquivo não encontrado. ")
    exit()

for linha in arquivo:
    if linha.startswith("X-DSPAM-Confidence:"):
        inicio = linha.find(" ")
        nv_ = linha[inicio+1::]
        print(nv_)


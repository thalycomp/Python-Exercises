"""
Exercício 2: Escreva um programa que solicite um arquivo e então leia
ele e procure por linhas da forma:
X-DSPAM-Confidence: 0.8475

"""
try:
    entrada = input("Arquivo > ")
    arquivo = open(entrada)
except:
    print("Erro. Arquivo não encontrado. ")
    exit()

for linha in arquivo:
    if linha.startswith("X-DSPAM-Confidence: 0.8475"):
        print(linha)

"""
Exercício 2: Às vezes, quando os programadores estão entediados ou
querem um pouco de diversão, eles adicionam um Easter Egg inofensivo
em seus programas. Modifique o programa que solicita um arquivo ao
usuário para que ele mostre uma mensagem engraçada quando o usuário
deigitar no nome do arquivo “na na boo boo”. O programa deve se
comportar normalmente para todos os outros arquivos que existem e
que não existem. Aqui está uma amostra da execução desse programa:
python egg.py
Digite o nome de um arquivo: mbox.txt
Há 1797 linhas de assunto em mbox.txt
python egg.py
Digite o nome de um arquivo: missing.tyxt
Arquivo não pôde ser aberto: missing.tyxt
python egg.py
Digite o nome de um arquivo: na na boo boo
NA NA BOO BOO PRA VOCÊ TAMBÉM!

"""

entrada = input("Arquivo > ")
entrada = entrada.lower();

if entrada == "na na boo boo":
    print("NA NA BOO BOO PRA VOCÊ TAMBÉM!")
    exit()

try:
    arquivo = open(entrada)

except:
    print("Erro. Arquivo não encontrado. ")
    exit()
cont = 0

for linha in arquivo:
    cont += 1

print(f"Há {cont} linhas de texto em {entrada} ")
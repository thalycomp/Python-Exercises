"""
Exercício 4: Altere o programa urllinks.py para extrair e contar as
tags de parágrafos (p) do documento de HTML recuperado e mostrar a
contagem dos parágrafos como uma saída do seu programa.Não mostre
o conteúdo, apenas conte-os. Teste seu programa em várias páginas da
web pequenas e também em algumas maiores.

"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

except:
    print("URL não encontrada ou URL não formadata corretamente")
    exit()

cont = 0
tags = soup('p')
for tag in tags:
    cont +=1

print(cont)

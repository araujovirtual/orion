
import re
import matplotlib.pyplot as plt
from datetime import datetime as dt

'''
Sistema de monitoria de logs
Trainees: Jucinaldo.S.A - UTFPR - RA 02296500
Trainess: Jackson - UTFPR

Backend : Por Jucinaldo
Frontend : Por JackSon
'''



# Cria um array de um lista de objetos
lista = []
# Caminho do arquivo
arquivo = open("arquivos/valores.txt", 'r')

# Abre o arquivo , explode, e separa por virgula cada index
for linha in arquivo:
    linha = linha.strip()
    linha = linha.split(',')
    lista.append(linha)
# fecha o arquivo
arquivo.close()

# cria um lista de objetos com os dados filtrados 
dados = []
for l in lista:
    for x in l:
        x = re.search(
            r'a0:-?\d*|a1:-?\d*|a2:-?\d*|a3:-?\d*|a4:-?\d*|a5:-?\d*|a6:-?\d*|a7:-?\d*', x)
        if x:
            # insere os dados caso o filtro tenha sido aplciado
            dados.append(x.group())




# Quantidade de amostras
n = len(dados)
# Monta a tabela 0.25ms * numero de linhas = tempo
xx = [float(dados[x][3:]) for x in range(0, len(dados),1)]




# Gera um grafo simples
#with plt.style.context('dark_background'):
plt.title('Orion 2021')
plt.plot(xx)
plt.xlabel("TEMPO")
plt.ylabel("DADOS")
plt.show()




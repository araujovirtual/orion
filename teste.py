from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import re

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


# Cria uma subplot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

# iterações e tempos inicias
iteracoes = 0
tempo = len(dados)

# Cria os axes para os sliders
tt = plt.axes([0.125, 0.1, 0.78, 0.03])
ii = plt.axes([0.125, 0.2, 0.78, 0.03])

# Cria o slider propriamente dito
t = Slider(tt, "Tempo", 1.0, len(dados))
i = Slider(ii, "Iterações", 0.0, len(dados))


<<<<<<< HEAD
# Função para atualizar os valores
=======


# Cria os sliders
tt = plt.axes([0.125,0.1,0.78,0.03])
ii = plt.axes([0.125,0.2,0.78,0.03])

t = Slider(tt,"Tempo",1.0,len(dados))
i = Slider(ii,"Iterações",0.0,len(dados))

>>>>>>> 0c8c3d45dd08366ecf8371dc231d6d99eff30081
def update(val):
    ax.clear()
    tempo = t.val
    iter = i.val
    #print(int(tempo))
    xx = [float(dados[x][3:])
          for x in range(int(iter), len(dados), int(tempo))]
    ax.plot(xx)


# Captura o evento do click ou da mudança
t.on_changed(update)
i.on_changed(update)

<<<<<<< HEAD
# Plota o gráfico
=======

>>>>>>> 0c8c3d45dd08366ecf8371dc231d6d99eff30081
plt.show()

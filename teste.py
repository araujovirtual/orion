from matplotlib import colors, cycler
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import re
'''
CRIADO E DESENVOLVIDO POR J.S.ARAUJO

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

# Cria uma subplot
fig, ax = plt.subplots()
fig.set_size_inches(10.5, 5.5)
fig.canvas.manager.set_window_title('ORION')
fig.patch.set_facecolor('#E0E0E0')
fig.patch.set_alpha(0.5)

# Configuração da figura plot
colors = cycler('color',
                ['#EE6666', '#3388BB', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])
plt.subplots_adjust(bottom=0.35)
plt.title("ORION")
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)

# Seta informações de label
def btl():
    ax.set_ylabel("Balança")
    ax.set_xlabel("Tempo")
    

# iterações e tempos inicias
iteracoes = 0
tempo = len(dados)

# Cria os axes para os sliders
tt = plt.axes([0.125, 0.1, 0.78, 0.03])
ii = plt.axes([0.125, 0.2, 0.78, 0.03])
rs = plt.axes([0.8, 0.025, 0.1, 0.04])

# Cria o slider propriamente dito
t = Slider(tt, "Tempo", 1.0, len(dados))
i = Slider(ii, "Iterações", 0.0, len(dados))

# Botão de reset
bt = Button(rs, 'Resetar', color='gold',
                hovercolor='skyblue')

# Função para atualizar os valores
def update(val):
    #ax.clear()
    ax.cla()
    tempo = t.val
    iter = i.val
    # print(int(tempo))
    xx = [float(dados[x][3:])
          for x in range(int(iter), len(dados), int(tempo))]
    btl()
    ax.plot(xx)

# Função para resetar
def reset(event):
    t.reset()
    i.reset()
    ax.clear()
    btl()

# Captura o evento do click ou da mudança
t.on_changed(update)
i.on_changed(update)
bt.on_clicked(reset)
# Plota o gráfico
plt.show()

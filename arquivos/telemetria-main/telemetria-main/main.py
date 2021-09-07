import matplotlib.pyplot as plt



t = []
p = []
s = []
l1 = []
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []

ocorrencia = ['@t:0', 'P:0.00', 'S:0', 'L:0#*']

lista = []
contador = 0
dataset = open('valores.txt', 'r')
for line in dataset:
    line = line.strip()
    line = line.split(',')
    lista.append(line)


dataset.close()

for l in lista:
    if l == ocorrencia:
        continue
    #print (l)
            
    for x in l:
        
        if (x[0:2] == "@t"):
            t.append(x)
        if (x[0:2] == "P:"):
            p.append(x)
        if (x[0:2] == "S:"):
            s.append(x)
        if (x[0:2] == "L:"):
            l1.append(x.replace("#a0", ""))
        if (x[0:2] == "a1"):
            a1.append(x)
        if (x[0:2] == "a2"):
            a2.append(x)
        if (x[0:2] == "a3"):
            a3.append(x)
        if (x[0:2] == "a4"):
            a4.append(x)
        if (x[0:2] == "a5"):
            a5.append(x)
        if (x[0:2] == "a6"):
            a6.append(x)
        if (x[0:2] == "a7"):
            a7.append(x)
        if (x[0:3] == "$c0"):
            c0.append(x)
        if (x[0:2] == "c1"):
            c1.append(x)
        if (x[0:2] == "c2"):
            c2.append(x)
        if (x[0:2] == "c3"):
            c3.append(x)
        if (x[0:2] == "c4"):
            c4.append(x)
        if (x[0:2] == "c5"):
            c5.append(x)
        if (x[0:2] == "c6"):
            c6.append(x.replace("*", ""))
        if (x[0:2] == "c7"):
            c7.append(x)


#print(a1[0][3:])  # Linha 1
#print(a1[1][3:])  # Linha 2
#print(a1[2][3:])  # Linha 3
#print(a1[3][3:])  # Linha 3
#print(c0[0][4:])



texto_triger = ['Gatilho']
texto_temp = ['Temp']
texto_estado = ['Eestado']
texto_amostra_balanca = ['A1','A2','A3','A4','A5','A6','A7']
texto_amostra_timestamp = ['C1','C2','C3','C4','C5','C6','C7','C8']
texto_L = ["L"]

valores_estado_triger = [t[0][3:]]
valores_l = [l1[0][4:]]
valores_temp = [p[0][2:]]
valores_estado = [s[0][2:]]
valores_amostra_balanca = [a1[0][3:],a2[0][3:],a3[0][3:],a4[0][3:],a5[0][3:],a6[0][3:],a7[0][3:]]
valores_amostra_timestamp = [c0[0][4:],c1[0][3:],c2[0][3:],c3[0][3:],c4[0][3:],c5[0][3:],c6[0][3:],c7[0][3:].replace("*","")]


#print(lista)
print(texto_triger)
print(texto_temp)
print(valores_estado_triger)
print(valores_l)
print(valores_temp)
print(valores_estado)
print(valores_amostra_balanca)
print(valores_amostra_timestamp)

fig , axs = plt.subplots(4,2)
fig.suptitle('Valores unica linha')
plt.rcParams.update({'font.size': 6})
axs[0, 0].plot(texto_amostra_balanca, valores_amostra_balanca , 'tab:orange')
axs[0, 0].set_title("Valores de amostra timestamp")
axs[1, 0].plot(texto_amostra_timestamp, valores_amostra_balanca, 'tab:red')
axs[1, 0].set_title("Valores de amostra de balanca")
axs[1, 1].plot(texto_estado, valores_estado, 'tab:blue')
axs[1, 1].set_title("Valores de amostra de estado")
axs[2, 0].sharex(axs[2, 0])
axs[2, 0].plot(texto_triger, valores_estado_triger, 'tab:pink')
axs[2, 0].set_title("Valores de amostra do gatilho")
axs[2, 1].plot(texto_temp, valores_temp, 'tab:cyan')
axs[2, 1].set_title("Valores de temperatura")
axs[3, 0].plot(texto_L, valores_l, 'tab:cyan')
axs[3, 0].set_title("Valores de L(Não informado")


fig.tight_layout()
#plt.show()



texto_a1 = [(""+str(x)) for x in range(len(a1))]
valores_a1 = [int(x.replace("a1:", "")) for x in a1]

texto_a2 = [(""+str(x)) for x in range(len(a2))]
valores_a2 = [int(x.replace("a2:", "")) for x in a2]

texto_a3 = [(""+str(x)) for x in range(len(a3))]
valores_a3 = [int(x.replace("a3:", "")) for x in a3]

texto_a4 = [(""+str(x)) for x in range(len(a4))]
valores_a4 = [int(x.replace("a4:", "")) for x in a4]

texto_a5 = [(""+str(x)) for x in range(len(a5))]
valores_a5 = [int(x.replace("a5:", "")) for x in a5]

texto_a6 = [(""+str(x)) for x in range(len(a6))]
valores_a6 = [int(x.replace("a6:", "")) for x in a6]

texto_a7 = [(""+str(x)) for x in range(len(a7))]
valores_a7 = [int(x.replace("a7:", "")) for x in a7]

texto_l = [(""+str(x)) for x in range(len(l1))]
valores_l = [int(x[4:]) for x in l1]


text_c1 = [(""+str(x)) for x in range(len(c1))]
valores_c1 = [int(x.replace("c1:", "")) for x in c1]


plt.plot(texto_a1, valores_a1, 'o-', color='lightgrey', label='A1')
plt.plot(texto_a2,valores_a2 ,'o-', label='A2')
plt.plot(texto_a3,valores_a3 ,'o-', label='A3')
plt.plot(texto_a4,valores_a4 ,'o-', label='A4')
plt.legend()
plt.title('outro exemplo')

fig, (ax1, ax2) = plt.subplots(2)
plt.rcParams.update({'font.size': 6})
fig.suptitle('Vertical')
ax1.plot(texto_a1, valores_a1)
ax2.plot(texto_a2, valores_a2)


fig, axs = plt.subplots(5, 2)
fig.suptitle('Valores A linha a linha')
axs[0, 0].plot(texto_a1, valores_a1,'tab:orange')
axs[0, 0].set_title("Valores de A1")
axs[1, 0].plot(texto_a2, valores_a2, 'tab:green')
axs[1, 0].set_title("Valores de A2")
axs[1, 0].sharex(axs[0, 0])
axs[0, 1].plot(texto_a3, valores_a3, 'tab:blue')
axs[0, 1].set_title("Valores de A3")
axs[1, 1].plot(texto_a4, valores_a4, 'tab:pink')
axs[1, 1].set_title("Valores de A4")
axs[2, 0].sharex(axs[0, 0])
axs[2, 0].plot(texto_a5, valores_a5, 'tab:cyan')
axs[2, 0].set_title("Valores de A5")
axs[2, 1].sharex(axs[0, 0])
axs[2, 1].plot(texto_a6, valores_a6, 'tab:brown')
axs[2, 1].set_title("Valores de A6")
axs[3, 0].sharex(axs[0, 0])
axs[3, 0].plot(texto_a7, valores_a7, 'tab:olive')
axs[3, 0].set_title("Valores de A7")
axs[3, 1].plot(texto_l, valores_l, 'tab:olive')
axs[3, 1].set_title("Valores de C")
axs[4, 0].plot(text_c1, valores_c1, 'tab:olive')
axs[4, 0].set_title("Valores de C")

fig.tight_layout()





plt.show()


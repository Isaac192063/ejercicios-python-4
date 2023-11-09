import pandas as pd
import pprint as prin
from tabulate import tabulate

arrayDesordenado  = []
data = pd.read_excel(
    "data.xlsx", sheet_name="Hoja1", index_col=None, header=None
)

NUM_FILA = data.shape[0]

LIMITE = 26
# extraccion de los datos del excel
matriz = [ data.loc[i].to_list() for i in range(NUM_FILA)]

# hacemos la division entre costo y volumen
division = [ costo/volumen for costo, volumen in zip(matriz[0], matriz[1]) ]

# ordenamos las filas de costo y volumen por separadao en base a la relacion de costo y volumen
costos =  [x for _, x in sorted(zip(division, matriz[0]), reverse=True)]
volumen1 = [x for _, x in sorted(zip(division,matriz[1]), reverse=True)]

# definimos el indice del array
matriz.append([i+1 for i in range(len(matriz[0])-1,-1, -1)])
# ordenamos de igual manera los indices para poder guiarnos en base a la relacion de costo y volumen
aux = [x for _, x in sorted(zip(division, matriz[2]), reverse=True)]

sum ,sum1 = 0,0
i = 0
rta = []
res = {}

# hacemos la suma de la fila de volumen hasta cumplir con la restriccion
while sum<LIMITE:
    res = {"costo": sum1, "volumen":sum}
    sum1 += costos[i]
    sum += volumen1[i]
    if sum<LIMITE:
        # si aun no se cunple con la restriccion vamos agregando el numeros de los indices ordenados
        rta.append(aux[i])
    i+=1

auxSol = []
total = 0

# buscamos los indices ordenaodos que se cumplen en el indice definido anteriormente antes de ordenar
for j in matriz[2]:
    if j in rta:
        auxSol.append(1)
    else:
        auxSol.append(0)
matriz.append(auxSol)


matriz[2] = [i+1 for i in range(len(matriz[2]))]
# definicion del indice en orden
prin.pprint(matriz)

# # visualizacion de los datos en una tabla
# title = [["costos"],["volumen"], ["indice"], ["seleccion"]] # titulo

# table_data = [ title[i] + row for i, row in enumerate(matriz)] # datos

# table = tabulate(table_data, tablefmt="fancy_grid")
# print(table)
# # resultado de la suma
# print(res)

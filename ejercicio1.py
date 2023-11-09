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
division = []
for costo, volumen in zip(matriz[0], matriz[1]):
    division.append(costo / volumen)

    
sum ,sum1 = 0,0
i = 0
res = {}
# hacemos la suma de la fila de volumen hasta cumplir con la restriccion
while sum<LIMITE:
    res = {"costo": sum1, "volumen":sum}
    sum1 += matriz[0][i]
    sum += matriz[1][i]
    i+=1

auxSol = []
total = 0

# como no se ordenada solo hacemos la suma hasta que se cumpla la restriccion 
for volumen in matriz[1]:
    total += volumen
    # verificamos la condicion
    if total < LIMITE:
        auxSol.append(1)
    else:
        auxSol.append(0)
matriz.append(auxSol)

prin.pprint(matriz)

# visualizacion de los dataos en un tabla 
title = [["costos"],["volumen"], ["seleccion"]]

table_data = [ title[i] + row for i, row in enumerate(matriz)]

table = tabulate(table_data, tablefmt="fancy_grid")
print(table)
print(res)
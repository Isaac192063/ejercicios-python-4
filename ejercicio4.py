import numpy as np
import pprint as pr
import pandas as pd
from tabulate import tabulate

arrayDesordenado  = []
data = pd.read_excel(
    "data.xlsx", sheet_name="Hoja1", index_col=None, header=None
)

NUM_FILA = data.shape[0]
LIMITE = 26
# extraccion de los datos del excel
data = [ data.loc[i].to_list() for i in range(NUM_FILA)]

AGlobal = []
div = []
LIMIT = 26

# hacemos la division entre costo y volumen
div = [ costos/volumen for costos, volumen in zip(data[0], data[1])] 

# creamso un indice
# es importante que este indice este de mayor a menor debido a que en el momento de ordenqarlo y darle la vuelta los
# los valores iguales en la division afecta y quedan invertidos pero si los hacemos normal el que da estable 

ax = [i+1 for i in range(9,-1, -1)] 
# ordenamso lso sub arrays en base a la relacion de costo y volumen
costos = [x for _,x in sorted(zip(div,data[0] ), reverse=True)]
volumen = [x for _,x in sorted(zip(div, data[1]), reverse=True)]
indice = [x for _, x in sorted(zip(div,ax), reverse=True)]


# creamos un array numpy para poder hacer uso del array_aplit y dividir con facilidad
array1 = np.array([
   costos, volumen
])
# pedimos el numero de particiones del array
NUM_DIV = int(input('ingrese el numero a dividir: '))

for arr in array1:
  aux = []
  partes = np.array_split(arr, NUM_DIV)

  for subArray in partes:
      aux.append(subArray.tolist())
  AGlobal.append(aux)

auxiliar = []

# en esas mismas particiones hacemos el indice
partes = np.array_split(indice, NUM_DIV)
for subArray in partes:
    auxiliar.append(subArray.tolist())

total = 0
total1 = 0
j = 0
i = 0
contador = 0
AGlobal.append(indice)

rta = []
res = {}
# suamamos tenieendo en cuenta los ciclos de las particiones del array
while total < LIMIT:
    res = {"volumen": total, "costo": total1}
    total += AGlobal[1][j][i]
    total1 += AGlobal[0][j][i]
    #  si se cumple la condicion vamos guardando los indices en un array
    if total < LIMIT:
       rta.append(auxiliar[j][i])

    contador += 1

    i += 1
    # esta condicion es para que cada vez que sean las posiciones de los subarrays se reincion y los vaya recorriendo
    # ya que al final es un array de 3 dimensiones
    if contador % len(AGlobal[1][j]) == 0:
        j += 1
        i = 0

seleccion = []

# conforme en los indices ordenanaos segun la disvion los buscamos en el arreglo original de lso indices
for i1 in ax:
    if i1 in rta:
        seleccion.append(1)
    else:
        seleccion.append(0)

data.append([i+1 for i in range(len(data[1]))])

data.append(seleccion)


pr.pprint(data)

# visualizacion de los datos a través de una tabla 
title = [["costos"],["volumen"], ["indice"], ["seleccion"]]

table_data = [ title[i] + row for i, row in enumerate(data)]

table = tabulate(table_data, tablefmt="fancy_grid")
print(table)
print(res)
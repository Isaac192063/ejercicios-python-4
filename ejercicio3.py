import numpy as np
import pprint as pr
import pandas as pd
from tabulate import tabulate

arrayDesordenado  = []
data = pd.read_excel(
    "data.xlsx", sheet_name="Hoja1", index_col=None, header=None
)

NUM_FILA = data.shape[0]
# extraccion de los datos del excel
array = [ data.loc[i].to_list() for i in range(NUM_FILA)]

matriz = []
div = []
LIMIT = 26

# creamos un array de numpy con los datos anteriormente mencionados 
array1 = np.array(array)
# pedimos un numero el cual va a represe tar el numeor de divisiones del array
NUM_DIV = int(input('ingrese el numero a dividir: '))

# dividimos el array segun el numero ingresado
for arr in array:
  aux = []
  partes = np.array_split(arr, NUM_DIV)

  for subArray in partes:
      aux.append(subArray.tolist())
  matriz.append(aux)


# hacemos la division conforme a las divisiones ingresadas anteriormente
s = 0
a1 = []
l= len(array[0])-1
for n in range(len(matriz[0])):
  aux = []
  s1 = []
  for k in range(len(matriz[0][n])):
    operaccion = matriz[0][n][k] / matriz[1][n][k]
    s1.append(l+1)
    l-=1
    aux.append(operaccion)
  div.append(aux)
  a1.append(s1)


copia = [[], [], []]
matriz.append([i+1 for i in range(9,-1, -1)])

# ordenamos los arrsy y el indice en base a la relacion de costo y volumen
for n in range(len(matriz[s])):
  # utilizamos el parametro de reverse debido a que originalmente solo se ordena de mayor a menor y nosotros
  # los necesitamos es al contrario
  copia[0].append([x for _, x in sorted(zip(div[n], matriz[0][n]), reverse=True)])
  copia[1].append([x for _, x in sorted(zip(div[n], matriz[1][n]), reverse=True)])
  copia[2].append([x for _, x in sorted(zip(div[n], a1[n]), reverse=True)])
 

# sumar
total = 0
total1 = 0
j = 0
i = 0
contador = 0

rta = []
res = {}
# suamamos tenieendo en cuenta los ciclos de las particiones del array
while total < LIMIT:
    res = {"volumen": total, "costo": total1}
    total += copia[1][j][i]
    total1 += copia[0][j][i]
    if total < LIMIT:
      #  si se cumple la condicion vamos guardando los indices en un array
       rta.append(copia[2][j][i])
    contador += 1
    i+=1
    if contador % len(copia[1][j]) == 0:
        j += 1
        i = 0


seleccion = []
# conforme en los indices ordenanaod segun la disvion los buscamos en el arreglo original de lso indices
for i1 in matriz[2]:
   if i1 in rta:
      seleccion.append(1)
   else:
      seleccion.append(0)
# como hemso estasdo trabajanod con indice invertido lo volemso a la normalidad
array.append([i+1 for i in range(len(array[0]))])

array.append(seleccion)

pr.pprint(array)

# visualizacion de los datos a través de una tabla 

title = [["costos"],["volumen"], ["indice"], ["seleccion"]]

table_data = [ title[i] + row for i, row in enumerate(array)]

table = tabulate(table_data, tablefmt="fancy_grid")
print(table)
print(res)
# Dada la lista de enteros nums, mueve todos los ceros al final de la misma, 
# manteniendo el orden relativo de los elementos no nulos.

# Reto: reordena los valores “in place”, sin hacer una copia de la lista.

from typing import List

def mover_ceros(numeros: List[int]) -> None:
   p1 = 0
   for p2 in range(len(numeros)):
       if numeros[p2] != 0:
           numeros[p2], numeros[p1] = numeros[p1], numeros[p2]
           p1+=1
  #  for p2 in range(p1,len(numeros)):
  #      numeros[p2] = 0
   return numeros

numeros = [0,1,0,3,12]

numeros = mover_ceros(numeros)

print(numeros)
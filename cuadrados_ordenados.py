# Dado un arreglo de números enteros ordenados en orden ascendente, 
# devuelve una matriz de los cuadrados de cada número ordenados en orden no decreciente.

from typing import List

def cuadrados_ordenados(números: List[int]) -> List[int]:
   p1 = 0
   p2 = len(números)-1
   respuesta = [0]*len(números)
   p_respuesta = len(números)-1
  
   while p_respuesta >= 0:
       if abs(números[p1]) > abs(números[p2]):
           respuesta[p_respuesta] = (números[p1])**2
           p1 += 1
           p_respuesta -= 1
       if abs(números[p1]) <= abs(números[p2]):
           respuesta[p_respuesta] = (números[p2])**2
           p2 -= 1
           p_respuesta -= 1
   return respuesta

nums = [-4,-1,0,3,10]
nums = cuadrados_ordenados(nums)
print(nums)

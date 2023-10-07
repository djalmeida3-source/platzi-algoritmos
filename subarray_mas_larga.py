# Dado un arreglo de valores binarios y un entero k, encuentra el máximo número de 1s consecutivos. Puedes cambiar k 0s por el valor 1.

from typing import List

def subarray_mas_larga(list: List[int], K: int) -> int:
   comienzo = 0
   cuentaCeros = 0
   mayorLongitud = 0
   for final in range(len(list)):
       if list[final] == 0: cuentaCeros += 1
       while cuentaCeros > K:
           if list[comienzo] == 0: cuentaCeros -= 1
           comienzo += 1
       mayorLongitud = max(mayorLongitud, final - comienzo + 1)
   return mayorLongitud

nums = [0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1] 
k = 3

print(subarray_mas_larga(nums, k))


# Escribe una función que invierta una cadena. La cadena de entrada se da como un arreglo de caracteres.

# Reto: hacerlo modificando la lista de entrada con O(1) de memoria extra.

from typing import List

def invertir_string(cadena: List[str]) -> None:
   p1 = 0
   p2 = len(cadena) - 1
   while p1 < p2:
       cadena[p1], cadena[p2] = cadena[p2], cadena[p1]
       p1 += 1
       p2 -= 1
   return cadena

# s = ["h", "e", "l", "l", "o"]
s = ["H", "a", "n", "n", "a", "h"]
s = invertir_string(s)

print(s)
# Dado un arreglo nums con n objetos de color rojo, blanco o azul, 
# ordénalos en su lugar para que los objetos del mismo color sean adyacentes, con los colores en el orden rojo, blanco y azul.

# Utilizaremos los enteros 0, 1 y 2 para representar el color rojo, blanco y azul, respectivamente.

# Reto 1: debes resolver este problema sin utilizar la función de ordenación de la biblioteca.

# Reto 2: ¿podrías idear un algoritmo de una sola pasada utilizando solo un espacio extra constante?

from typing import List

def reordenar_colores(nums: List[int]) -> None:
    p2, p1, p3 = 0, 0, len(nums) - 1
    while p2 <= p3:
       if nums[p2] == 0:
           if p2 == p1:
               p2 += 1
               continue
           nums[p1], nums[p2], p1 = nums[p2], nums[p1], p1 + 1
       elif nums[p2] == 2:
           nums[p3], nums[p2], p3 = nums[p2], nums[p3], p3 -1
       else:
           p2 += 1
    return nums

numeros = [2,0,2,1,1,0]

numeros = reordenar_colores(numeros)

print(numeros)
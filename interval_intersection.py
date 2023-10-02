# Dadas dos listas de intervalos cerrados, lista1 y lista2, donde lista1[i] = [inicio_i, final_i] y lista2[j] = [inicio_j, final_j]. 
# Cada lista de intervalos es disjunta por pares y está ordenada.

# Devuelve la intersección de estas dos listas de intervalos.

# Un intervalo cerrado [a, b] (con a <= b) denota el conjunto de números reales x con a <= x <= b. 
# La intersección de dos intervalos cerrados es un conjunto de números reales que está vacío o representado como un intervalo cerrado. 
# Por ejemplo, la intersección de [1, 3] y [2, 4] es [2, 3].

from typing import List

def intervalIntersection(lista1: List[List[int]], lista2: List[List[int]]) -> List[List[int]]:
   pila = []
   p1 = 0
   p2 = 0
   while p1 < len(lista1) and p2 < len(lista2):
       low = max(lista1[p1][0],lista2[p2][0])
       high = min(lista1[p1][1],lista2[p2][1])
       if low <= high:
           pila.append([low,high])
       if lista1[p1][1] < lista2[p2][1]:
           p1+=1
       else:
           p2+=1
   return pila

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print(intervalIntersection(firstList, secondList))


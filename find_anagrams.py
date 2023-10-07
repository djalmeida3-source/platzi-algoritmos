# Dadas dos cadenas s y p, devuelva un arreglo con todos los índices de inicio de los anagramas de p en s. 
# Puede devolver la respuesta en cualquier orden.

# Un anagrama es una palabra o frase que se forma reordenando las letras de otra palabra o frase, 
# normalmente utilizando todas las letras originales exactamente una vez.

from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
   contadorAnagrama = [0]*26
   contadorString = [0]*26
   for num in p:
       contadorAnagrama[ord(num)-ord('a')]+=1
   comienzo = 0
   posiciones = []
   for final in range(len(s)):
       contadorString[ord(s[final])-ord('a')]+=1
       if contadorString == contadorAnagrama:
           posiciones.append(comienzo)
       if len(p) <= final - comienzo+1:
           contadorString[ord(s[comienzo])-ord('a')]-=1
           comienzo+=1
   return posiciones

s = "abab"
p = "ab"

print(findAnagrams(s,p))